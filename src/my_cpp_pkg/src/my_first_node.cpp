#include <stdio.h>
#include "rclcpp/rclcpp.hpp"

// Creating C++ Node with OOP
class MyNode: public rclcpp::Node
{
    public:
        MyNode(): Node("cpp_test"), counter_(0)
        {
            RCLCPP_INFO(this->get_logger(), "Hello Cpp Node");
        
            timer_ = this->create_wall_timer(std::chrono::seconds(1),
                                             std::bind(&MyNode::timerCallBack, this));
        };
    
    private:

        void timerCallBack()
        {
            counter_++;
            RCLCPP_INFO(this->get_logger(), "Hello %d", counter_);
        }

        rclcpp::TimerBase::SharedPtr timer_;
        int counter_;
};

int main(int argc, char **argv){

    // Initialize ROS2 communication
    rclcpp::init(argc, argv);

    // Object created into Shared pointer 
    // auto node = std::make_shared<rclcpp::Node>("cpp_test");

    // RCLCPP_INFO(node->get_logger(), "Hello CPP Node");

    auto node = std::make_shared<MyNode>();

    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}