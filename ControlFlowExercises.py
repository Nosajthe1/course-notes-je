print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
print(x[0:5])
# A1a:



print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
lists = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
for num in lists:
    if num % 2 == 0:
        print(num)


# A1b:



print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

for num in x[0:5]:
    if num % 2 == 0:
        print(num)
# A1c:


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
new_name_list = []
for letter in names:
    new_name_list.append(letter[0])
print(new_name_list)
# A2a:




print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names_list = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

index_list = []
for names in names_list:
    x = names.index(" ")
    index_list.append(x)
print(index_list)

# A2b:




print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

new_list = []

for name in names:
    new_list.append(name[0] + name[name.index(" ") + 1])
print(new_list)


# A2c:


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


for arr in list_of_lists:
    if len(arr) == len(set(arr)):
        print(arr)


# A3a:


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:

# player_num = int(input("Please enter a number greater than 100: "))
# while player_num < 100:
#     player_num = int(input("Please input another number: "))
#     if player_num >= 100:
#         print("Your number is " + str(player_num))




print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise


player_num = int(input("Please enter a number greater than 100: "))
while player_num < 100:
    player_num = int(input("Please input another number: "))
    if player_num >= 100:
        print("Your number is " + str(player_num))

if player_num > 1:
    for i in range(2, player_num, 1):
        if(player_num % i) == 0:
            print(f"{player_num} is not a prime number")
            break
        else:
            print(f"{player_num} is a prime number")
            break








# A4b:





