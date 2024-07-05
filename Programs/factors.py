x = int(input("Enter a number: "))

for i in range(1, x+1):     # 1,2,3,4,5
    if x%i == 0:
        print(i)