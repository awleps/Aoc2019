
import math

file = open("d1\\d1p2.txt","r")
lines = file.readlines()
file.close()
sum = 0
for line in lines:
    v = math.floor(int(line)/3) - 2
    while (v > 0):
        sum = sum + v
        v = math.floor(v/3) - 2
print("sum : {0}".format(sum))