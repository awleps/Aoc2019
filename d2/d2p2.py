file = open("d2\\d2p2.txt","r")
inp = file.read().split(",")
file.close()
inp = [int(a) for a in inp]

for i in range(100):
    for j in range(100):
        data = inp.copy()
        data[1] = i
        data[2] = j
        try:
            for v in range(0,len(data),4):
                if data[v] == 1:
                    data[data[v+3]] = data[data[v+1]] + data[data[v+2]]
                elif data[v] == 2:
                    data[data[v+3]] = data[data[v+1]] * data[data[v+2]]
                elif data[v] == 99:
                    break
        except:
            continue
        if data[0] == 19690720:
            print("i= {0} j = {1}".format(i,j))