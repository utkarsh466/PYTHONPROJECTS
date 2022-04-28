import csv
import math

from numpy import square

with open('105.csv') as f:
    d=csv.reader(f)
    data=list(d)

data_list=[]
for i in data[0]:
    data_list.append(float(i))  

# print(data_list)
sum=0
l=len(data_list)
for i in data_list:
    sum+=i

mean=sum/l
# print(mean)

diff_list=[]

for i in data_list:
    x=i-mean
    diff_list.append(x)

# print(diff_list)    
squared_list=[]

for i in diff_list:
    sq=i**2
    squared_list.append(sq)
# print(squared_list)    
sqsum=0
for i in squared_list:
    sqsum+=i

# print(sqsum)     

temp=sqsum/(l-1)
stdv=math.sqrt(temp)
print(stdv) 