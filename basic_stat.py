# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = int(input())
a = list(map(int,input().split()))
mean = sum(a)/len(a)
a.sort()
if n%2==0:
    median = (a[int(n/2)]+a[int(n/2)-1])/2
else:
    median = a[int(n/2)+1]
count_i,mode = 0,0
for i in a:
    if a.count(i)>count_i:
        mode = i
        count_i = a.count(i)
a1 = [(x-mean)**2 for x in a]
sa1=sum(a1)
sd = math.sqrt(sa1/len(a))
n=math.sqrt(len(a))
ci_l,ci_u = mean-1.96*(sd/n),mean+1.96*(sd/n)
print(mean)
print(median)
print(mode)
print("%0.1f"%sd)
print(round(ci_l,1),round(ci_u,1))
