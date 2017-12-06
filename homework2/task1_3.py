length = int(raw_input())

list1 = []
raw1 = ''
input_str = map(int, raw_input().strip().split(' '))

string = ""
for j in range(2, length + 1):
    for i in range(2, j):
        if (j % i) == 0:
            break
    else:
        raw1 += str(j)
        list1.append(j)

print str(list1)
print raw1
print input_str

for i in range(len(input_str)):
    string += raw1[input_str[i]-1]

print string
