#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from random import seed 
from random import randint
import time
    #g=rospy.Publisher('gain', Int32, queue_size=10)
    #l=rospy.Publisher('land', Int32, queue_size=10)
f=rospy.Publisher('forward', Int32, queue_size=10)
b=rospy.Publisher('backward', Int32, queue_size=10)
l=rospy.Publisher('left', Int32, queue_size=10)
r=rospy.Publisher('right', Int32, queue_size=10)
n=rospy.Publisher('neutral', Int32, queue_size=10)
rospy.init_node('Simulator', anonymous=True)
rate=rospy.Rate(1  )
while not rospy.is_shutdown():
            start = time.time()
            while time.time() < start + 10:
                f.publish(80)
                l.publish(0)
                r.publish(0)
                b.publish(0)
                n.publish(0)
                rospy.loginfo("Forward")    
            start = time.time()
            while time.time() < start + 10:
                f.publish(0)
                l.publish(80)
                r.publish(0)
                b.publish(0)
                n.publish(0)
                rospy.loginfo("Left")    
            start = time.time()
            while time.time() < start +10:
                f.publish(0)
                l.publish(0)
                r.publish(0)
                b.publish(80)
                n.publish(0)    
                rospy.loginfo("Backwards")
            start = time.time()
            while time.time() < start + 10:
                f.publish(0)
                l.publish(80)
                r.publish(80)
                b.publish(0)
                n.publish(0)
                rospy.loginfo("Right")    
            start = time.time()
            while time.time() < start + 10:
                f.publish(0)
                l.publish(80)
                r.publish(80)
                b.publish(0)
                n.publish(0)    
                rospy.loginfo("Land")
if __name__ == '__main__':
    try:
        Talker()
    except rospy.ROSInterruptException:
        pass
