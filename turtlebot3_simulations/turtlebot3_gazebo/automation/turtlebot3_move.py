import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import time

class TurtleBotMover(Node):
    def __init__(self):
        super().__init__('turtlebot_mover')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.odom_subscriber = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.cmd = Twist()
        self.position = None
        self.orientation = None
        self.yaw = None
        self.initial_yaw = None

        # Wait for initial odometry data
        while self.yaw is None:
            self.get_logger().info("Waiting for odometry data...")
            rclpy.spin_once(self, timeout_sec=0.1)
        self.initial_yaw = self.yaw

    def odom_callback(self, msg):
        self.position = msg.pose.pose.position
        self.orientation = msg.pose.pose.orientation
        self.yaw = self.euler_from_quaternion(self.orientation)

    def euler_from_quaternion(self, orientation):
        x, y, z, w = orientation.x, orientation.y, orientation.z, orientation.w
        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        yaw = math.atan2(siny_cosp, cosy_cosp)
        return yaw

    def move_callback(self):
        pass

    def move_to_point(self, linear_speed, target_distance):
        time.sleep(0.5)
        initial_position = self.get_position()
        if initial_position is None:
            self.get_logger().info("No initial position data available.")
            return

        if( abs(self.cmd.angular.z) > 0 ):
            self.cmd.angular.z = 0.0
            self.publisher.publish(self.cmd)
            rclpy.spin_once(self, timeout_sec=0.1)

        initial_x, initial_y = initial_position[0], initial_position[1]

        self.cmd.linear.x = linear_speed
        self.cmd.angular.z = 0.0
        
        self.get_logger().info(f'Starting move from position: {initial_position} with target distance: {target_distance}')
        
        total_distance = 0.0
        
        while total_distance < target_distance:
            self.publisher.publish(self.cmd)
            rclpy.spin_once(self, timeout_sec=0.1)
            
            current_position = self.get_position()
            if current_position is None:
                continue
            
            current_x, current_y = current_position[0], current_position[1]
            total_distance = math.sqrt((current_x - initial_x) ** 2 + (current_y - initial_y) ** 2)
            self.get_logger().info(f'Current distance traveled: {total_distance:.2f} meters')
        
        self.stop()
        self.get_logger().info(f'Finished move. Final position: {self.get_position()}')

    def turn_to_angle(self, target_angle):
        time.sleep(0.5)
        target_angle_rad = math.radians(target_angle)
        
        target_yaw = self.normalize_angle(self.initial_yaw + target_angle_rad)
        
        self.cmd.linear.x = 0.0
        Kp = 0.5 
        Ki = 0.1 
        Kd = 0.2
        integral = 0.0
        previous_error = 0.0
        previous_time = self.get_clock().now().nanoseconds / 1e9
        
        self.get_logger().info(f'Starting turn. Initial yaw: {math.degrees(self.initial_yaw):.2f}, Target yaw: {math.degrees(target_yaw):.2f}')
        
        while not self.is_angle_reached(target_yaw):
            current_time = self.get_clock().now().nanoseconds / 1e9
            delta_time = current_time - previous_time
            previous_time = current_time

            angle_diff = self.normalize_angle(target_yaw - self.yaw)
            integral += angle_diff * delta_time
            derivative = (angle_diff - previous_error) / delta_time if delta_time > 0 else 0.0
            previous_error = angle_diff

            control_signal = Kp * angle_diff + Ki * integral + Kd * derivative
            
            if abs(angle_diff) < math.radians(10):
                control_signal *= 0.7
            if abs(angle_diff) < math.radians(5):
                control_signal *= 0.5
            if abs(angle_diff) < math.radians(1):
                control_signal *= 0.4
            if abs(angle_diff) < math.radians(0.5):
                control_signal *= 0.3
            
            self.cmd.angular.z = control_signal
            self.publisher.publish(self.cmd)
            rclpy.spin_once(self, timeout_sec=0.05)

        self.stop()
        self.get_logger().info(f'Finished turn. Current yaw: {math.degrees(self.yaw):.2f}')

    def is_angle_reached(self, target_yaw):
        if self.yaw is None:
            return False
        angle_diff = abs(self.normalize_angle(target_yaw - self.yaw))
        self.get_logger().info(f'Current yaw: {math.degrees(self.yaw):.2f}, Target yaw: {math.degrees(target_yaw):.2f}, Angle diff: {math.degrees(angle_diff):.2f}')
        return angle_diff < math.radians(0.2)  # Decreased tolerance to 0.2 degrees

    def normalize_angle(self, angle):
        while angle > math.pi:
            angle -= 2 * math.pi
        while angle < -math.pi:
            angle += 2 * math.pi
        return angle

    def stop(self):
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.publisher.publish(self.cmd)

    def get_position(self):
        if self.position is not None:
            return (self.position.x, self.position.y, self.position.z)
        else:
            return None

    def get_orientation(self):
        if self.orientation is not None:
            return (self.orientation.x, self.orientation.y, self.orientation.z, self.orientation.w)
        else:
            return None
        
    def print_pos(self):
        position = self.get_position()
        self.get_logger().info(f'Current Position: {position}')

    def print_orient(self):
        orientation = self.get_orientation()
        self.get_logger().info(f'Current Orientation: {orientation}')

    def print_pos_and_orient(self):
        self.print_pos()
        self.print_orient()