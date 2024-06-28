s1 = float(input("Subject 1: "))
s2 = float(input("Subject 2: "))
s3 = float(input("Subject 3: "))

avg = (s1+s2+s3) / 3
if avg >= 95 :
    print("A+")
elif avg>=90 and avg<95:
    print("A")
elif avg >= 80 and avg < 90:
    print("B")
elif avg >= 70 and avg < 80:
    print("C")
elif avg >= 60 and avg < 70:
    print("D")
elif avg >= 50 and avg < 60:
    print("E")
elif avg <50:
    print("F")
else:
    print("invalid")