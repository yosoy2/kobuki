#!/usr/bin/env python

import rospy
from kobuki_msgs.msg import MotorPower
from kobuki_msgs.msg import BumperEvent
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class Kobuki_safe_controller:
    def __init__(self):
        self.publisher_motor=rospy.Publisher("/mobile_base/commands/motor_power", MotorPower, queue_size=0)
        self.publisher_wheels=rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size=0)
        self.subscriber_joy=rospy.Subscriber("/joy", Joy, self.joy_callback)
        self.Subscriber_bumper=rospy.Subscriber("/mobile_base/events/bumper", BumperEvent, self.bumper_callback)
        #self.bumper=BumperEvent()
        self.stop=0   #no hay choques, si fuese 1, se acticvaron los bumpers
        self.power=MotorPower()
        self.twist=Twist()

    def joy_callback(self,msg):
        velocity=msg.axes[1]*0.5
        angular=msg.axes[0]
        if self.stop==0:
            print("no he chocado")
            self.power.state=1
            self.twist.linear.x=velocity
            self.twist.angular.z=angular
            self.publisher_motor.publish(self.power)
            self.publisher_wheels.publish(self.twist)

        else:
            print("choque")
            self.power.state=1
            self.twist.linear.x=-0.5
            self.twist.angular.z=0
            self.publisher_motor.publish(self.power)
            self.publisher_wheels.publish(self.twist)
            if self.stop==0:
                print("no he chocado")
                self.twist.linear.x=velocity
                self.twist.angular.z=angular
                self.publisher_motor.publish(self.power)
                self.publisher_wheels.publish(self.twist)
            else:
                print("choque")
                self.twist.linear.x=velocity
                self.twist.angular.z=angular
                self.publisher_motor.publish(self.power)
                self.publisher_wheels.publish(self.twist)

        '''    self.publisher_motor.publish(self.power)
            self.publisher_wheels.publish(self.twist)
            self.power.state=0
            self.twist.linear.x=0
            self.twist.angular.z=0
            self.publisher_motor.publish(self.power)
            self.publisher_wheels.publish(self.twist)
            self.stop=1'''

    def bumper_callback(self, msg):
        if msg.state==1:
            self.stop=1

def main():
    rospy.init_node('Kobuki_safe_controller') #creacion y registro del nodo!

    obj = Kobuki_safe_controller() # Crea un objeto del tipo Template, cuya definicion se encuentra arriba


    #objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template


    #rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers
    rospy.spin()


if __name__ =='__main__':
    main()
