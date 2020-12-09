file = open("input1.txt","r")
numbers = file.readlines()
for i in range(0,len(numbers)):
    numbers[i] = int(numbers[i].strip("\n"))

result = 0

for i in range(0,len(numbers)):
    result += numbers[i] // 3 - 2

#---------------------PART2------------------#
file = open("input1.txt","r")
numbers = file.readlines()
for i in range(0,len(numbers)):
    numbers[i] = int(numbers[i].strip("\n"))

result = 0

for i in range(0,len(numbers)):
    while(numbers[i] // 3 - 2 >= 0):
        result += numbers[i] // 3 - 2
        numbers[i] = numbers[i] // 3 - 2
print(result)