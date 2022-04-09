import csv
from collections import Counter
with open('SOCR-HeightWeight.csv') as f:
    data=csv.reader(f)
    data_list=list(data)

data_list.pop(0)
weight_list=[]
for i in data_list:
    weight_list.append(float(i[2]))
weight_list.sort()

tp=len(weight_list)
weight=0
for i in weight_list:
    weight+=i

if(tp%2==0):
    median1=weight_list[tp//2]
    median2=weight_list[(tp//2)-1]
    median=(median1+median2)/2
else:
    median=weight_list[tp//2]

mean=weight/tp


new_data=Counter(weight_list)
# print(new_data)
mode_data_for_range={"75-85":0,"85-95":0,"95-105":0,"105-115":0,"115-125":0,"125-135":0,"135-145":0,"145-155":0,"155-165":0,"165-175":0}
for height,occurence in new_data.items():
    if 75<height<85:
        mode_data_for_range["75-85"]+=occurence
    elif 85<height<95:
        mode_data_for_range["85-95"]+=occurence
    elif 95<height<105:
        mode_data_for_range["95-105"]+=occurence
    elif 105<height<115:
        mode_data_for_range["105-115"]+=occurence
    elif 115<height<125:
        mode_data_for_range["115-125"]+=occurence
    elif 125<height<135:
        mode_data_for_range["125-135"]+=occurence            
    elif 135<height<145:
        mode_data_for_range["135-145"]+=occurence    
    elif 145<height<155:
        mode_data_for_range["145-155"]+=occurence    
    elif 155<height<165:
        mode_data_for_range["155-165"]+=occurence        
    else:
        mode_data_for_range["165-175"]+=occurence

        
mode_range,mode_occurence = 0,0
for range,occurrence in mode_data_for_range.items():
    if occurrence>mode_occurence:
        mode_range,mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurrence
    
mode=(mode_range[0]+mode_range[1])/2
print("Mean (Average) is -> "+str(mean))
print("Median is -> "+str(median))
print("Mode is -> "+str(mode))