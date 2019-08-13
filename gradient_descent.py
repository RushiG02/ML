import pandas as pd
import numpy as np
m,c,lr,epoch=0,0,0.001,100000
data= pd.read_csv('data_set.csv')
marks=pd.DataFrame(data)
x=marks['mse']
y=marks['ese']
mse_m=np.array(x)
ese_m=np.array(y)
n=float(len(mse_m))

for i in range(epoch):
    yp=mse_m*m+c
    dm=(-2/n)*sum(mse_m*(ese_m-yp))
    dc=(-2/n)*sum(ese_m-yp)
    m=m-lr*dm
    c=c-lr*dc
print(m,c)
