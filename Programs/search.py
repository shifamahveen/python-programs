# linear search
tuple = [10, 20, 30]
x = int(input("Enter a number: "))
i = 0

while i < len(tuple):       # 0, 1, 2
    if tuple[i] == x:
        print("Value found")
        break
    i += 1

if i == len(tuple):
    print("Value not found")