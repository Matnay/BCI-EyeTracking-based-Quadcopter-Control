import pyautogui
import rospy
from std_msgs.msg import Int32,Float32
import time

publisher=rospy.Publisher("eye_tracking_data",Int32,queue_size=10)
rospy.init_node("eye_tracking")
while not rospy.is_shutdown():
	x,y = pyautogui.position()
	res = [x,y]
	print(res)
	
	publisher.publish(x)
	publisher.publish(y)
	time.sleep(1)
