#!/usr/bin/env python
import rospy
import time
from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped,Pose
from std_msgs.msg import Int32
path = Path()
path_square=Path()
action=0
def odom_cb(data):
	global path
	global action
	path.header = data.header
	pose = PoseStamped()
	pose.header = data.header
	pose.pose = data.pose.pose
	path.poses.append(pose)
	path_pub.publish(path)
	
def action_cb(msg):
	global action
	action=msg.data

# use the terminal command example: rostopic pub /topic std_msgs/Int32 1
#change number according to each action

def square(iteration):
	global path_sq
	path_square.header.stamp =rospy.Time.now() 
	pose_sq = PoseStamped()
	path_square.header.frame_id="map"
	if(iteration>=5):
		pose_sq.pose.position.x=0
		pose_sq.pose.position.y=0
		pose_sq.pose.position.z=2
		action_pub.publish(1)

	if(iteration>=10):
		pose_sq.pose.position.x=5
		pose_sq.pose.position.y=0
		pose_sq.pose.position.z=2
		action_pub.publish(2)
		
	if(iteration>=15):
		pose_sq.pose.position.x=5
		pose_sq.pose.position.y=5
		pose_sq.pose.position.z=2
		action_pub.publish(3)

	if(iteration>=20):
		pose_sq.pose.position.x=0
		pose_sq.pose.position.y=5
		pose_sq.pose.position.z=2
		action_pub.publish(4)

	if(iteration>=30):
		pose_sq.pose.position.x=0
		pose_sq.pose.position.y=0
		pose_sq.pose.position.z=2
		action_pub.publish(5)
		
	path_square.poses.append(pose_sq)
	path_pub_sq.publish(path_square)

rospy.init_node('path_node')
rate=rospy.Rate(10)
odom_sub = rospy.Subscriber('mavros/local_position/odom', Odometry, odom_cb)
path_pub = rospy.Publisher('/path', Path, queue_size=10)
action_sub=rospy.Subscriber('topic',Int32,action_cb)
path_pub_sq=rospy.Publisher('/path_square', Path, queue_size=10)
action_pub=rospy.Publisher('action',Int32,queue_size=1)
if __name__ == '__main__':
	count=1
	error=0
	while not rospy.is_shutdown():
		count=count+1
		square(count)
		rate.sleep()

