# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qzxaoYu8B8S-HahKayZfS2f-SzsmzU_o
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import pandas as pd
phy_marks = list(map(int,input().split()))
hist_marks = list(map(int,input().split()))
x = pd.Series(phy_marks)
y = pd.Series(hist_marks)
r = x.cov(y)/(x.std()*y.std())
print("%0.3f"%r)