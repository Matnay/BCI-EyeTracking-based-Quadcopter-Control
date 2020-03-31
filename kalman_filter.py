import rospy
from std_msgs.msg import Int32,Float32,String
from math import *
import numpy as np
class Kalman:
	def __init__(self):
		self.action_1=0
		self.data_sub=rospy.Subscriber("chatter",Int32,self.data_cb)

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

	def data_cb(self,msg):
			global action_1
			self.action_1=msg.data
			print self.action_1
			return self.action_1

	def initialisation(self):
		rospy.init_node("kalman")
		measurement_sig = 4
		motion_sig = 2
		mu = 1
		sig = 10000.
		while not rospy.is_shutdown():
			mu, sig = kalman.update(mu, sig, self.action_1, measurement_sig)
	    	print('Update: [{}, {}]'.format(mu, sig))
	    	mu, sig = kalman.predict(mu, sig, 1, motion_sig)
	    	print('Predict: [{}, {}]'.format(mu, sig))

		print('\n')
		print('Final result: [{}, {}]'.format(mu, sig))

if __name__ == '__main__':
	kalman=Kalman()
	kalman.initialisation()
'''
measurements = [0,1,2,3,4,5,6,7,8,10]
motions = [1,1,1,1,1,1,1,1,1,2]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

for n in range(len(measurements)):    
    mu, sig = update(mu, sig, measurements[n], measurement_sig)
    print('Update: [{}, {}]'.format(mu, sig))
    mu, sig = predict(mu, sig, motions[n], motion_sig)
    print('Predict: [{}, {}]'.format(mu, sig))
print('\n')
print('Final result: [{}, {}]'.format(mu, sig))
'''
