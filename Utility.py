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
		self.act_sub=rospy.Subscriber('action',Int32,self.act_cb)
		self.action=0
		self.time_initial=rospy.Time.now()
		self.error=1
		self.pose_st = PoseStamped()

	def act_cb(self,msg):
		self.action=msg.data

	def odom_cb(self,data):
		self.pose_st.header = data.header
		self.pose_st.pose = data.pose.pose

	def check(self):
		if(self.action==2):
			self.error=self.error+abs(self.pose_st.pose.position.y)
		if(self.action==3):
			self.error=self.error+abs(self.pose_st.pose.position.x-5)
		if(self.action==4):
			self.error=self.error+abs(self.pose_st.pose.position.y-5)
		if(self.action==5):	
			self.error=self.error+abs(self.pose_st.pose.position.x)
		u=(1/self.error)
		print(("Utility: {}").format(u))	

	def initialization(self):
		while not rospy.is_shutdown():
			self.check()

if __name__ == '__main__':
	rospy.init_node('error_node')
	rate=rospy.Rate(10)
	utility=Utility()	
	utility.initialization()
