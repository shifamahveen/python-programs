print("** Calculator App **\n1. Addition\t2. Subtraction\t3. Multiplication\t4. Division")
user = int(input("Enter your choice (1-4): "))
a = int(input("Enter A: "))
b = int(input("Enter B: "))

if user == 1:
    print("Addition of given numbers: ", a + b)
elif user == 2:
    print("Subtraction of given numbers: ", a - b)
elif user == 3:
    print("Multiplication of given numbers: ", a * b)
elif user == 4:
    print("Division of given numbers: ", a / b)
else:
    print("Invalid option")