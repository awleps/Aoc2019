
file = open("d2\\d2p1.txt","r")
inp = file.read().split(",")
file.close()
data = [int(a) for a in inp]

iter = 0
for v in range(0,len(data),4):
    value = data[v]
    if value == 1:
        data[data[v+3]] = data[data[v+1]] + data[data[v+2]]
    elif value == 2:
        data[data[v+3]] = data[data[v+1]] * data[data[v+2]]
    elif value == 99:
        print(data)
        break