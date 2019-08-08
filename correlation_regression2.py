import math
Score1 = list(map(int,input().split())) 
Score2 = list(map(int,input().split()))

m1 = (sum(Score1)/len(Score1))
m2 = (sum(Score2)/len(Score1))

Score_1 = [x-m1 for x in Score1]
Score_2 = [x-m2 for x in Score2]

n1 = sum([x*y for x,y in zip(Score_1,Score_2)])

Score1 = sum([(x-m1)**2 for x in Score1])
Score2 = sum([(x-m2)**2 for x in Score2])

n2 = (Score1**(1/2))*(Score2**(1/2))

r = n1/n2
sd1 = math.sqrt(Score1/len(Score_1))
sd2 = math.sqrt(Score2/len(Score_2))
print (round(r*sd2/sd1,3))
