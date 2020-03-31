import rospy
from std_msgs.msg import Int32,Float32,String
from math import *
import numpy as np

def gaussian(mu,sigma_sq,input_x):
	coeff=1.0/sqrt(2*pi*sigma_sq)
	expo=exp(-0.5*(x-mu)**2/sigma_sq)
	return coeff* expo

def update(mean_1,var_1,mean_2,var_2):
	new_mean=(var_2*mean_1+var_1*mean_2)/(var_1+var_2)
	new_var=1/(1/var_1 + 1/var_2)
	return [new_mean,new_var]

def predict(mean_1,var_1,mean_2,var_2):
	new_mean=mean_1+mean_2
	new_var=var_1+var_2
	return [new_mean,new_var]
def data_cb(msg):
		global action_1
		action_1=msg.data
		print action_1
		return action_1

if __name__ == '__main__':
	#rospy.init_node("kalman")
	#data_sub=rospy.Subscriber("data",String,data_cb)
	measurements = [1,2,3,4,5,6,7,8,9,11]
	motions = [1,1,1,1,1,1,1,1,1,2]

	measurement_sig = 4
	motion_sig = 2
	mu = 1
	sig = 10000.
	for n in range(len(measurements)):

	    mu, sig = update(mu, sig, measurements[n], measurement_sig)
	    print('Update: [{}, {}]'.format(mu, sig))
	   
	    mu, sig = predict(mu, sig, motions[n], motion_sig)
	    print('Predict: [{}, {}]'.format(mu, sig))
print('\n')
print('Final result: [{}, {}]'.format(mu, sig))