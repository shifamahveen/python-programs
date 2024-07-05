# Arbitrary arguments
def demo(**fruits):
    print(fruits['f1'])

demo(f1="apple", f2="banana", f3="cherry")