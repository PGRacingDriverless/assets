import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import turtlebot3_move

def main(args=None):
    rclpy.init(args=args)
    turtlebot_mover = turtlebot3_move.TurtleBotMover()

    try:
        turtlebot_mover.turn(0.2, -60)
        time.sleep(0.5)
        turtlebot_mover.move_to_point(0.2, 0.0, 7.0)
        time.sleep(0.5)
        turtlebot_mover.turn(0.2, 60)
        time.sleep(0.5)
        turtlebot_mover.move_to_point(0.2, 0.0, 14.5)
        time.sleep(0.5)
        turtlebot_mover.turn(0.2, 90)
        time.sleep(0.5)
        turtlebot_mover.move_to_point(0.2, 0.0, 16.5)
        time.sleep(0.5)
        turtlebot_mover.turn(0.2, 90)
        time.sleep(0.5)
        turtlebot_mover.move_to_point(0.2, 0.0, 14.5)
        time.sleep(0.5)
        turtlebot_mover.turn(0.2, 60)
        time.sleep(0.5)
        turtlebot_mover.move_to_point(0.2, 0.0, 6.5)
        time.sleep(0.5)
        turtlebot_mover.turn(0.2, 120)
        time.sleep(0.5)
        turtlebot_mover.move_to_point(0.2, 0.0, 16.0)
    except KeyboardInterrupt:
        pass

    turtlebot_mover.stop()
    turtlebot_mover.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
