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
		self.error=0
		self.pose_st = PoseStamped()

	def act_cb(self,msg):
		self.action=msg.data

	def odom_cb(self,data):
		self.pose_st.header = data.header
		self.pose_st.pose = data.pose.pose

	def check(self):
		if(self.pose_st.pose.position.x<0.5):
			self.error=abs(self.pose_st.pose.position.y)
		elif(self.pose_st.pose.position.x>4.6 or self.pose_st.pose.position.x<5.4):
			self.error=abs(self.pose_st.pose.position.y)
		elif(self.pose_st.pose.position.y>4.6 or self.pose_st.pose.position.y<5.4):
			self.error=abs(self.pose_st.pose.position.x-5)
		elif(self.pose_st.pose.position.x<0.2 or self.pose_st.pose.position.x>-0.2):
			self.error=abs(self.pose_st.pose.position.y-5)
		elif(self.pose_st.pose.position.x>4.6 or self.pose_st.pose.position.x<5.4):
			self.error=abs(self.pose_st.pose.position.x)
		return self.error
		print(("Utility: {}").format(u))	

	def initialization(self):
		utility=1
		while not rospy.is_shutdown():
			time.sleep(10)
			print("Utility calculation started!")
			if(self.check()>0.01):
				utility=utility+(1/self.check())
			time.sleep(1)
			print(self.check())
		print(("Utility:{}").format(utility))
if __name__ == '__main__':
	rospy.init_node('error_node')
	rate=rospy.Rate(10)
	utility=Utility()
	utility.initialization()
