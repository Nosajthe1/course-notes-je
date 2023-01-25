print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1


def divisor(num: int = 1) -> int:
    div_list = []
    for n in range(1, num + 1, 1):
        if num % n == 0:
            div_list.append(n)
    print(div_list)
    return div_list


# divisor(20)
# A1a:

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function


def factor(num1, num2):
    div_list_num1 = divisor(num1)
    div_list_num2 = divisor(num2)
    if num1 in div_list_num2:
        return True
    if num2 in div_list_num1:
        return True
    else:
        return False


factor(6, 12)
# A1b:



# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


def letter_loc(word):
    return alphabet.index(word.lower())


letter_loc("F")
# A2a:


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14


def name_pos(word):
    a = ''
    for letter in word:
        a += str(letter_loc(letter))

    print(a)
    return a

# name_pos("bob")
# A2b:


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)


def password(word):
    a = 0
    word_num = name_pos(word)
    for i in word_num:
        a += int(i)
    print(int(word_num) - a)
    return int(word_num) - a

# password("bob")


# A2c:

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.
# def prime_checker(number):
#     if number > 1:
#         for num in range(2, number):
#             if number % num == 0:
#                 return False
#         return True
#     return False
#
# prime_checker(11)
# A3a:

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit


def prime_checker(number):
    int_number = int(number)
    if int_number > 1:
        for num in range(2, int_number):
            if int_number % num == 0:
                return False
        print("Hello")
        return True
    print("False")
    return False


prime_checker(7.1)




# A3b:



# -------------------------------------------------------------------------------------- #






