# count = 1
#
# while count <= 10:
#     print(count)
#     count = count + 1

#  print 10 to 1 -> 10, 9, 8, 7,    ,1
# even numbers between 1 to 10
i = 1

while i <= 10:
    print(i)

    if i%2 == 0:
        break
    i+=1

print("End of loop")