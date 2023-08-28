# Que 2 - Write a Python program to read an entire text file.
file = open("example.txt", "r") 
text = file.read() 
file.close() 
print(text)

# Que 3 - Write a Python program to append text to a file and display the text
f = open("sample.txt", "a")

f.write("This is some additional text")
f.close()

f = open("sample.txt", "r")
print(f.read())
f.close()

# Que 4 - Write a Python program to read first n lines of a file. 
def read_first_n_lines(file_name, n):
    with open(file_name) as f:
        for i in range(n):
            print(f.readline())

read_first_n_lines('example.txt', 5)

# Que 5 - Write a Python program to read last n lines of a file. 
def read_last_n_lines(filename, n):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return lines[-n:]

last_5_lines = read_last_n_lines('myfile.txt', 5)

# Que 6 - Write a Python program to read a file line by line and store it into a list
f = open('myfile.txt', 'r') 

lines = f.readlines() 
f.close() 

print(lines)

# Que 7 - Write a Python program to read a file line by line store it into a variable.
file = open("filename.txt", "r")

for line in file:
    line_data = line

file.close()

# Que 8 - Write a python program to find the longest words.
def longest_words(sentence):
    words = sentence.split()
    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

sentence = input("Enter a sentence: ")
print("The longest word is:", longest_words(sentence))

# Que 9 - Write a Python program to count the number of lines in a text file.
file = open('textfile.txt', 'r')
count = 0

for line in file:
    count += 1

print('Number of lines in the file:', count)
file.close()

# Que 10 - Write a Python program to count the frequency of words in a file.
f = open("myfile.txt", "r")

wordcount = {}

for line in f:
    words = line.split()
    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

f.close()

for key, value in wordcount.items():
    print(key, value)

# Que 11 - Write a Python program to write a list to a file
items = ['apple', 'banana', 'cherry']

f = open("items.txt", "w")

for item in items:
    f.write(item + "\n")

f.close()

# Que 12 - Write a Python program to copy the contents of a file to another file. 
source_file = open("source.txt", "r") 
target_file = open("target.txt", "w") 

for line in source_file: 
    target_file.write(line) 

source_file.close() 
target_file.close() 

# Que 20 - Write python program that user to enter only odd numbers, else will raise an exception. 
def get_odd_number():
    while True:
        try:
            num = int(input("Enter an odd number: "))
            if num % 2 == 1:
                return num
            else:
                raise ValueError("Even number entered. Please enter an odd number.")
        except ValueError as e:
            print(e)

odd_number = get_odd_number()
print("You entered:", odd_number)

# Que 23 - Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

rectangle = Rectangle(10, 5)
print(rectangle.get_area())

# Que 24 - Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

print("Area of the circle:", circle.area())
print("Perimeter of the circle:", circle.perimeter())

