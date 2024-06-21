import csv
filename = "cereal_grains.csv"


#problem with this code is that it prints numeric values as string 

#with open(filename,'r',encoding='utf-8',newline="") as data:
#    reader = csv.reader(data)
#    for row in reader:
#        print(row)

#Fix!!
#NOTE: This only works if all numeric data has been quoted 
#       and it returns all the numeric data in float
with open(filename,'r',encoding='utf-8',newline='') as data:
    reader = csv.reader(data,quoting=csv.QUOTE_NONNUMERIC) #here we specify that the non numeric data has been quoted
    for row in reader:
        print(row)