# Que 1 - Write a program to check if the number is positive, negative or zero.
num = float(input("Enter your number: "))

if num>0:
    print("The number you entered is positive.")
elif num<0:
    print("The number you entered is negative.")    
else:
    print("The number you entered is zero.")

# Que 2 - Write a Python program to get the Factorial number of given number.
num = int(input("Enter a number: "))

factorial = 1
for i in range(1, num+1):
   factorial = factorial * i

print(f"The factorial of {num} is {factorial} ")    

# Que - 3 Write a Python program to get the Fibonacci series of given range.
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if start > end:
    print("Start of the range should be less than the end of the range")
else:
    print("Fibonacci series of the given range is:")
    for i in range(start, end+1):
        print(Fibonacci(i))

# Que 4 - How memory is managed in Python?
with open('Que_4.txt', 'r') as f:
    data = f.read()
    print(data)

# Que 5 - What is the purpose continue statement in python?
with open('Que_5.txt', 'r') as f:
    data = f.read()
    print(data)

# Que 6 - Write python program that swap two number with temp variable and without temp variable.
    a = 34
    b = 50

    # With tmp variable
    tmp = a
    a = b
    b = tmp
print("A:", a)
print("B:", b)

    # Without tmp variable
a,b = b,a
print("A:", a)
print("B:", b)

# Que 7 - Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.
num = int(input("Enter a number: "))

if num%2 ==0:
    print("The number you entered is Even ")
else:
    print("The number you entered is odd.")

# Que 8 - Write a Python program to test whether a passed letter is a vowel or not.
word = input("Enter a word: ")

if word.endswith("a" and "e" and "i" and "o" and "u" and "A" and "E" and "I" and "O" and "U"):
    print("This is a vowel")
else :
    print("This is not a vowel")    

#Que 9 - Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1==n2:
    print("The sum of your three number is zero.")
elif n1==n3:
    print("The sum of your three number is zero.")
elif n2==n3:    
    print("The sum of your three number is zero.")
else:
    print("The sum of your three number is ", n1+n2+n3)

# Que 10 - Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if n1==n2:
    print("This is true")
elif n1+n2==5:
    print("This is true")
elif n1-n2==5 or n2-n1==5:    
    print("This is true")

# Que 11 - Write a python program to sum of the first n positive integers.
n = int(input("Enter a positive integer: "))

total = n * (n+1) / 2
print("The sum of the first",n,"positive integers",total)

# Que 12 - Write a Python program to calculate the length of a string.
string = ("Hello there I am Prince and I am currently working in Python")
print(len(string))

# Que 13 - Write a Python program to count the number of characters (character frequency) in a string
string = ("Hello there I am Prince and I am currently working in Python")
print(string.count("I"))

# Que 14 - What are negative indexes and why are they used?
with open('Que_14.txt', 'r') as f:
    data = f.read()
    print(data)

# Que 15 - Write a Python program to count occurrences of a substring in a string.
string = ("My name is Prince and the Prince of the city is Mr. Crown")
print(string.count("Prince"))

# Que 16 - Write a Python program to count the occurrences of each word in a given sentence
sentence = input("Enter a sentence: ")

# split the sentence into words
words = sentence.split()

# create an empty dictionary
word_count = {}

# count the occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# print the result
for word, count in word_count.items():
    print(word, ":", count)

# Que 17 - Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
str1 = "This is the string number1"
str2 = "That is the string number2 "
str1, str2 = str2, str1
combine_str = str1 + str2
print(combine_str)

# Que 18 - Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.
string = input("Enter a word: ")
if len(string) <= 3:
    print("Please enter a word which contains minimum 3 words")
elif string.endswith("ing"):
    print(string + "ly")
else:
    print(string + "ing")    

# Que 19 Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
message = "The food is not that much poor"
print(message.find("not"))
print(message.find("poor"))

if "poor" > "not":
    print(message.replace ("not that much poor", "good"))

# Que 20 - Write a Python function that takes a list of words and returns the length of the longest one.
def longest_word_length(word_list):
    max_length = 0
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

words = ['apple', 'banana', 'orange', 'kiwi']
length = longest_word_length(words)
print("The lenth of the longest one is", length)

# Que 21 - Write a Python function to reverses a string if its length is a multiple of 4.
def reverse_string(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return string

string1 = "Hello"
string2 = "Princess"
string3 = "OpenAI"
string4 = "Wolf"

print(reverse_string(string1))
print(reverse_string(string2))
print(reverse_string(string3)) 
print(reverse_string(string4))

# Que 22 - Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
def get_string(string):
    if len(string) < 2:
        return ''
    else:
        return string[:2] + string[-2:]

input_string = input("Enter a string:")
result = get_string(input_string)
print("Result:", result)

# Que 23 - Write a Python function to insert a string in the middle of a string.
def insert_string_in_middle(original_string, string_to_insert):
    middle_index = len(original_string) // 2
    return original_string[:middle_index] + string_to_insert + original_string[middle_index:]

original = "Hello World"
to_insert = "Python"
result = insert_string_in_middle(original, to_insert)
print(result)
