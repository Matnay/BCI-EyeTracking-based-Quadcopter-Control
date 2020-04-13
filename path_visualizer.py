#!/usr/bin/env python
import rospy
import time
from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped,Pose

path = Path()
path_square=Path()
def odom_cb(data):
	global path
	path.header = data.header
	pose = PoseStamped()
	pose.header = data.header
	pose.pose = data.pose.pose
	path.poses.append(pose)
	path_pub.publish(path)


def square(iteration):
	global path_sq
	path_square.header.stamp =rospy.Time.now() 
	pose_sq = PoseStamped()
	path_square.header.frame_id="map"
	if(iteration<=100):
		pose_sq.pose.position.x=pose_sq.pose.position.x+1
		pose_sq.pose.position.y=pose_sq.pose.position.y
		pose_sq.pose.position.z=2
	if(iteration>=100 and iteration<200):
		pose_sq.pose.position.x=pose_sq.pose.position.x
		pose_sq.pose.position.y=pose_sq.pose.position.y+1
		pose_sq.pose.position.z=2
	if(iteration>=200 and iteration<300):
		pose_sq.pose.position.x=pose_sq.pose.position.x-1
		pose_sq.pose.position.y=pose_sq.pose.position.y
		pose_sq.pose.position.z=2
	if(iteration>=300 and iteration<400):
		pose_sq.pose.position.x=pose_sq.pose.position.x
		pose_sq.pose.position.y=pose_sq.pose.position.y-1
		pose_sq.pose.position.z=2
	path_square.poses.append(pose_sq)
	path_pub_sq.publish(path_square)

rospy.init_node('path_node')
rate=rospy.Rate(10)
odom_sub = rospy.Subscriber('mavros/local_position/odom', Odometry, odom_cb)
path_pub = rospy.Publisher('/path', Path, queue_size=10)
path_pub_sq=rospy.Publisher('/path_square', Path, queue_size=10)
if __name__ == '__main__':
	count=1
	while not rospy.is_shutdown():
		count=count+1
		square(count)
		rate.sleep()


