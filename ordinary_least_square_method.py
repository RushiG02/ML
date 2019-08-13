import pandas as pd
import numpy as np
m,c,lr,epoch=0,0,0.0001,1000
data= pd.read_csv('data_set.csv')
marks=pd.DataFrame(data)
X=marks['mse']
Y=marks['ese']

x = pd.Series(X)
y = pd.Series(Y)
r = round(x.cov(y)/(x.std()*y.std()),2)


b1 = round(r*y.std()/x.std(),2)

b0 = round(y.mean()-b1*x.mean(),2)
print(b1,b0)
