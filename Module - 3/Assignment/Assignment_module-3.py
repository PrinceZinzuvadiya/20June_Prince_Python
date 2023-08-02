# # Que 2 - How will you remove last object from a list? 
# list = [1,2,3,4,5]
# list.pop()
# print(list)

# # Que 5 - Write a Python function to get the largest number, smallest num and sum of all from a list. 
# def largest_smallest_sum(numbers):
#     largest_number = numbers[0]
#     smallest_number = numbers[0]
#     sum_of_numbers = 0

#     for number in numbers:
#         if number > largest_number:
#             largest_number = number
#         elif number < smallest_number:
#             smallest_number = number
#     sum_of_numbers += number

#     return largest_number, smallest_number, sum_of_numbers

# numbers = [10, 4, 2, 9, 7, 5, 1, 8, 6]
# largest_number, smallest_number, sum_of_numbers = largest_smallest_sum(numbers)
# print("The largest number is", largest_number)
# print("The smallest number is", smallest_number)
# print("The sum of all numbers is", sum_of_numbers)

# # Que 7 - Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# def count_strings(string_list):
#     count = 0
#     for string in string_list:
#         if len(string) >= 2 and string[0] == string[-1]:
#             count += 1
#     return count

# string_list = ["abc", "xyz", "aba", "1221"]

# result = count_strings(string_list)

# print(f"The number of strings with the same first and last character is {result}")

# # Que 8 - Write a Python program to remove duplicates from a list. 
# def remove_duplicates(list1):
#     unique_list = []
#     for item in list1:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list

# list1 = [1, 2, 3, 4, 5, 1, 2, 3]
# unique_list = remove_duplicates(list1)
# print(unique_list)

# # Que 9 - Write a Python program to check a list is empty or not. 
# l1 = input("Please enter a list")
# if len(l1)== 0 :
#     print("Please enter at least  2 values")
# else:
#     print(l1)    

# # Que 10 - Write a Python function that takes two lists and returns true if they have at least one common member. 
# def common_member(list1, list2):
#     for item in list1:
#         if item in list2:
#             return True
#     return False

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# print(common_member(list1, list2))

# Que 11 - Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30. 
# list_of_squares = [] 

# for i in range(1,31): 
#     list_of_squares.append(i**2) 

# print("First 5 elements are:", list_of_squares[:5]) 
# print("Last 5 elements are:", list_of_squares[-5:]) 

# Que 12 - Write a Python function that takes a list and returns a new list with unique elements of the first list. 
# def unique_list(lst): 
#     x = [] 
#     for i in lst:  
#         if i not in x: 
#             x.append(i) 
#     return x 

# list1 = [10,20,30,10,20,40,50]
# list2 = unique_list(list1)
# print(list2)

# Que 13 - Write a Python program to convert a list of characters into a string. 
# char_list = ['a', 'b', 'c', 'd']
# string = ""

# for char in char_list:
#     string += char
# print(string)

# Que 14 - Write a Python program to select an item randomly from a list.
# import random
# items = ['apple', 'banana', 'orange', 'strawberry']

# random_item = random.choice(items)
# print(random_item)

# Que 15 - Write a Python program to find the second smallest number in a list
# nums = [1, 9, 2, 8, 3, 7, 4, 6, 5]
# nums.sort()

# print(nums[1])

# Que 16 - Write a Python program to get unique values from a list
# list = [1,2,3,3,3,4,5,6,7,7,7,8]
# unique_list = []

# for item in list:
#     if item not in unique_list:
#         unique_list.append(item)

# print(unique_list)

# Que 17 - Write a Python program to check whether a list contains a sub list 
# def is_sublist(list1, list2):
#     if list2 == []:
#         return True
#     for i in range(len(list1)):
#         if list1[i:i + len(list2)] == list2:
#             return True
#     return False

# list1 = [1, 2, 3, 4, 5]
# list2 = [2, 3, 4]

# print(is_sublist(list1, list2))

# Que 18 - Write a Python program to split a list into different variables.
# def split_list(list):
#     var1 = list[0]
#     var2 = list[1]
#     var3 = list[2]
#     return var1, var2, var3

# list = ["apple", "banana", "cherry"]
# var1, var2, var3 = split_list(list)
# print(var1, var2, var3)

# Que 20 - Write a Python program to create a tuple with different data types.
# tup = (1, "Hello", 3.4)
# print(tup)

# print(type(tup))

# Que 21 - Write a Python program to create a tuple with numbers. 
# tup = (1,2,3,4,5,6,7)
# print(tup)

# Que 22 - Write a Python program to convert a tuple to a string. 
# tup = ('hello ', 'my ', 'name ', 'is ', 'prince')
# string = "".join(tup)
# print(string)

# Que 23 - Write a Python program to check whether an element exists within a tuple. 
# tuple = ("apple", "banana", "cherry")

# if "apple" in tuple:
#     print("Yes, 'apple' is in the sample tuple")
# else:
#     print("No, 'apple' is not in the sample tuple")

# Que 24 - Write a Python program to find the length of a tuple. 
# tuple = (10,20,30,40,50)
# print(len(tuple))

