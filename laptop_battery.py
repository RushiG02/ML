import numpy as np
import pandas as pd
X,Y = np.loadtxt("trainingdata.txt", delimiter=",",unpack=True)
x = pd.Series(X)
y = pd.Series(Y)
r = round(x.cov(y)/(x.std()*y.std()),2)


b1 = round(r*y.std()/x.std(),2)

b0 = round(y.mean()-b1*x.mean(),2)

x_ip = float(input())

print(round(b1*x_ip+b0,2))
