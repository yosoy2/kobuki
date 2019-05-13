#!/usr/bin/env python

import rospy
from kobuki_msgs.msg import *
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class Kobuki_controller:
    def __init__(self):
        self.publisher_motor=rospy.Publisher("/mobile_base/commands/motor_power", MotorPower, queue_size=0)
        self.subscriber_joy=rospy.Subscriber("/joy", Joy, self.callback)
        self.publisher_wheels=rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size=0)
        self.power=MotorPower()
        self.twist=Twist()

    def callback(self, msg):
        velocity=msg.axes[1]*0.5
        angular=msg.axes[0]
        if msg.buttons[0]==1:
            self.power.state=1
            self.twist.linear.x=velocity
            self.twist.angular.z=angular
            self.publisher_motor.publish(self.power)
            self.publisher_wheels.publish(self.twist)

        else:
            self.power.state=0
            self.twist.linear.x=0
            self.twist.angular.z=0
            self.publisher_motor.publish(self.power)
            self.publisher_wheels.publish(self.twist)

def main():
	rospy.init_node('Kobuki_controller') #creacion y registro del nodo!

	obj = Kobuki_controller() # Crea un objeto del tipo Template, cuya definicion se encuentra arriba


	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template


	#rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers
	rospy.spin()


if __name__ =='__main__':
	main()
