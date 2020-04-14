#!/usr/bin/env python
import rospy
import time
from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped,Pose
from std_msgs.msg import Int32


class Utility:
	def __init__(self):
		self.odom_sub = rospy.Subscriber('mavros/local_position/odom', Odometry, self.odom_cb)
		self.act_sub=rospy.Subscriber("action",Int32,act_cb)
		self.action=0
		self.time_initial=rospy.Time.now()

	def act_cb(self,msg):
		self.action=msg.data

	def odom_cb(self,data):
		pose_st = PoseStamped()
		pose_st.header = data.header
		pose_st.pose = data.pose.pose
		if(self.action==2):
			error=error+abs(pose_st.pose.position.y)
		if(self.action==3):
			error=error+abs(pose_st.pose.position.x-5)
		if(self.action==4)
			error=error+abs(pose_st.pose.position.y-5)
		if(self.action==5)	
			error=error+abs(pose_st.pose.position.x)

		u=(1/error)/(rospy.Time.now()-self.time_initial)	
		print(("Utility: "{}).format(u))	

if __name__ == '__main__':
	rospy.init_node('error_node')
	rate=rospy.Rate(10)
	
	while not rospy.is_shutdown():
		utility=Utility()
		rate.sleep()


