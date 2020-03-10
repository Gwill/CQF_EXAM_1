import math
import numpy as np, numpy.random
import pandas as pd

#==================================================
#MANUAL INPUTS
#==================================================
R=np.array([[1,0.3,0.3,0.3],[0.3,1,0.6,0.6],[0.3,0.6,1,0.6],[0.3,0.6,0.6,1]])
MU=np.array([0.02,0.07,0.15,0.20])
S=np.array([0.05,0.12,0.17,0.25])

m = 0.045

CORR_MULTIPLIER= 1.5

#print("CORR MUTLIPLIER: " + str(CORR_MULTIPLIER))

R =  R*CORR_MULTIPLIER

np.fill_diagonal(R, 1)

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

LAMBDA = (A*m - B)/(A*C - B*B)
GAMMA =  (C - B*m)/(A*C - B*B)

#print("A: " + str(A))
#print("B: " + str(B))
#print("C: " + str(C))
#print("LAMBDA: " + str(LAMBDA))
#print("GAMMA: " + str(GAMMA))

#CALCULATE W*
LAMBDA_MU = np.dot(LAMBDA,MU)
GAMMA_ONES = np.dot(GAMMA,ONES)
DIFF = LAMBDA_MU + GAMMA_ONES
W_STAR = np.dot(SRS_INV, DIFF)

#SUM OF WEIGHTS
SUM_WEIGHTS = np.sum(W_STAR)

#print("PORTFOLIO WEIGHTS BELOW:")
#print(W_STAR)
#print("SUM OF WEIGHTS: " + str(round(SUM_WEIGHTS,5)))

#PORTFOLIO RISK
W_STAR_TRANSP = W_STAR.transpose()
PORTF_RISK = np.dot(W_STAR_TRANSP,SRS)
PORTF_RISK = np.dot(PORTF_RISK,W_STAR)
PORTF_RISK = math.sqrt(PORTF_RISK)

#print("PORTFOLIO RISK BELOW:")
#print(PORTF_RISK)


#==================================================
#to plot random weights
#==================================================
random_df = pd.DataFrame(columns=['RISK','RETURN'])

for i in range(20000):
    RANDOM_W = np.random.dirichlet(np.ones(4),size=1)
    RANDOM_W = np.squeeze(np.asarray(RANDOM_W))
    RANDOM_W_TRANSP = RANDOM_W.transpose()
    RANDOM_PORT_RETURN = np.dot(MU_TRANSP,RANDOM_W)
    RANDOM_PORTF_RISK = np.dot(RANDOM_W_TRANSP,SRS)
    RANDOM_PORTF_RISK = np.dot(RANDOM_PORTF_RISK,RANDOM_W)
    RANDOM_PORTF_RISK = math.sqrt(RANDOM_PORTF_RISK)
    
    temporary_df = pd.DataFrame([[RANDOM_PORTF_RISK,RANDOM_PORT_RETURN]], columns=['RISK','RETURN'])
    random_df = random_df.append(temporary_df)

    
plot = random_df.plot.scatter(x='RISK',y='RETURN')    
print(random_df.head())
