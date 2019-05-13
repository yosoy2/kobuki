#!/usr/bin/env python

import rospy
from kobuki_std_msg.msgs import * #no me acuerdo cual wea era
from std_msgs.msg import twist
from sensor_msgs.msg import Joy

class Kobuki_controller:
    def __init__(self):
        self.subscriber_motor=rospy.Subscriber("/mobile_base/commands/motor_power", #nombre del mensaje q, queue_size = 0)
        self.subscriber_joy=rospy.Subscriber("kobuki_joy",Joy, self.callback)
        self.publisher_wheels=rospy.Publisher()

    def callback(self,args):