# Que 25 - Write a Python program to convert a list to a tuple. 
# list = [2,22,222,2222]
# my_tuple = tuple(list)
# print(my_tuple)

# Que 26 - Write a Python program to reverse a tuple.
# tuple = (10,9,8,7,6,5,4,3,2,1,0)
# print(tuple[::-1])
# print(tuple[-1::])
# print(tuple[::-2])

# Que 27 - Write a Python program to replace last value of tuples in a list.
# list_of_tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# replacement_value = 100

# list_of_tuples = [(t[0], t[1], replacement_value) for t in list_of_tuples]
# print(list_of_tuples)

# Que 28 - Write a Python program to find the repeated items of a tuple. 
# sample_tuple = (2, 4, 5, 6, 2, 3, 4, 4, 7)
# repeated_items = []

# for item in sample_tuple:
#     if item not in repeated_items:
#         if sample_tuple.count(item) > 1:
#             repeated_items.append(item)

# print(repeated_items)

# Que 29 - Write a Python program to remove an empty tuple(s) from a list of tuples
# list_of_tuples = [(), ('',), ('a', 'b'), ('c', 'd'), (), (), ('', '')] 

# list_of_tuples = [t for t in list_of_tuples if t]  
# print(list_of_tuples) 

# Que 30 - Write a Python program to unzip a list of tuples into individual lists.
# Initialize list of tuples 
# list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]  

# Unzip the list of tuples using *
# unzipped_list = list(zip(*list_of_tuples)) 

# Print unzipped lists  
# print(unzipped_list) 

# Que 31 - Write a Python program to convert a list of tuples into a dictionary
# list_of_tuples = [("apple", 5), ("orange", 3), ("banana", 4)]

# dict_from_tuples = dict(list_of_tuples)
# print(dict_from_tuples)

# Que 32 - How will you create a dictionary using tuples in python?
# tup = (1, "apple", 2, "orange", 3, "banana") 

# dict = dict(tup)  
# print(dict) 

# Que 33 - Write a Python script to sort (ascending and descending) a dictionary by value. 
# my_dict = {'a': 5, 'b': 2, 'c': 9, 'd': 6}

# # Sort the dictionary
# sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])

# # Print the sorted dictionary
# print(sorted_dict)

# # Output: [('b', 2), ('a', 5), ('d', 6), ('c', 9)]

# # Create a dictionary
# my_dict = {'a': 5, 'b': 2, 'c': 9, 'd': 6}

# # Sort the dictionary
# sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

# # Print the sorted dictionary
# print(sorted_dict)

# # Output: [('c', 9), ('d', 6), ('a', 5), ('b', 2)]

# Que 34 - Write a Python script to concatenate following dictionaries to create a new one
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}

# dict1.update(dict2)
# print(dict1)

# Create two dictionaries 
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}

# Concatenate two dictionaries 
# dict3 = {**dict1, **dict2}

# Print the result 
# print(dict3)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Que 35 - Write a Python script to check if a given key already exists in a dictionary. 
# sample_dict = {'name': 'John', 'age': 30}

# if 'name' in sample_dict:
#     print('Key exists!')
# else:
#     print('Key does not exist!')

# Que 36 - How Do You Traverse Through A Dictionary Object In Python? 
# my_dict = {
#     'key1': 'value1',
#     'key2': 'value2',
#     'key3': 'value3'
# }

# for key, value in my_dict.items():
# print(f'{key}: {value}')
#----------------------------------------#

# my_dict = {
#     'key1': 'value1',
#     'key2': 'value2',
#     'key3': 'value3'
# }

# for key in my_dict.keys():
#     print(f'{key}: {my_dict[key]}')
# #-----------------------------------------#

# my_dict = {
#     'key1': 'value1',
#     'key2': 'value2',
#     'key3': 'value3'
# }

# for value in my_dict.values():
#     for key in my_dict.keys():
#         if my_dict[key] == value:
#             print(f'{key}: {value}')
#             break

# Que 36 - How Do You Check The Presence Of A Key In A Dictionary?
# my_dict = {
#     'key1': 'value1',
#     'key2': 'value2'
# }

# if 'key1' in my_dict:
#     print('key1' is present in the dictionary')

# Que 37 - Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 
# my_dict = {}

# for i in range(1, 16):
#     my_dict[i] = i**1

# print(my_dict)

# Que 38 - Write a Python program to check multiple keys exists in a dictionary
# d = {'a': 1, 'b': 2, 'c': 3}
# keys = ['a', 'b', 'd']

# for key in keys:
#     if key in d:
#         print('{} key exists in the dictionary'.format(key))
#     else:
#         print('{} key does not exist in the dictionary'.format(key))

# Que 39 - Write a Python script to merge two Python dictionaries 
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}

# d1.update(d2)
# print(d1)

# Que 40 - Write a Python program to map two lists into a dictionary
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# dict_map = dict(zip(list1, list2))

# print(dict_map) 

# Que 41 - Write a Python program to combine two dictionary adding values for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200,'d':400}

# combined_dict = {}

