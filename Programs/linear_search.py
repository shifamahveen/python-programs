list = [1,2,3,4,5]
num = int(input("Enter number to be found: "))

for i in list:
    if i == num:
        print("Value found")
        break

if i == list[len(list)-1]:
    print("Value Not Found")