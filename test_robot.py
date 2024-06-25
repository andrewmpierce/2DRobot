from robot import Robot

def test_robot_initialized_correctly():
    robot = Robot()
    assert robot.position == [0, 0]
    assert robot.orientation == 0

def test_robot_moves_and_changes_location():
    robot = Robot()
    robot.move()
    assert robot.position == [0,1]

def test_robot_turns_and_changes_orientation():
    robot = Robot()
    robot.turn_left()
    assert robot.orientation == 270
    robot.turn_right()
    assert robot.orientation == 0


