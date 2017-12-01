input = ["5","-2","4","C","D","9","+","+"]

length = len(input)
print length

temp = []

for op in input:
    if op == "C":
        temp.pop()
    elif op == "D":
        temp.append(temp[-1]*2)
    elif op == "+":
        temp.append(temp[-1]+temp[-2])
    else:
        temp.append(int(op))
print sum(temp)