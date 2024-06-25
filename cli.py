from robot import Robot

MOVE = 'm'
LEFT = 'l'
RIGHT = 'r'
EXIT = 'e'
NEW_ROBOT = 'new'
SWITCH = 's'

def cli():
    exited = False
    # set up robot
    initial_robot = Robot()
    all_robots = [initial_robot]
    current_index = 0
    print("Hello, welcome to our CLI")
    print("Our robot moves around a 2D plane and only knows 4 commands")
    print("'m' to move one space")
    print("'l' to turn left")
    print("'r to turn right")
    print("'e' to exit")

    while exited == False:
        robot = all_robots[current_index]
        print("Robot Position: % s Robot Orientation: % s Robot ID: % s" % (robot.position, robot.orientation, current_index))
        user_input = input("Enter Prompt:")
        if user_input == MOVE:
            robot.move()
        if user_input == LEFT:
            robot.turn_left()
        if user_input == RIGHT:
            robot.turn_right()
        if user_input == NEW_ROBOT:
            new_robot = Robot()
            all_robots.append(new_robot)
            current_index += 1
        if user_input == SWITCH:
            if (len(all_robots) - 1) <= current_index:
                current_index = 0
            else:
                current_index +=1
        if user_input == EXIT:
            print("Goodbye")
            exited = True

cli()