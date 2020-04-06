import pymouse
import rospy
from std_msgs.msg import Int32,String
import math
import numpy as np

def screensize():
    m=pymouse.PyMouse()
    size=m.screen_size()
    size=np.asarray(size)
    size[0]=size[0]*0.5
    size[1]=size[0]*0.5
    return size

def positiont():
    m=pymouse.PyMouse()
    pos=m.position()
    return pos
    

def distance():
    center=screensize()
    pos=positiont()
    max_dist=math.sqrt((0-center[0])**2  + (0-center[1])**2)
    dist=math.sqrt((pos[0]-center[0])**2  + (pos[1]-center[1])**2)
    dist=dist*100/max_dist
    return dist

def quadrant():
    center=screensize()
    pos=positiont()
    if(pos[0]>center[0] and pos[1]<center[1]):
        return ("Quadrant 1")
    if(pos[0]<center[0] and pos[1]<center[1]):
        return ("Quadrant 2")
    if(pos[0]<center[0] and pos[1]>center[1]):
        return ("Quadrant 3")
    if(pos[0]>center[0] and pos[1]>center[1]):
        return ("Quadrant 4")

def Quadrant_Distance():
    Dist=rospy.Publisher('Distance', Int32, queue_size=10)
    Quad=rospy.Publisher('Quadrant', String, queue_size=10)
    rospy.init_node('mPose',anonymous=True)
    rospy.Rate(10)
    while not rospy.is_shutdown():
        Dist.publish(distance())
        Quad.publish(quadrant())
        rospy.loginfo(distance())
        rospy.loginfo(quadrant())
    

if __name__ == '__main__':
    try:
        Quadrant_Distance()
    except rospy.ROSInterruptException:
        pass
