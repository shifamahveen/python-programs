a = 4
b = 6
def greater(a,b):
    if a>b:
        return a
    else:
        return b
def lcm(greater,a,b):
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            return lcm
        greater+=1

large = greater(a,b)
result = lcm(large,a,b)
print(result)






