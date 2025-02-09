cmake_minimum_required(VERSION 3.8)
project(my_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(my_robot_interfaces REQUIRED)

add_executable(cpp_node src/my_first_node.cpp)
ament_target_dependencies(cpp_node rclcpp)

add_executable(robot_news src/robot_news_station.cpp)
ament_target_dependencies(robot_news rclcpp example_interfaces)

add_executable(smartphone src/smartphone.cpp)
ament_target_dependencies(smartphone rclcpp example_interfaces)

add_executable(hardware_status_publisher src/hw_status_publisher.cpp)
ament_target_dependencies(hardware_status_publisher rclcpp my_robot_interfaces)

add_executable(hardware_status_subscriber src/hw_status_subscriber.cpp)
ament_target_dependencies(hardware_status_subscriber rclcpp my_robot_interfaces)

install(TARGETS
  cpp_node
  robot_news
  smartphone
  hardware_status_publisher
  hardware_status_subscriber
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
