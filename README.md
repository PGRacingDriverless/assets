Robot Repo
=============================

Based on TurtleBot3 with added Intel RealSense depth camera.

# How to run
Don't forget about the
```source /opt/ros/humble/setup.bash```
command and
```source install/setup.bash```
command after the build.

Export the waffle model with RealSense camera:
```
export TURTLEBOT3_MODEL=waffle_realsense
```

Launching the world in gazebo:  
```
__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```
or
```
__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py
```

Keyboard control:  
```
ros2 run turtlebot3_teleop teleop_keyboard
```