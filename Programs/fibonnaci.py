n = 12
num1 = 0
num2 = 1
num3 = num1 + num2
count = 1

print(num1, num2, end=" ")      # print on same line separated by space
while count <= n:
    print(num3, end=" ")
    num1, num2 = num2, num3
    num3 = num1 + num2

    count += 1