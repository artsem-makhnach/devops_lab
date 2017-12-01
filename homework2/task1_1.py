n = 0
students = []
listTmp = []
while n not in [2, 3, 4, 5]:
    n = int(raw_input())
for i in range(n):
    name = raw_input()
    score = float(raw_input())
    listTmp = [name, score]
    students.append(listTmp)
students.sort(key=lambda x: x[1])

listTmp = []
for i in range(n):
    listTmp.append(students[i][1])
minGrade = min(listTmp)

listTmp2 = []
for i in range(n):
    if listTmp[i] > minGrade and i == n-1:
        listTmp2.append(i)
        break
    elif listTmp[i] > minGrade and i < n-1 and listTmp[i] == listTmp[i+1]:
        listTmp2.append(i)
    elif listTmp[i] > minGrade and listTmp[i] < listTmp[i+1]:
        listTmp2.append(i)
        break

listTmp3 = []
for i in range(len(listTmp2)):
    listTmp3.append(students[i+1][0])

listTmp3.sort()
for i in range(len(listTmp3)):
    print (listTmp3[i])