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
		error=0
		self.pose_st = PoseStamped()

	def act_cb(self,msg):
		self.action=msg.data

	def odom_cb(self,data):
		self.pose_st.header = data.header
		self.pose_st.pose = data.pose.pose

	def check(self,error):
		if(self.pose_st.pose.position.x<0.5):
			error=abs(self.pose_st.pose.position.y)
		elif(self.pose_st.pose.position.x>4.6 or self.pose_st.pose.position.x<5.4):
			error=abs(self.pose_st.pose.position.y)
		elif(self.pose_st.pose.position.y>4.6 or self.pose_st.pose.position.y<5.4):
			error=abs(self.pose_st.pose.position.x-5)
		elif(self.pose_st.pose.position.x<0.2 or self.pose_st.pose.position.x>-0.2):
			error=abs(self.pose_st.pose.position.y-5)
		elif(self.pose_st.pose.position.x>4.6 or self.pose_st.pose.position.x<5.4):
			error=abs(self.pose_st.pose.position.x)
		#u=(1/error)
		return error
		#print(("Utility: {}").format(u))	

	def initialization(self):
		error=1
		while not rospy.is_shutdown():
			error=error+self.check(error)
			time.sleep(1)
			print(error)
		print(("Utility:{}").format(1/error))
if __name__ == '__main__':
	rospy.init_node('error_node')
	rate=rospy.Rate(10)
	utility=Utility()
	utility.initialization()
