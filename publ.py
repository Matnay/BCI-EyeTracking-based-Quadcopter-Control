#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from random import seed 
from random import randint

def random_generate():
    return randint(1,100)

def Talker():
     pub=rospy.Publisher('chatter', Int32, queue_size=10)
     rospy.init_node('talker', anonymous=True)
     rate=rospy.Rate(10)
     while not rospy.is_shutdown():
            no=random_generate()
            rospy.loginfo(no)
            pub.publish(no)
            rate.sleep()
if __name__ == '__main__':
    try:
        Talker()
    except rospy.ROSInterruptException:
        pass