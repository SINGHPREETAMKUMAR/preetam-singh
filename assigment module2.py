"""
1. WAP to sum of the first n positive integers
"""
# n = int(input("Enter a number: "))
# sum = (n * (n + 1)) / 2
# print("sum : ", sum)

"""
2. WAP to count occurences of a substring in a string
"""

# string = input("Enter a string: ")
# substring = input("Enter a substring: ")
# count = string.count(substring)
# print(f"The substring '{substring}' occurs {count} times in the string.")

"""
3. WAP to count the occurences of each word in a sentence
"""

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] +=1

#     else:
#         word_count[word] =1

# print("word frequency")
# for word, count in word_count.items():
#   print(f"{word}: {count}")

"""
4. WAP to get a single string from two given strings, separated by a space and swap the first two characters of each string.
"""

# str1 = "Python"
# str2 = "Java"

# newstr1 = str2[:2]+str1[2:] + " " + str1[:2]+str2[2:]
# print(newstr1)

"""
5. WAP to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead If the string length of the given string is less than 3, leave it unchanged
"""
# string = input("Enter a string: ")

# if len(string) < 3:
#     new_string = string
# elif string[-3:] =="ing":
#     new_string = string + "ily"
# else:
#     new_string = string + "ing"
# print("New string: ", new_string)

"""
7. Program to find greatest common divisor of two numbers.
"""

# def hcf(a, b):
#     if(b == 0):
#         return a
#     else:
#         return hcf(b, a % b)
#     a = 4
#     b = 14

# print("GCD of a and b is : ")
# print(hcf(4, 14))

"""
8. Write a python program to check whether a list contains a sublist.
"""

# def is_sublist(list1, list2):
#     return set(list1).issubset(set(list2))

# list1 = [1,2,3]
# list2 = [0,1,2,3,4,5]

# if is_sublist(list1, list2):
#     print("List 2 contains List 1 as a sublist.")
# else:
#     print("List 2 does not contain List 1 as a sublist")

"""
9. Write a Python program to find the second smallest number in a list.
"""

# l1 = [1,2,3,4,5,10,13,15]
# l1.sort()
# print("Second smallest number: ", l1[1])

"""
10. Write a python program to get a unique values from a list.
"""

# s = {10,20,30,30,20,10,61,35,61,35}
# print(s)

"""
11. Write a python program to unzip of tuples into individual lists.
"""

# t = (10,20,30,40,50,60)
# print(t)
# for item in t:
#     print(item)

"""
12. Write a Python program to convert of tuples into dictionary.
"""

# t = [("Apple", 1), ("Orange", 2)]
# print(t)
# my_dict = dict(t)
# print(my_dict)

"""
13. Write a Python program to sort a dictionary (ascending/descending)by value
"""
# my_dict = {"apple" : 10, "banana" : 5, "mango" : 15}
# asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
# desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse = True))
# print("original dictionary:", my_dict)
# print("sorted dictionary (ascending):" ,(asc))
# print("sorted dictionary (descending):", (desc))

"""
14. Write a Python program to find the highest 3 values in dictionary.
"""

# my_dict = {"a": 10, "b": 14, "c": 20, "d": 12, "e": 11}
# sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
# highest_values = [value for key, value in sorted_dict[:3]]
# print("The hoghest 3 values in the dictionary are:", highest_values)

"""
15. Given a number n, write a python program to make and print the list of Fibonacci series up to n.
Input: n = 7
Hint : first 7 numbers in the series
Expected output:
First few Fibonacci numbers are 0,1,1,2,3,5,8,13
"""

# def fibonacciseries(i):
#     if i <= 1:
#         return i
#     else:
#         return(fibonacciseries(i - 1) + fibonacciseries(i -2))
# num = int(input("Enter the Number: "))
# if num <= 0:
#     print("Please enter a positive number")
# else:
#     print("Fibonacci Series:", end=" ")
# for i in range(num):
#     print(fibonacciseries(i), end=" ")

"""
16. Counting the frequencies in a list using a dictionary in Python.
"""
# L1 = [1,2,3,4,5,2,34,6,7,8,9,0,9]
# freq = {}
# for item in L1:
#     if(item in freq):
#         freq[item] += 1
#     else:
#         freq[item] = 1
# for key, value in freq.items():
#     print("% d: % d"%(key, value))

"""
18. Write a Python program to find the factorial of number using Recursion.
"""

# num = int(input("Enter the Number: "))
# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return (n * factorial_recursive(n-1))

#     print("Factorial using recursive method ", factorial_recursive(number))

"""
19. Write a Python program that takes a list and returns a new list with unique elements of the first list.
"""

# def unique_list(l1):
#     x = []
#     for a in l:
#         if a not in x :
#             x.append(a)
#         return x 
#     print(unique_list([1,2,3,3,3,4,4,5,6]))

"""
20. Make a program to generate a strong password using the input given by the user. To generate a password,
randomly take some words from the user input and then include numbers, special characters and capital
letters to generate the password. Also, keep a check that password length is more than 8 characters.
"""
# import random
# import array
 
# db = {} #blank dictionary

# def Creat_Pass(firstname,password): # function with parameters..
#     db['name'] = firstname
#     db['password'] = password
#     print("Password created successfully...")

# def Access_Pass(name):
#     if name == db['name']:
#         return db['password']
               
#     else:
#         return "User not found.."
    
# status = True
# while status:

#     menu = """
#             1) press 1 for creating Password
#             2) press 2 for accessing Password
#             3) press 3 for exit
#     """
#     print(menu)

#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         name = input("Enter name: ")
    
#         MAX_LEN = 8

#         DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

#         LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
#                             'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
#                             'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#                             'z']
        
#         UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
#                             'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
#                             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
#                             'Z']
        
#         SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
#                 '*', '(', ')', '<']

#         COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

#         rand_digit = random.choice(DIGITS)
#         rand_upper = random.choice(UPCASE_CHARACTERS)
#         rand_lower = random.choice(LOCASE_CHARACTERS)
#         rand_symbol = random.choice(SYMBOLS)
        
#         temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
        
#         for x in range(MAX_LEN - 4):
#             temp_pass = temp_pass + random.choice(COMBINED_LIST)
        
#             temp_pass_list = array.array('u', temp_pass)
#             random.shuffle(temp_pass_list)
        
#         password = ""
#         for x in temp_pass_list:
#                 password = password + x
                
#         print(password)

#         Creat_Pass(name,password)

#     elif choice == 2:
#         name = input("Enter name: ")
#         print(Access_Pass(name))

#     elif choice == 3:
#         status = False
