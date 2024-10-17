from cpa_robot import position_x, position_y, orientation, drive, plot_path, reset_robot, plot_robot, sensor_left, sensor_middle, sensor_right, animate_path
import random
reset_robot()

# edit this comment - challenge is to have the robot move like a roomba. Any time it hits the circle it should turn by a random angle and carry on moving. Any time it hits a wall it should turn 180 degrees.???
import random
from math import pi
def rotate(angle):
    dist = 2.5*angle
    drive(dist,-dist)

def random_rotate():
    random_angle = random.random()*pi*2
    rotate(random_angle)

def touching_circle():
    if sensor_middle() or sensor_left() or sensor_right():
        return True
    else:
        return False

def touching_wall():
    if position_x() < -50 or position_x() > 150 or position_y() < -50 or position_y() > 150:
        return True
    else:
        return False
    

reset_robot()
#Drive forwards until reaches circle or boundary, then turn by random angle
for i in range(100):
    random_rotate()
    while not touching_circle() and not touching_wall():
        drive(1,1)

    drive(-3,-3)
plot_path()