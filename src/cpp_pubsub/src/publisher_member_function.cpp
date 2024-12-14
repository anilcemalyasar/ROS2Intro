#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include <chrono>
#include <functional>
#include <memory>
#include <string>

using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
* member function as a callback from the timer. */

class MinimalPublisher : public rclcpp::Node
{
    public:
        MinimalPublisher():  Node("minimal_publisher"), counter_(0)
        {
            publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
            timer_ = this->create_wall_timer(std::chrono::seconds(1),
                                              std::bind(&MinimalPublisher::timer_callback, this));
        };

    private:

        void timer_callback()
        {
            auto message = std_msgs::msg::String();
            message.data = "Hello, world! " + std::to_string(counter_++);
            RCLCPP_INFO(this->get_logger(), "Publishing %s", message.data.c_str());
        }

        rclcpp::TimerBase::SharedPtr timer_;
        rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
        int counter_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<MinimalPublisher>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}