import sys
input = sys.stdin.readline

data = []

count = 0
for i in range(8):
    data.append(list(map(str,input())))

for i in range(8):
    for j in range(8):
        if(i+j)%2 == 0:
            if data[i][j]=='F':
                count +=1
print(count)


