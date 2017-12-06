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
    if listTmp[i] != minGrade:
        listTmp2.append(listTmp[i])
minGrade2 = min(listTmp2)

listTmp3 = []
for i in range(len(listTmp)):
    if listTmp[i] == min(listTmp2):
        listTmp3.append(students[i][0])

listTmp3.sort()
for i in range(len(listTmp3)):
    print (listTmp3[i])