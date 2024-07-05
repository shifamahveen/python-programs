# prime numbers -> which are divisible by 1 and itself
num = int(input("Enter a number: "))
flag = True

for i in range(2,num):
    if num%i == 0:
        flag = False
        break

if flag:
    print("Prime Number")
else:
    print("Not a prime")