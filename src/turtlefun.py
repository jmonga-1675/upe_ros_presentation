#!/usr/bin/env python3

import rospy
import tf
import math
import random
import sys
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class Turtle():
    def __init__(self, radius, speed):
        self.radius = radius
        self.speed = speed
        rospy.Subscriber('/turtle1/pose', Pose, self.set_vel)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pubb = rospy.Publisher('/turtwhale/cmd_vel', Twist, queue_size=10)

    def set_vel(self, turtle_pose):
        lin_vel = self.radius * self.speed
        turtle_vel = Twist()
        turtle_vel.linear.x = lin_vel
        rand = 2 * random.randint(0, 1) - 1
        rand2 = 2 * random.randint(0, 1) - 1
        turtle_vel.angular.z = rand * self.speed
        self.pub.publish(turtle_vel)
        turtle_vel.angular.z = rand2 * self.speed
        self.pubb.publish(turtle_vel)
        br = tf.TransformBroadcaster()
        br.sendTransform((turtle_pose.x, turtle_pose.y, 0),
                  tf.transformations.quaternion_from_euler(0, 0, turtle_pose.theta),
                  rospy.Time.now(),
                  'turtle1',
                  'world')




if __name__ == '__main__':
    rospy.init_node('turtle_fun', anonymous=True)
    radius = float(sys.argv[1])
    speed = float(sys.argv[2])
    turtle = Turtle(radius, speed)
    rospy.spin()
