#include <stdio.h>
#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

// Creating C++ Node with OOP
class RobotNewsStationNode: public rclcpp::Node
{
    public:
        RobotNewsStationNode(): Node("robot_news_station"), robot_name_("R2D2")
        {
            publisher_ = this->create_publisher<example_interfaces::msg::String>("robot_news", 10);
            timer_ = this->create_wall_timer(std::chrono::seconds(1),
                                             std::bind(&RobotNewsStationNode::publishNews, this));

            RCLCPP_INFO(this->get_logger(), "Robot News Station has been started.");
        };
    
    private:

        void publishNews()
        {
            auto msg = example_interfaces::msg::String();
            msg.data = std::string("Hi, this is ") + robot_name_ + std::string(" from the Robot News Station");
            publisher_->publish(msg);
        }

        std::string robot_name_;
        rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;
        rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv){

    // Initialize ROS2 communication
    rclcpp::init(argc, argv);

    // Object created into Shared pointer 
    // auto node = std::make_shared<rclcpp::Node>("cpp_test");

    // RCLCPP_INFO(node->get_logger(), "Hello CPP Node");

    auto node = std::make_shared<RobotNewsStationNode>();

    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}