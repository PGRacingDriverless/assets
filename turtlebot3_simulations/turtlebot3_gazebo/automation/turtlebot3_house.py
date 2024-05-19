import rclpy
import turtlebot3_move

def main(args=None):
    rclpy.init(args=args)
    print("-------- Start --------")
    turtlebot_mover = turtlebot3_move.TurtleBotMover()

    try:
        turtlebot_mover.turn_to_angle(350)
        turtlebot_mover.move_to_point(0.2, 3.2)
        turtlebot_mover.turn_to_angle(90)
        turtlebot_mover.move_to_point(0.2, 1.4)

        # right side of house
        turtlebot_mover.turn_to_angle(0)
        turtlebot_mover.move_to_point(0.2, 5.0)
        turtlebot_mover.turn_to_angle(270)
        turtlebot_mover.move_to_point(0.2, 1.5)
        turtlebot_mover.turn_to_angle(90)
        turtlebot_mover.move_to_point(0.2, 5.5)
        turtlebot_mover.turn_to_angle(180)
        turtlebot_mover.move_to_point(0.2, 3.4)
        turtlebot_mover.turn_to_angle(270)
        turtlebot_mover.move_to_point(0.2, 3.8)

        turtlebot_mover.turn_to_angle(180)
        turtlebot_mover.move_to_point(0.2, 4.0)
        
        # left side of house
        turtlebot_mover.turn_to_angle(90)
        turtlebot_mover.move_to_point(0.2, 3.2)
        turtlebot_mover.turn_to_angle(180)
        turtlebot_mover.move_to_point(0.2, 5.2)
        turtlebot_mover.turn_to_angle(-90)
        turtlebot_mover.move_to_point(0.2, 3.5)
        turtlebot_mover.turn_to_angle(90)
        turtlebot_mover.move_to_point(0.2, 3.5)
        turtlebot_mover.turn_to_angle(0)
        turtlebot_mover.move_to_point(0.2, 2.5)
        turtlebot_mover.turn_to_angle(270)
        turtlebot_mover.move_to_point(0.2, 3.2)
        turtlebot_mover.turn_to_angle(0)
        turtlebot_mover.move_to_point(0.2, 5.0)
        turtlebot_mover.turn_to_angle(270)

    except KeyboardInterrupt:
        pass

    turtlebot_mover.stop()
    print("-------- End --------")
    turtlebot_mover.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
