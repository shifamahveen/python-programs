list = [10, 20, 30]
marks = [100, 200, 300, 100]

# adding list items
list.append(40)     # add element at end of list
list.insert(1,15)      # add element at specified index
list.extend(marks)      # add multiple items / list / tuple

# deleting list items
list.pop()      # deletes last element if index not given, otherwise deletes element at specified index
list.remove(15)     # deletes the given value
list.clear()        # deletes all items

marks[1] = 20

print(marks.count(100))
print(len(marks))
list = marks.copy()
list.sort()
list.reverse()
print(list)
print(marks)