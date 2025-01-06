#include "rclcpp/rclcpp.hpp"
#include "my_robot_interfaces/msg/hardware_status.hpp"

class HardwareStatusSubscriber : public rclcpp::Node
{
public:
    HardwareStatusSubscriber() : Node("hardware_status_subscriber")
    {
        subscriber_ = this->create_subscription<my_robot_interfaces::msg::HardwareStatus>(
            "hardware_status_cpp", 10, std::bind(&HardwareStatusSubscriber::callbackHardwareStatus, this, std::placeholders::_1)
        );

        RCLCPP_INFO(this->get_logger(), "Hardware Status Subscriber has been started!");
    }

private:

    void callbackHardwareStatus(const my_robot_interfaces::msg::HardwareStatus::SharedPtr msg) 
    {
        // RCLCPP_INFO(this->get_logger(), "Are motors ready: %s", std::to_string(msg->are_motors_ready));
        RCLCPP_INFO(this->get_logger(), "Temperature: %ld", msg->temperature);
    }
    rclcpp::Subscription<my_robot_interfaces::msg::HardwareStatus>::SharedPtr subscriber_;

};

int main(int argc, char **argv){

    // Initialize ROS2 communication
    rclcpp::init(argc, argv);

    // Object created into Shared pointer 
    // auto node = std::make_shared<rclcpp::Node>("cpp_test");

    // RCLCPP_INFO(node->get_logger(), "Hello CPP Node");

    auto node = std::make_shared<HardwareStatusSubscriber>();

    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}