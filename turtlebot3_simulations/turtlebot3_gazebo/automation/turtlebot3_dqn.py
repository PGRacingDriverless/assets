import rclpy
import turtlebot3_move

def main(args=None):
    rclpy.init(args=args)
    print("-------- Start --------")
    turtlebot_mover = turtlebot3_move.TurtleBotMover()

    try:
        turtlebot_mover.turn_to_angle(320)
        turtlebot_mover.move_to_point(0.2, 1.0)
        turtlebot_mover.turn_to_angle(0)
        turtlebot_mover.move_to_point(0.2, 1.0)
        turtlebot_mover.turn_to_angle(335)
        turtlebot_mover.move_to_point(0.2, 1.8)
        turtlebot_mover.turn_to_angle(90)
        turtlebot_mover.move_to_point(0.2, 2.0)
        turtlebot_mover.turn_to_angle(180)
        turtlebot_mover.move_to_point(0.2, 0.8)
        turtlebot_mover.turn_to_angle(90)
        turtlebot_mover.move_to_point(0.2, 1.9)
        turtlebot_mover.turn_to_angle(180)
        turtlebot_mover.move_to_point(0.2, 2.6)
        turtlebot_mover.turn_to_angle(270)
        turtlebot_mover.move_to_point(0.2, 2.5)
        turtlebot_mover.turn_to_angle(0)
    except KeyboardInterrupt:
        pass

    turtlebot_mover.stop()
    print("-------- End --------")
    turtlebot_mover.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()