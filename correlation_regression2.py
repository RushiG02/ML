import math
phy_marks = [15 , 12 , 8  , 8 ,  7 ,  7 ,  7 ,  6   , 5  , 3] 
hist_marks = [10  ,25 , 17  ,11 , 13 , 17 , 20 , 13 , 9  , 15]
m1 = (sum(phy_marks)/len(phy_marks))
m2 = (sum(hist_marks)/len(hist_marks))

Score_1 = [x-m1 for x in phy_marks]
Score_2 = [x-m2 for x in hist_marks]

n1 = sum([x*y for x,y in zip(Score_1,Score_2)])

phy_marks = sum([(x-m1)**2 for x in phy_marks])
hist_marks = sum([(x-m2)**2 for x in hist_marks])

n2 = (phy_marks**(1/2))*(hist_marks**(1/2))

r = n1/n2
sd1 = math.sqrt(phy_marks/len(Score_1))
sd2 = math.sqrt(hist_marks/len(Score_2))
print (round(r*sd2/sd1,3))
