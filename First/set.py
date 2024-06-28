# set - collection, unordered, doesnt allow duplicates
fruits = {"apple", "banana", "orange"}
fruits.add("mango")         # adding single item
fruits.add("apple")

new_fruits = {"mango", "berries"}
list = [1, 2]
fruits.update(new_fruits)     # adding multiple elements / set / list/ tuple
fruits.update(list)

#
# list_of_fruits = ["cheeku", "dates"]
# fruits.update(list_of_fruits)
#
fruits.remove("apple")     # delete an item if present, if not present it gives an error
fruits.discard('cheeku')    # if element is not present, doesnt throw error
fruits.pop()        # deletes random element
fruits.clear()         # deletes all set items
print(fruits)
print(type(fruits))
# del fruits      # deletes the set instance
# print(fruits)

# frozenset
veggies = ({"carrot", "potato", "tomato"})
print(type(veggies))
veggies.add("chilli")
print(veggies)

