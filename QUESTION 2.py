import math
import numpy as np, numpy.random
import pandas as pd


#==================================================
#MANUAL INPUTS
#==================================================

R=np.array([[1,0.3,0.3,0.3],[0.3,1,0.6,0.6],[0.3,0.6,1,0.6],[0.3,0.6,0.6,1]])
MU=np.array([0.02,0.07,0.15,0.20])
S=np.array([0.05,0.12,0.17,0.25])

m=4.5/100

"""#FOR TRAINING ONLY
R=np.array([[1,0.8,0.5,0.4],[0.8,1,0.7,0.5],[0.5,0.7,1,0.8],[0.4,0.5,0.8,1]])
MU=np.array([0.05,0.07,0.15,0.27])
S=np.array([0.07,0.12,0.30,0.60])
"""

#print("PLEASE SEE BELOW THE CORREL MATRIX:")
#print(S)

#==================================================
#CALCULATIONS BELOW
#==================================================

#CALCULATE SRS
S=np.diag(S)
SR=np.dot(S,R)
SRS=np.dot(SR,S)

#print("THE SRS IS BELOW:")
#print(SRS)

#CALCULATE A,B,C
ONES = np.array([1,1,1,1])
ONES_TRANSP = ONES.transpose()
SRS_INV = np.linalg.inv(SRS)
MU_TRANSP = MU.transpose()

A = np.dot(ONES_TRANSP,SRS_INV)
A = np.dot(A,ONES)

B = np.dot(MU_TRANSP,SRS_INV)
B = np.dot(B,ONES)

C = np.dot(MU_TRANSP,SRS_INV)
C = np.dot(C,MU)

#LAMBDA = (A*m - B)/(A*C - B*B)
#GAMMA =  (C - B*m)/(A*C - B*B)

#print("A: " + str(A))
#print("B: " + str(B))
#print("C: " + str(C))
#print("LAMBDA: " + str(LAMBDA))
#print("GAMMA: " + str(GAMMA))


#==================================================
#TANGENCY PORTFOLIO
#==================================================

tangency_df = pd.DataFrame(columns=['Risk Free Rate','Return','Standard Dev'])

RATE_1 = 0.50/100
RATE_2 = 1/100
RATE_3 = 1.5/100
RATE_4 = 1.75/100
RATE_5 = 2.5/100

LIST_OF_RATES = [RATE_1,RATE_2,RATE_3,RATE_4,RATE_5]

#print('========== NEXT RATE =========')

for rate in LIST_OF_RATES:

    TANGENT_W = MU - np.dot( rate , ONES )
    TANGENT_W = np.dot( SRS_INV , TANGENT_W )
    B_MINUS_AR = 1/(B - A*rate)
    TANGENT_W = np.dot( TANGENT_W , B_MINUS_AR )

    RETURN_PORTFOLIO = (C-B*rate)*B_MINUS_AR
    STDEV_PORTFOLIO = math.sqrt((C-2*B*rate + A*rate*rate)*B_MINUS_AR*B_MINUS_AR)
    
    """
    print('For Risk Free Rate = ' + str(rate) + ', please see below the weights:')
    print(TANGENT_W)
    print ('SUM OF THE WEIGHTS: ' + str(round(TANGENT_W.sum(),5)))
    print('RETURN OF THE PORTFOLIO IS BELOW:')
    print(RETURN_PORTFOLIO)
    print('STANDARD DEV OF THE PORTFOLIO IS BELOW:')
    print(STDEV_PORTFOLIO)
    print('========== NEXT RATE =========')
    """
    
    temporary_df = pd.DataFrame([[rate,RETURN_PORTFOLIO,STDEV_PORTFOLIO]],columns=['Risk Free Rate','Return','Standard Dev'])
    tangency_df = tangency_df.append(temporary_df)

print(tangency_df)
