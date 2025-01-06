#include "rclcpp/rclcpp.hpp"
#include "my_robot_interfaces/msg/hardware_status.hpp"

class HardwareStatusPublisher : public rclcpp::Node
{
public:
    HardwareStatusPublisher() : Node("hardware_status_publisher")
    {
        pub_ = this->create_publisher<my_robot_interfaces::msg::HardwareStatus>(
            "hardware_status_cpp", 10
        );
        
        timer_ = this->create_wall_timer(
            std::chrono::seconds(1),
            std::bind(&HardwareStatusPublisher::publishHardwareStatus, this)
        );

        RCLCPP_INFO(this->get_logger(), "Hardware status publisher has been started!");

    }

private:

    void publishHardwareStatus()
    {
        auto msg = my_robot_interfaces::msg::HardwareStatus();
        msg.temperature = 60;
        msg.are_motors_ready = false;
        msg.debug_message = "Motors are getting hot!";
        pub_->publish(msg);
    }

    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<my_robot_interfaces::msg::HardwareStatus>::SharedPtr pub_;
};

int main(int argc, char **argv){

    // Initialize ROS2 communication
    rclcpp::init(argc, argv);

    // Object created into Shared pointer 
    // auto node = std::make_shared<rclcpp::Node>("cpp_test");

    // RCLCPP_INFO(node->get_logger(), "Hello CPP Node");

    auto node = std::make_shared<HardwareStatusPublisher>();

    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}