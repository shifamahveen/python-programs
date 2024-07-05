# factorial - 5!
# 5*4*3*2*1
x = int(input("Enter a number: "))
num = x
fact = 1

while x > 1:
    fact *= x
    x -= 1

print("The factorial of", num, "is:", fact)
