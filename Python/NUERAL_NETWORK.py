import numpy as np
import matplotlib.pyplot as ply


price=np.array([0,10,21,39,10,60,51,7,8])
area=np.array([0,1,2,3,4,5,6,7,8])

#                Try Removing Hash in Below two lines to Create more Random Data


from sklearn.linear_model import LinearRegression as lmd
p2=price.reshape(-1,1)
a2=area.reshape(-1,1)
lr=lmd.LinearRegression()
lr.fit(a2,p2)

m=0
c=0



##                            Try Putting Values of Irerations  100 , 600 ,1000 , 10000

irter=int(input('Enter no of Iterations to do :'))

L=0.01                   # L= Learning Rate , Try Putting L=  0.1  , 0.01 , 0.01

JJ=[]
ii=[]

for i in range(irter):
    ii.append(i)
    J = 0
    for l in range(len(price)):
        ss = (c + m * area[l] - price[l]) ** 2
        J = J + ss
    J = J / (2 * len(price))
    JJ.append(J)

    S1=0
    for j in range(len(area)):
        s1=(c+m*area[j]-price[j])*area[j]
        S1=S1+s1
    S2=0
    for k in range(len(price)):
        s2=(c+m*area[k]-price[k])
        S2=S2+s2
    m=m-(L*S1)/len(area)
    c=c-(L*S2)/len(area)


ply.title('Cost Function  V/S   No of Iterations')
ply.xlabel('ITERATIONS')
ply.ylabel('Cost Function')
ply.scatter(ii,JJ)
ply.show()

y=m*area+c

ply.title('Red Line is most Accurate')
ply.xlabel('Area')
ply.ylabel("Price")
ply.plot(a2,lr.coef_*a2+lr.intercept_,'r')
ply.scatter(area,price)
ply.plot(area,y)
ply.show()