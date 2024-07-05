x = int(input("enter a number: "))
fact = 1
# 3! = 3*2*1
# 5! = 5*4*3*2*1
# 0! = 1

for i in range(1, x+1):
    fact *= i

print("Factorial of",x, "is:", fact)
