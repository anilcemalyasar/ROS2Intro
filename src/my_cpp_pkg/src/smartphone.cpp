#include <stdio.h>
#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

// Creating C++ Node with OOP
class SmartphoneNode: public rclcpp::Node
{
    public:
        SmartphoneNode(): Node("smartphone")
        {
            subscriber_ = this->create_subscription<example_interfaces::msg::String>(
                "robot_news", 10,
                std::bind(&SmartphoneNode::callbackRobotNews, this, std::placeholders::_1)
            );
            RCLCPP_INFO(this->get_logger(), "Smartphone has been started!");
        };
    
    private:

        void callbackRobotNews(const example_interfaces::msg::String::SharedPtr msg)
        {
            RCLCPP_INFO(this->get_logger(), "%s", msg->data.c_str());
        }

        rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_;

};

int main(int argc, char **argv){

    // Initialize ROS2 communication
    rclcpp::init(argc, argv);

    // Object created into Shared pointer 
    // auto node = std::make_shared<rclcpp::Node>("cpp_test");

    // RCLCPP_INFO(node->get_logger(), "Hello CPP Node");

    auto node = std::make_shared<SmartphoneNode>();

    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}