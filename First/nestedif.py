a = 12
b = 4
c = 16

if a<b and a<c:
    if b<c:
        print("Order: a, b, c")
    else:
        print("Order: a, c, b")
elif b<a and b<c:
    if a<c:
        print("Order: b, a, c")
    else:
        print("Order: b, c, a")
elif c<a and c<b:
    if a<b:
        print("Order: c, a, b")
    else:
        print("Order: c, b, a")
else:
    print("One of the numbers is equal")