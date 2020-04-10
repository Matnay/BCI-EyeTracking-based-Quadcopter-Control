import rospy
from std_msgs.msg import Int32,Float32,String
from math import *
import numpy as np
from numpy.linalg import inv
import time
import statistics
class Least_Square_Estimation_f:
    def __init__(self):
        self.action_1=0
        self.data_sub=rospy.Subscriber("forward",Int32,self.data_cb)
        self.final_pub=rospy.Publisher("action_f",Float32,queue_size=1)
        self.y=[0.,0.,0.,0.,0.,0.,0.,0.,0.]

    def data_cb(self,msg):
            self.prev_action=self.action_1
            self.action_1=msg.data
            return self.action_1
    
    def data_cb(self,msg):
            self.prev_action=self.action_1
            self.action_1=msg.data
            return self.action_1
    
    def construct_y(self,val):
        self.y.append(val)
        print(self.y)
        if (len(self.y)>=10):
            self.y.pop(0)
        self.y_constructed=np.mat([self.y]).T

    def initialisation(self):
        rospy.init_node("lse")
        rate=rospy.Rate(2)
        H=np.mat([1,1,1,1,1,1,1,1,1]).T
        while not rospy.is_shutdown():
            self.construct_y(self.action_1)
            true_value=inv(H.T.dot(H)).dot(H.T.dot(self.y_constructed))  
            print('\n')
            ans=true_value.tolist()
            print('Final LSE estimated value: [{}]'.format(ans[0][0]))
            self.final_pub.publish(ans[0][0])
            rate.sleep()

class Least_Square_Estimation_b:
    def __init__(self):
        self.action_1=0
        self.data_sub=rospy.Subscriber("backward",Int32,self.data_cb)
        self.final_pub=rospy.Publisher("action_b",Float32,queue_size=1)
        self.y=[0.,0.,0.,0.,0.,0.,0.,0.,0.]

    def data_cb(self,msg):
            self.prev_action=self.action_1
            self.action_1=msg.data
            return self.action_1
    
    def data_cb(self,msg):
            self.prev_action=self.action_1
            self.action_1=msg.data
            return self.action_1
    
    def construct_y(self,val):
        self.y.append(val)
        print(self.y)
        if (len(self.y)>=10):
            self.y.pop(0)
        self.y_constructed=np.mat([self.y]).T

    def initialisation(self):
        rospy.init_node("lse")
        rate=rospy.Rate(2)
        H=np.mat([1,1,1,1,1,1,1,1,1]).T
        while not rospy.is_shutdown():
            self.construct_y(self.action_1)
            true_value=inv(H.T.dot(H)).dot(H.T.dot(self.y_constructed))  
            print('\n')
            ans=true_value.tolist()
            print('Final LSE estimated value: [{}]'.format(ans[0][0]))
            self.final_pub.publish(ans[0][0])
            rate.sleep()

class Least_Square_Estimation_r:
    def __init__(self):
        self.action_1=0
        self.data_sub=rospy.Subscriber("right",Int32,self.data_cb)
        self.final_pub=rospy.Publisher("action_r",Float32,queue_size=1)
        self.y=[0.,0.,0.,0.,0.,0.,0.,0.,0.]

    def data_cb(self,msg):
            self.prev_action=self.action_1
            self.action_1=msg.data
            return self.action_1
    
    def data_cb(self,msg):
            self.prev_action=self.action_1
            self.action_1=msg.data
            return self.action_1
    
    def construct_y(self,val):
        self.y.append(val)
        print(self.y)
        if (len(self.y)>=10):
            self.y.pop(0)
        self.y_constructed=np.mat([self.y]).T

    def initialisation(self):
        rospy.init_node("lse")
        rate=rospy.Rate(2)
        H=np.mat([1,1,1,1,1,1,1,1,1]).T
        while not rospy.is_shutdown():
            self.construct_y(self.action_1)
            true_value=inv(H.T.dot(H)).dot(H.T.dot(self.y_constructed))  
            print('\n')
            ans=true_value.tolist()
            print('Final LSE estimated value: [{}]'.format(ans[0][0]))
            self.final_pub.publish(ans[0][0])
            rate.sleep()

class Least_Square_Estimation_l:
    def __init__(self):
        self.action_1=0
        self.data_sub=rospy.Subscriber("left",Int32,self.data_cb)
        self.final_pub=rospy.Publisher("action_l",Float32,queue_size=1)
        self.y=[0.,0.,0.,0.,0.,0.,0.,0.,0.]

    def data_cb(self,msg):
            self.prev_action=self.action_1
            self.action_1=msg.data
            return self.action_1
    
    def data_cb(self,msg):
            self.prev_action=self.action_1
            self.action_1=msg.data
            return self.action_1
    
    def construct_y(self,val):
        self.y.append(val)
        print(self.y)
        if (len(self.y)>=10):
            self.y.pop(0)
        self.y_constructed=np.mat([self.y]).T

    def initialisation(self):
        rospy.init_node("lse")
        rate=rospy.Rate(2)
        H=np.mat([1,1,1,1,1,1,1,1,1]).T
        while not rospy.is_shutdown():
            self.construct_y(self.action_1)
            true_value=inv(H.T.dot(H)).dot(H.T.dot(self.y_constructed))  
            print('\n')
            ans=true_value.tolist()
            print('Final LSE estimated value: [{}]'.format(ans[0][0]))
            self.final_pub.publish(ans[0][0])
            rate.sleep()
if __name__ == '__main__':
    lse_f=Least_Square_Estimation_f()
    lse_b=Least_Square_Estimation_b()
    lse_r=Least_Square_Estimation_r()
    lse_l=Least_Square_Estimation_l()
    lse_f.initialisation()
    lse_b.initialisation()
    lse_r.initialisation()
    lse_l.initialisation()
