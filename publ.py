#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from random import seed 
from random import randint
from future import time

def random_generate():
    return randint(1,2)

def Talker():
     g=rospy.Publisher('gain', Int32, queue_size=10)
     l=rospy.Publisher('land', Int32, queue_size=10)
     f=rospy.Publisher('forward', Int32, queue_size=10)
     b=rospy.Publisher('backward', Int32, queue_size=10)
     le=rospy.Publisher('left', Int32, queue_size=10)
     rg=rospy.Publisher('right', Int32, queue_size=10)
     rospy.init_node('Simulator', anonymous=True)
     rate=rospy.Rate(10)
     while not rospy.is_shutdown():
            no=random_generate()
            rospy.loginfo(no)
            g.publish(no)
            no=random_generate()
            rospy.loginfo(no)
            l.publish(no)
            rate.sleep()
            no=random_generate()
            rospy.loginfo(no)
            f.publish(no)
            no=random_generate()
            rospy.loginfo(no)
            b.publish(no)
            no=random_generate()
            rospy.loginfo(no)
            le.publish(no)
            no=random_generate()
            rospy.loginfo(no)
            rg.publish(no)
            rospy.loginfo("\n")
if __name__ == '__main__':
    try:
        Talker()
    except rospy.ROSInterruptException:
        pass
