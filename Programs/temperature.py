print("** Temperature Converter **\n1. Fahrenheit\t2. Kelvin")
user = int(input("Enter your choice (1-2): "))
c = int(input("Enter the temperature in celsius: "))

if user == 1:
    f = (9/5)*c + 32;
    print("The temperature converted to fahrenheit is: ", f,"F")
elif user == 2:
    k = c+273.15
    print("The temperature converted to kelvin is: ", k, "K")