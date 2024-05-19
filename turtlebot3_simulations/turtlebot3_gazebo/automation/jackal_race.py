import rclpy
import turtlebot3_move

def main(args=None):
    rclpy.init(args=args)
    print("-------- Start --------")
    turtlebot_mover = turtlebot3_move.TurtleBotMover()

    try:
        turtlebot_mover.turn_to_angle(0)
        turtlebot_mover.move_to_point(0.2, 1.0)
        turtlebot_mover.turn_to_angle(45)
        turtlebot_mover.move_to_point(0.1, 1.0)
        turtlebot_mover.move_to_point(0.4, 9.0)
        turtlebot_mover.turn_to_angle(0)
        turtlebot_mover.turn_to_angle(90)
        turtlebot_mover.move_to_point(0.2, 1.4)
        turtlebot_mover.turn_to_angle(180)
        turtlebot_mover.move_to_point(0.2, 10.0)
        turtlebot_mover.turn_to_angle(240)
        turtlebot_mover.move_to_point(0.2, 7.0)
        turtlebot_mover.turn_to_angle(270)
        turtlebot_mover.move_to_point(0.2, 7.0)
        turtlebot_mover.turn_to_angle(0)
        turtlebot_mover.move_to_point(0.2, 8.0)
    except KeyboardInterrupt:
        pass

    turtlebot_mover.stop()
    print("-------- End --------")
    turtlebot_mover.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()