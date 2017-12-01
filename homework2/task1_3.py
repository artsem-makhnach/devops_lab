length = int(raw_input())
input = [1, 5, 7]
list = []
#a = 2
string = ""
for j in range(1, length + 1):
    if j > 1:
        for i in range(2, j):
            if (j % i) == 0:
                break
        else:
            list.append(j)

print list

for _ in range(len(input)):
    string += str(list[input[_]])
print string