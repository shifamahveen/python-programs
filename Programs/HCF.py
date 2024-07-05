a = 30
b = 150
def smaller(a,b):
    if a<b:
        return a
    else:
        return b
def hcf(smaller,a,b):
    for i in range(1, smaller+1):   # i = 1,2,3,4,5,6,7,8
        if a%i == 0 and b%i == 0:
            hcf = i     # 1, 2, 4
    return hcf

small = smaller(a,b)
result = hcf(small,a,b)
print(result)