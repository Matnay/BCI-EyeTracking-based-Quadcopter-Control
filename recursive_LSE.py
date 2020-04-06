import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

I = np.array([0.2, 0.3, 0.4, 0.5, 0.6])
V = np.array([1.23, 1.38, 2.06, 2.47, 3.17])
plt.scatter(I, V)

plt.xlabel('current (A)')
plt.ylabel('voltage (V)')
plt.grid(True)
plt.show()

H = np.ones((5,2))
H[:, 0] = I
print(H.T)
x_ls = inv(H.T.dot(H)).dot(H.T.dot(V))
print('The parameters of the line fit are ([R, b]):')
print(x_ls)

#Plot
I_line = np.arange(0, 0.8, 0.1)
V_line = x_ls[0]*I_line + x_ls[1]

plt.scatter(I, V)
plt.plot(I_line, V_line)
plt.xlabel('current (A)')
plt.ylabel('voltage (V)')
plt.grid(True)
plt.show()

P_k=np.array([[10,0],[0,0.2]])
#Initialize the parameter estimate x
# x_k = ...
x_k=np.array([4.0,0])
#Our measurement variance
Var = 0.0225
Id=np.ones((2,2))
#Pre allocate our solutions so we can save the estimate at every step
num_meas = I.shape[0]
x_hist = np.zeros((num_meas + 1,2))
P_hist = np.zeros((num_meas + 1,2,2))

 
x_hist[0] = x_k
P_hist[0] = P_k

#Iterate over the measurements
for k in range(num_meas):
    #Construct H_k
    # H_k = ...
    H_k = np.array([[I[k], 1.0]])
    print(H_k)
    #Construct K_k
    # K_k = ...
    K_k = np.dot(P_k , np.dot(H_k.T , inv(np.dot(H_k,np.dot(P_k, H_k.T)) + Var)))
#     print(np.shape(K_k))
                    
    #Update our estimate
    # x_k = ...
    x_k = x_k + np.dot(K_k,(V[k]-np.dot(H_k,x_k)))
#     print(np.shape(x_k))
 
    #Update our uncertainty
    # P_k = ...
    P_k = np.dot((np.eye(2,2)-np.dot(K_k,H_k)),P_k)
#     print(np.shape(P_k))

    #Keep track of our history
    P_hist[k+1] = P_k
    x_hist[k+1] = x_k
    
print('The parameters of the line fit are ([R, b]):')
print(x_k) 