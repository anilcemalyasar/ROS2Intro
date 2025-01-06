#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class TemplateNode: public rclcpp::Node
{
    public:
        TemplateNode(): Node("robot_news_station"),
        {

        };
    
    private:

};

int main(int argc, char **argv){

    rclcpp::init(argc, argv);

    auto node = std::make_shared<RobotNewsStationNode>();

    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}