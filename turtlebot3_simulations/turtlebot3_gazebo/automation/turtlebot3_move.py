import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class TurtleBotMover(Node):
    def __init__(self):
        super().__init__('turtlebot_mover')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move_callback)
        self.cmd = Twist()

    def move_callback(self):
        pass

    def move_to_point(self, linear_speed, angular_speed, duration):
        self.cmd.linear.x = linear_speed
        self.cmd.angular.z = angular_speed
        start_time = self.get_clock().now()
        duration = rclpy.duration.Duration(seconds=duration)
        while (self.get_clock().now() - start_time) < duration:
            self.publisher.publish(self.cmd)
            rclpy.spin_once(self, timeout_sec=0.1)
        self.stop()

    def turn(self, angular_speed, angle):
        duration = abs(math.radians(angle) / angular_speed)
        self.move_to_point(0.0, math.copysign(angular_speed, angle), duration)

    def stop(self):
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.publisher.publish(self.cmd)
