import rospy
import time
from mavros_msgs.msg import State,PositionTarget
from mavros_msgs.srv import CommandBool, SetMode
from geometry_msgs.msg import Pose, PoseStamped, Point, Quaternion
import math
import numpy
from geometry_msgs.msg import Twist, TwistStamped
from nav_msgs.msg import Odometry
from std_msgs.msg import Header, String , Int32,Int8
from threading import Thread
from rospy.numpy_msg import numpy_msg
import autogui

def start():
	rate=rospy.Rate(10)
	takeoff()
	while not rospy.is_shutdown():
		result = arming_srv(value=True)
		print result
		result = mode_srv(custom_mode="OFFBOARD")
		print result
		pos=set_position()
	    #pos.header.frame_id = 'base_link'
	    #pos.header.stamp = rospy.Time.now()
		vel_pub.publish(pos)
		rate.sleep()


 
def takeoff():
	local_pos_pub = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped, queue_size=10)
	pose = PoseStamped()
	pose.header.stamp = rospy.Time.now()
	pose.pose.position.x = 0
	pose.pose.position.y = 0
	pose.pose.position.z = 4
	for i in range(100):
		local_pos_pub.publish(pose)
		rate.sleep()

def gaze_callback_y(msg_y):
	global yc
	yc=int(msg_y.data)
	print(yc)
	return yc

def gaze_callback_x(msg_x):
	global xc
	xc=int(msg_x.data)
	print(xc)
	return xc		

def set_position():
	x,y = pyautogui.position()
	pos=TwistStamped()
	pos.header = Header()
	print("xc is " + str(xc))
	if(xc<680 and yc<380):
		pos.twist.linear.z=0.0
		pos.twist.linear.x=-12
		pos.twist.linear.y=-12
		print("inside conditoion1")
	elif(xc<680 and yc>380):
		pos.twist.linear.z=0.0
		pos.twist.linear.x=-12
		pos.twist.linear.y=12
		print("forward_right")

	elif(xc>680 and yc<380):
		pos.twist.linear.z=0.0
		pos.twist.linear.x=12
		pos.twist.linear.y=12
		print("backward_left")

	elif(xc>680 and yc>380):
		pos.twist.linear.z=0.0
		pos.twist.linear.x=12
		pos.twist.linear.y=-12
		print("backward_right")

	else: 
		pos.twist.linear.z=0
		pos.twist.linear.x=0
		pos.twist.linear.y=0
		print("entered default")
	return pos

if __name__ == '__main__':
	rospy.init_node('gaze_control', anonymous=True)
	rate=rospy.Rate(10)
	vel_pub = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel', TwistStamped,queue_size=10)
	gaze_sub_x = rospy.Subscriber("eye_tracking_data_x",Int32,gaze_callback_x)
	gaze_sub_y = rospy.Subscriber("eye_tracking_data_y",Int32,gaze_callback_y)
	arming_srv = rospy.ServiceProxy("/mavros/cmd/arming", CommandBool)
	mode_srv = rospy.ServiceProxy("/mavros/set_mode", SetMode)
	start()
