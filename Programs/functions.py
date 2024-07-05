def welcome(name, city):
    print("Welcome!", name, "from", city)


welcome(city="Los Angeles", name="Alex")
welcome("Lisa", "Mumbai")

def func(name="Jack"):          # Default Parameter
    print("Hello,", name)

func("John")        # Hello, John
func()              # Hello, Jack