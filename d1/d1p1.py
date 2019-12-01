import math

file = open("d1\\d1p1.txt","r")
lines = file.readlines()
file.close()
sum = 0
for line in lines:
    sum = sum + math.floor(int(line)/3) - 2
print("sum : {0}".format(sum))