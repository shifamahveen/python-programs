# String datatype
name = "this, is a beautiful day"

print(name.upper())     # capital letter
print(name.lower())     # lower case
print(name.capitalize())        # capitalize
print(name.index("thi")) # index method returns index if present, otherwise throws error
print(name.find("flower")) # returns index if found otherwise -1
print(name.count("z")) # count of occurrences in the string
print(name.replace("beautiful", "sunny"))
print(name.split(",")) # separates the string based on a character -  space(default)
