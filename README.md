Robot Repo
=============================

Based on TurtleBot3 with added Intel RealSense depth camera.


```source /opt/ros/humble/setup.bash```

~~export TURTLEBOT3_MODEL=waffle~~ ~~Waffle by default and only waffle is available~~ ```export TURTLEBOT3_MODEL=waffle_realsense```

Launching the world in gazebo:  
```__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py```

Keyboard control:  
```ros2 run turtlebot3_teleop teleop_keyboard```