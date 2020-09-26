#!/usr/bin/env python3

import rospy
import tf
import math
import random
import sys
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose



if __name__ == '__main__':
    rospy.init_node('turtle_fun', anonymous=True)
    radius = float(sys.argv[1])
    speed = float(sys.argv[2])
    rospy.spin()
