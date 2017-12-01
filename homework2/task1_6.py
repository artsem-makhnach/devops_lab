input = map(int,raw_input().strip().split(' '))
print input
nod = 0
list1 = []
#list2 = []

for i in range(1,input[0]+1):
    if input[0]%i == 0 and input[1]%i == 0:
        list1.append(i)
print list1
print max(list1)