# for d in (d1, d2):
#     for key, value in d.items():
#         if key in combined_dict:
#             combined_dict[key] += value
#         else:
#             combined_dict[key] = value

# print(combined_dict)

# Que 42 - Write a Python program to print all unique values in a dictionary. 
# my_dict = {
# "key1": "value1",
# "key2": "value2",
# "key3": "value1"
# }

# unique_values = []

# for value in my_dict.values():
#     if value not in unique_values:
#         unique_values.append(value)

# print(unique_values)

# Que 43 - Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# dict_letters = {'1': ['a','b'], '2': ['c','d']}

# combinations = []
# for letter1 in dict_letters['1']:
#     for letter2 in dict_letters['2']:
#         combinations.append(letter1 + letter2)

# print(combinations)

# Que 44 - Write a Python program to find the highest 3 values in a dictionary
# d = {'a': 6, 'b': 9, 'c': 3, 'd': 2, 'e': 8}

# highest_3 = []

# for key, value in d.items():
#     if len(highest_3) == 0:
#         highest_3.append(value)
#     elif len(highest_3) == 1:
#         highest_3.append(value)
#     elif len(highest_3) == 2:
#         highest_3.append(value)
#     elif len(highest_3) == 3:
#         if value > min(highest_3):
#             highest_3.remove(min(highest_3))
#             highest_3.append(value)

# highest_3.sort(reverse=True)
# print(highest_3)

# Que 45 - Write a Python program to combine values in python list of dictionaries.
# from collections 
# import Counter

# data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}] 

# result = Counter()
# for d in data:
#     result[d['item']] += d['amount']

# print(result)

# Que 46 - Write a Python program to create a dictionary from a string. 
# string = 'w3resource'

# dictionary = {} 

# for char in string: 

#     if char in dictionary: 
#         dictionary[char] += 1
#     else:  
#         dictionary[char] = 1

# print(dictionary)

# Que 47 - Write a Python function to calculate the factorial of a number (a nonnegative integer) 
# def calculate_factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * calculate_factorial(n-1)

# print(calculate_factorial(5))

# Que 48 - Write a Python function to check whether a number is in a given range
# def is_in_range(number, lower_bound, upper_bound):

#     if number >= lower_bound and number <= upper_bound:
#         return True
#     else:
#         return False

# number = 10
# lower_bound = 5
# upper_bound = 15

# print(is_in_range(number, lower_bound, upper_bound))

# Que 49 - Write a Python function to check whether a number is perfect or not
# def is_perfect(number):

#     sum_of_divisors = 1
#     for i in range(2, number):
#         if number % i == 0:
#             sum_of_divisors += i
#             sum_of_divisors += number // i

#     if sum_of_divisors == number:
#         return True
#     else:
#         return False

# number = 6
# print(is_perfect(number))

# Que 50 - Write a Python function that checks whether a passed string is palindrome or not.
# def is_palindrome(string):
#     reversed_string = ""
#     for i in range(len(string) - 1, -1, -1):
#         reversed_string += string[i]

#     return string == reversed_string

# string = "racecar"
# print(is_palindrome(string))

# Que 57 - Write a Python program to read a random line from a file.
# import random

# def read_random_line(filename):

#   with open(filename, "r") as f:
#     lines = f.readlines()

#   random_index = random.randrange(len(lines))
#   return lines[random_index]

# if __name__ == "__main__":
#   filename = "my_file.txt"
#   random_line = read_random_line(filename)
#   print(random_line)

# Que 58 - Write a Python program to convert degree to radian
# import math
# degree = 45
# radian = math.radians(degree)

# print("Degree:", degree)
# print("Radian:", radian)Write a Python program to convert degree to radian

# Que 59 - Write a Python program to calculate the area of a trapezoid 
# def trapezoid_area(a, b, h):
#   area = (a + b) * h / 2
#   return area

# area = trapezoid_area(2, 4, 3)
# print("The area of the trapezoid is:", area)

# Que 60 - Write a Python program to calculate the area of a parallelogram
# def parallelogram_area(b,h):
#     area = (b*h)
#     return area

# area = parallelogram_area(2,3)
# print("The area of parallelogram is ",area)

# Que 61 - Write a Python program to calculate surface volume and area of a cylinder
# import math
# r = float(input("Enter the radius of the cylinder: "))

# h = float(input("Enter the height of the cylinder: "))

# volume = math.pi * r * r * h

# area = 2 * math.pi * r * (r + h)

# print("The volume of the cylinder is: ", volume)
# print("The surface area of the cylinder is: ", area)

# Que 62 - Write a Python program to returns sum of all divisors of a number
# def divisors_sum(n):
#     sum = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             sum += i
#     return sum

# num = int(input("Enter a number: "))
# print("The sum of all divisors of", num, "is", divisors_sum(num))

# Que 63 - Write a Python program to find the maximum and minimum numbers from the specified decimal numbers. 
# decimal_numbers = [2.5, 0.25, 4.75, 3.14, 0.45]

# max_num = decimal_numbers[0]
# min_num = decimal_numbers[0]

# for num in decimal_numbers:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num

# print(f"The maximum number is {max_num}")
# print(f"The minimum number is {min_num}")