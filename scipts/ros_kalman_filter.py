import rospy
from std_msgs.msg import Int32,Float32,String
from math import *
import numpy as np
import time
class Kalman:
	def __init__(self):
		self.action_1=0
		self.iterations=1
		self.mean=0
		self.num_sum=0
		self.prev_mean=0
		self.DIFF_THRESHOLD=10
		self.data_sub=rospy.Subscriber("chatter",Int32,self.data_cb)
		self.final_pub=rospy.Publisher("action",Float32,queue_size=1)

	def gaussian(self,mu,sigma_sq,input_x):
		coeff=1.0/sqrt(2*pi*sigma_sq)
		expo=exp(-0.5*(x-mu)**2/sigma_sq)
		return coeff* expo

	def update(self,mean_1,var_1,mean_2,var_2):
		new_mean=(var_2*mean_1+var_1*mean_2)/(var_1+var_2)
		new_var=1/(1/var_1 + 1/var_2)
		return [new_mean,new_var]

	def predict(self,mean_1,var_1,mean_2,var_2):
		new_mean=mean_1+mean_2
		new_var=var_1+var_2
		return [new_mean,new_var]

	def mean_val(self,value):
		global iterations
		self.iterations=self.iterations+1
		self.num_sum=self.num_sum+value
		self.mean=self.num_sum/self.iterations
		if abs(self.prev_mean-self.mean)>self.DIFF_THRESHOLD:
			#reset iterations if difference between the last mean and new mean is above a certain threshold
			#the new mean is initialized with a latest reading to prevent mean 0 which will bias reading
			#the prev_mean is given the value of mean and num_sum is reinitialized
			print("iteration_reset! prev_mean:{} mean:{}").format(self.prev_mean,self.mean)
			self.iterations=1
			self.prev_mean=self.mean
			self.num_sum=0
			self.mean=value
		return self.mean

	def data_cb(self,msg):
			global action_1
			self.action_1=msg.data
			return self.action_1

	def initialisation(self):
		rospy.init_node("kalman")
		rate=rospy.Rate(2)
		measurement_sig = 0.1
		motion_sig = 2
		mu = 1
		sig = 10.
		while not rospy.is_shutdown():
			mu, sig = kalman.update(mu, sig, self.mean_val(self.action_1), measurement_sig)
			print('Update: [{}, {}]'.format(mu, sig))
			mu, sig = kalman.predict(mu, sig, self.action_1, motion_sig)
			print('Predict: [{}, {}]'.format(mu, sig))
			time.sleep(0.5)
			self.final_pub.publish(mu)
		print('\n')
		print('Final result: [{}, {}]'.format(mu, sig))

if __name__ == '__main__':
	kalman=Kalman()
	kalman.initialisation()
