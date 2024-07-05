print("** Sentence Evaluator App **\n1. Length of String\t2. No of words\t3. Membership")
user = int(input("Enter your choice (1-3): "))
str = input("Enter a String: ")

if user == 1:
    print(len(str))
elif user == 2:
    words = str.split()         # stores all words from str in "words"
    print(len(words))           # find length of the list having all words
elif user == 3:
    word = input("Enter the word you want to find: ")
    if str.find(word) > 0:      # check if word is present based on index
        print("It is present")
    else:
        print("Not present")
else:
    print("Invalid option")