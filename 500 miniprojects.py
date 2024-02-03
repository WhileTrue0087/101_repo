#   Telegram channel ID ==> @PythonCV














# Variables تمرین های رشته

# 1. Declare two variables, x and y, and assign them the values 5 and 10. Print the sum of the two 
# variables. 
x = 5
y = 10
print(x + y)


# 2. Declare a variable name and assign it your name as a string. Print a greeting message that 
# uses the name variable. 
name = "John"
print("Hello, " + name + "!")


# 3. Declare a variable radius and assign it the value of a radius of a circle. Calculate the 
# circumference of the circle using the formula 2 * pi * radius, where pi is the mathematical 
# constant for pi. Print the result. 
import math
radius = 3.5
circumference = 2 * math.pi * radius
print(circumference)


# 4. Declare two variables, a and b, and assign them values. Swap the values of the two variables 
# without using a third variable. Print the values of a and b before and after the swap. 
a = 10
b = 20
print("Before swap: a =", a, ", b =", b)
a, b = b, a
print("After swap: a =", a, ", b =", b)



# 5. Declare a variable age and assign it an integer value. Use conditional statements to print a 
# message that changes based on the value of age. If age is less than 18, print "You are a 
# minor". If age is between 18 and 65, print "You are an adult". If age is greater than 65, print 
# "You are a senior citizen". 
age = 25
if age < 18:
    print("You are a minor")
elif age >= 18 and age <= 65:
    print("You are an adult")
else:
    print("You are a senior citizen")



# 6. Declare a variable favorite_foods and assign it a list of your favorite foods. Print the first and 
# last items in the list. 
favorite_foods = ["pizza", "sushi", "ice cream"]
print(favorite_foods[0])
print(favorite_foods[-1])



# 7. Declare a variable sales_tax_rate and assign it a floating-point value representing a sales tax 
# rate as a percentage. Declare another variable price and assign it a value. Calculate the total 
# price with tax included and print the result. 
sales_tax_rate = 8.25
price = 100
total_price = price + (sales_tax_rate / 100 * price)
print(total_price)



# 8. Declare a variable my_tuple and assign it a tuple of three values. Access the second value in 
# the tuple and print it. 
my_tuple = (1, 2, 3)
print(my_tuple[1])


# 9. Declare a variable my_dict and assign it a dictionary with three key-value pairs. Access the 
# value of one of the keys and print it. 
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict["age"])


# 10. Declare a variable my_set and assign it a set of three values. Print the length of the set.
my_set = {1, 2, 3}
print(len(my_set))




# 1. Declare a variable message and assign it a string. Print the length of the string. 
message = "Hello, world!"
print(len(message))


# 2. Declare two variables, num1 and num2, and assign them integer values. Print the result of 
# adding, subtracting, multiplying, and dividing the two variables. 
num1 = 10
num2 = 5
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)


# 3. Declare a variable my_list and assign it a list of numbers. Print the sum of the numbers in the 
# list. 
my_list = [1, 2, 3, 4, 5]
sum = 0
for num in my_list:
    sum += num
print(sum)


# 4. Declare a variable my_string and assign it a string. Convert the string to uppercase and print 
# the result. Declare a variable num and assign it an integer value. Use a loop to print the 
# numbers from 1 to num (inclusive). 
my_string = "hello, world!"
print(my_string.upper())


# 5. Declare a variable my_dict and assign it a dictionary with at least 3 key-value pairs. Print the 
# keys and values of the dictionary using a loop. 
num = 5
for i in range(1, num+1):
    print(i)



# 6. Declare a variable x and assign it an integer value. 
my_dict = {"name": "John", "age": 30, "city": "New York"}
for key, value in my_dict.items():
    print(key, value)


# 7. Declare another variable y and assign it the value of x squared. Print the value of y. 
x = 5
y = x ** 2
print(y)


# 8. Declare a variable my_set and assign it a set of numbers. Check if a specific number is in the 
# set and print the result. 
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)



# 9. Declare a variable my_list and assign it a list of strings. Use a loop to print each string in the 
# list with an exclamation mark at the end. 
my_list = ["apple", "banana", "orange"]
for fruit in my_list:
    print(fruit + "!")

# 10. Declare a variable my_tuple and assign it a tuple of strings. Use a loop to print each string in 
# the tuple in reverse order.
my_tuple = ("apple", "banana", "orange")
for i in range(len(my_tuple)-1, -1, -1):
    print(my_tuple[i])



# 1. Declare a variable num and assign it an integer value. Use a loop to print the even numbers 
# from 0 to num (inclusive). 
num = 10
for i in range(0, num+1, 2):
    print(i)


# 2. Declare a variable my_dict and assign it a dictionary with at least 3 key-value pairs. Add a 
# new key-value pair to the dictionary, and then remove one of the existing key-value pairs. 
my_dict = {"name": "John", "age": 30, "city": "New York"}
my_dict["occupation"] = "programmer"
del my_dict["age"]
print(my_dict)



# 3. Declare a variable my_string and assign it a string of words. Use the split() method to split 
# the string into a list of words, and then print the list. 
my_string = "The quick brown fox"
my_list = my_string.split()
print(my_list)


# 4. Declare a variable my_list and assign it a list of numbers. Use a loop to calculate the product 
# of the numbers in the list. 
my_list = [1, 2, 3, 4, 5]
product = 1
for num in my_list:
 product *= num
print(product)



# 5. Declare a variable my_tuple and assign it a tuple of integers. Print the maximum and 
# minimum values in the tuple. 
my_tuple = (1, 2, 3, 4, 5)
print(max(my_tuple))
print(min(my_tuple))


# 6. Declare a variable my_list and assign it a list of strings. Use a loop to create a new list that 
# contains the length of each string in the original list. 
my_list = ["apple", "banana", "orange"]
new_list = []
for word in my_list:
    new_list.append(len(word))
print(new_list)


# 7. Declare a variable x and assign it an integer value. Declare another variable y and assign it 
# the value of x divided by 2. Print the value of y, and then update the value of x to be 10. Print 
# the value of y again. Declare a variable my_set1 and assign it a set of numbers. 
x = 20
y = x / 2
print(y)
x = 10
print(y)


# 8. Declare another variable my_set2 and assign it a set of numbers that includes some (but not 
# all) of the same numbers as my_set1. Use set operations to create a new set that contains all 
# the unique numbers from both sets. 
my_set1 = {1, 2, 3, 4, 5}
my_set2 = {3, 4, 5, 6, 7}
new_set = my_set1.union(my_set2)
print(new_set)


# 9. Declare a variable my_dict and assign it a dictionary with at least 3 key-value pairs. Use a 
# loop to print the keys of the dictionary in alphabetical order. 
my_dict = {"name": "John", "age": 30, "city": "New York"}
for key in sorted(my_dict.keys()):
    print(key)


# 10. Declare a variable my_list and assign it a list of strings. Use a loop to create a new list that 
# contains the strings from the original list in reverse order.
my_list = ["apple", "banana", "orange"]
new_list = []
for i in range(len(my_list)-1, -1, -1):
    new_list.append(my_list[i])
print(new_list)


# 1. Declare a variable my_list and assign it a list of integers. Use a loop to calculate the sum of 
# the numbers in the list. 
my_list = [1, 2, 3, 4, 5]
sum = 0
for num in my_list:
    sum += num
print(sum)


# 2. Declare a variable my_tuple and assign it a tuple of strings. Use a loop to create a new list 
# that contains the uppercase versions of the strings in the tuple. 
my_tuple = ("apple", "banana", "orange")
new_list = []
for word in my_tuple:
    new_list.append(word.upper())
print(new_list)


# 3. Declare a variable my_string and assign it a string of words. Use string formatting to print 
# the string in title case. 
my_string = "the quick brown fox"
print(my_string.title())


# 4. Declare a variable my_list and assign it a list of strings. Use a loop to create a new list that 
# contains the strings from the original list with all the vowels removed.
my_list = ["apple", "banana", "orange"]
new_list = []
vowels = "aeiou"
for word in my_list:
    new_word = ""
    for letter in word:
        if letter.lower() not in vowels:
            new_word += letter
    new_list.append(new_word)
print(new_list)


# 5. Declare a variable my_dict and assign it a dictionary with at least 3 key-value pairs. Use the 
# items() method to print the key-value pairs in the dictionary. 
my_dict = {"name": "John", "age": 30, "city": "New York"}
for key, value in my_dict.items():
    print(key, value)
    
    
# 6. Declare a variable my_string and assign it a string of words. Use a loop to create a new string 
# that contains the words from the original string in reverse order, separated by spaces. 
my_string = "the quick brown fox"
words = my_string.split()
new_string = ""
for i in range(len(words)-1, -1, -1):
    new_string += words[i] + " "
print(new_string.strip())


# 7. Declare a variable my_list and assign it a list of integers. Use a loop to create a new list that 
# contains the square of each number in the original list. 
my_list = [1, 2, 3, 4, 5]
new_list = []
for num in my_list:
 new_list.append(num ** 2)
print(new_list)


# 8. Declare a variable my_set and assign it a set of strings. Use the sorted() function to create a 
# new list that contains the strings from the original set in alphabetical order. 
my_set = {"orange", "apple", "banana"}
new_list = sorted(list(my_set))
print(new_list)


# 9. Declare a variable my_list and assign it a list of strings. Use a loop to create a new list that 
# contains the first letter of each string in the original list. 
my_list = ["apple", "banana", "orange"]
new_list = []
for word in my_list:
    new_list.append(word[0])
print(new_list)


# 10. Declare a variable my_dict and assign it a dictionary with at least 3 key-value pairs. Use the 
# keys() method to create a new list that contains the keys from the dictionary in reverse 
# order.
my_dict = {"name": "John", "age": 30, "city": "New York"}
new_list = list(reversed(list(my_dict.keys())))
print(new_list)

# String تمرین های رشته


# 1. Write a Python program to print the length of a string.
import string
string = "Hello, world!"
print(len(string))


# 2. Write a Python program to count the number of characters in a string.
string = "Hello, world!"
count = 0
for char in string:
    count += 1
print(count)
# 3. Write a Python program to reverse a string.
string = "Hello, world!"
reverse = ""
for char in string:
    reverse = char + reverse
print(reverse)

# 4. Write a Python program to check whether a string is a palindrome or not.
string = "racecar"
reverse = ""
for char in string:
    reverse = char + reverse
if string == reverse:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")


# 5. Write a Python program to remove all the vowels from a string.
string = "Hello, world!"
vowels = "aeiouAEIOU"
new_string = ""
for char in string:
    if char not in vowels:
        new_string += char
print(new_string)

# 6. Write a Python program to check whether a string contains only letters.
string = "Hello, world!"
is_alpha = True
for char in string:
    if not char.isalpha():
        is_alpha = False
        break
if is_alpha:
    print("The string contains only letters")
else:
    print("The string does not contain only letters")

# 7. Write a Python program to check whether a string is a pangram or not.
string = "The quick brown fox jumps over the lazy dog"
alphabet = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True
for char in alphabet:
    if char not in string.lower():
        is_pangram = False
        break
if is_pangram:
    print("The string is a pangram")
else:
    print("The string is not a pangram")

# 8. Write a Python program to capitalize the first letter of each word in a sentence.
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
new_sentence = ""
for word in words:
    new_sentence += word.capitalize() + " "
print(new_sentence)



# 9. Write a Python program to remove all the punctuation from a string.
import string
string = "Hello, world! This is a sentence with punctuation."
new_string = string.translate(str.maketrans("", "", string.punctuation))
print(new_string)


# 10. Write a Python program to concatenate two strings.
string1 = "Hello"
string2 = "world"
concatenated = string1 + " " + string2
print(concatenated)



# 11. Write a Python program to check whether two strings are anagrams of each other. 
str1 = "silent"
str2 = "listen"
if sorted(str1) == sorted(str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")


# 12. Write a Python program to find the most common character in a string. 
string = "Hello, world!"
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
most_common_char = max(char_count, key=char_count.get)
print(f"The most common character is {most_common_char}")


# 13. Write a Python program to check whether a string is a substring of another string. 
string1 = "Hello, world!"
string2 = "world"
if string2 in string1:
    print("The second string is a substring of the first string")
else:
    print("The second string is not a substring of the first string")


# 14. Write a Python program to remove all the spaces from a string. 
string = "Hello, world!"
no_spaces = ""
for char in string:
    if char != " ":
        no_spaces += char
print(no_spaces)


# 15. Write a Python program to find the first non-repeating character in a string. 
string = "Hello, world!"
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char in string:
    if char_count[char] == 1:
        print(f"The first non-repeating character is {char}")
    break


# 16. Write a Python program to check whether a string is a valid URL or not. 
import re
url = "https://www.google.com"
pattern = re.compile(r"https?://(www\.)?\w+\.\w+")
if pattern.match(url):
    print("The URL is valid")
else:
    print("The URL is not valid")



# 17. Write a Python program to remove all the duplicate characters from a string. 
string = "Hello, world!"
no_duplicates = ""
for char in string:
    if char not in no_duplicates:
        no_duplicates += char
print(no_duplicates)


# 18. Write a Python program to find the second most common character in a string. 
string = "Hello, world!"
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
second_most_common_char = sorted_char_count[1][0]
print(f"The second most common character is {second_most_common_char}")



# 19. Write a Python program to convert a string to title case. 
string = "the quick brown fox"
title_case = ""
for word in string.split():
    title_case += word.capitalize() + " "
print(title_case)




# 21. Write a Python program to find the frequency of each word in a given sentence. 
sentence = "Hello world hello"
words = sentence.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items():
    print(f"{word}: {count}")


# 22. Write a Python program to reverse a string word by word. 
string = "Hello world"
words = string.split()
reversed_words = words[::-1]
reversed_string = " ".join(reversed_words)
print(reversed_string)


# 23. Write a Python program to check if a given string is a palindrome or not. 
string = "racecar"
if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")



# 24. Write a Python program to find the first occurrence of a word in a given string. 
string = "Hello world hello"
word = "hello"
if word in string:
    index = string.index(word)
    print(f"The word '{word}' first occurs at index {index}")
else:
    print(f"The word '{word}' does not occur in the string")




# 25. Write a Python program to remove all the vowels from a string. 
string = "Hello world"
vowels = "aeiou"
no_vowels = ""
for char in string:
    if char.lower() not in vowels:
        no_vowels += char
print(no_vowels)



# 26. Write a Python program to count the number of words in a given sentence. 
sentence = "Hello world"
words = sentence.split()
print(f"There are {len(words)} words in the sentence")



# 27. Write a Python program to capitalize the first letter of each word in a given sentence. 
sentence = "hello world"
capitalized_words = []
for word in sentence.split():
    capitalized_words.append(word.capitalize())
capitalized_sentence = " ".join(capitalized_words)
print(capitalized_sentence)


# 28. Write a Python program to sort the words in a given sentence in alphabetical order. 
sentence = "hello world"
sorted_words = sorted(sentence.split())
sorted_sentence = " ".join(sorted_words)
print(sorted_sentence)



# 29. Write a Python program to find the longest word in a given sentence. 
sentence = "Hello world, how are you doing today?"
longest_word = max(sentence.split(), key=len)
print(f"The longest word is '{longest_word}'")



# 30. Write a Python program to find the most frequent word in a given sentence.
sentence = "Hello world hello"
word_count = {}
for word in sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
most_frequent_word = max(word_count, key=word_count.get)
print(f"The most frequent word is '{most_frequent_word}'")



# 1. Write a Python program to find the common characters in two given strings. 
string1 = "hello"
string2 = "world"
common_chars = set(string1) & set(string2)
print(f"The common characters are {', '.join(common_chars)}")




# 2. Write a Python program to check if two given strings are anagrams of each other. 
string1 = "silent"
string2 = "listen"
if sorted(string1) == sorted(string2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")


# 3. Write a Python program to find the second most frequent character in a given string. 
string = "hello world"
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
second_most_frequent_char = sorted_char_count[1][0]
print(f"The second most frequent character is '{second_most_frequent_char}'")


# 4. Write a Python program to find the first non-repeating character in a given string. 
string = "hello world"
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char in string:
    if char_count[char] == 1:
        print(f"The first non-repeating character is '{char}'")
        break


# 5. Write a Python program to find the length of the longest substring without repeating characters in a given string.
string = "abcabcbb"
max_length = 0
start = 0
char_index_map = {}
for i in range(len(string)):
    if string[i] in char_index_map and start <= char_index_map[string[i]]:
        start = char_index_map[string[i]] + 1
    else:
        max_length = max(max_length, i - start + 1)
    char_index_map[string[i]] = i
print(f"The length of the longest substring without repeating characters is {max_length}")


# 6. Write a Python program to count the number of vowels in a given string. 
string = "hello world"
vowels = "aeiou"
vowel_count = 0
for char in string:
    if char.lower() in vowels:
        vowel_count += 1
print(f"There are {vowel_count} vowels in the string")



# 7. Write a Python program to count the number of consonants in a given string. 
string = "hello world"
vowels = "aeiou"
consonant_count = 0
for char in string:
    if char.isalpha() and char.lower() not in vowels:
        consonant_count += 1
print(f"There are {consonant_count} consonants in the string")


# 8. Write a Python program to remove all the duplicate characters from a given string. 
string = "hello world"
unique_chars = []
for char in string:
    if char not in unique_chars:
        unique_chars.append(char)
unique_string = "".join(unique_chars)
print(unique_string)


# 9. Write a Python program to find the smallest window in a given string containing all characters of another string.

string = "this is a test string"
pattern = "tist"
# initialize variables
start = 0
end = 0
min_window = None
pattern_dict = {}
for char in pattern:
    if char in pattern_dict:
        pattern_dict[char] += 1
    else:
        pattern_dict[char] = 1
count = len(pattern_dict)
# find smallest window
while end < len(string):
    if string[end] in pattern_dict:
        pattern_dict[string[end]] -= 1
        if pattern_dict[string[end]] == 0:
            count -= 1
    end += 1
    while count == 0:
        if min_window is None or end - start < len(min_window):
            min_window = string[start:end]
        if string[start] in pattern_dict:
            pattern_dict[string[start]] += 1
            if pattern_dict[string[start]] > 0:
                count += 1
        start += 1
print(f"The smallest window containing all characters of the pattern is '{min_window}'")


# 10. Write a Python program to check if a given string contains only digits.
sentence = "this is a test sentence for testing the word count program"
# split the sentence into words
words = sentence.split()
# create a dictionary to store word counts
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
# print the word counts
for word, count in word_counts.items():
    print(f"'{word}': {count}")









# List تمرین های لیست




# 1. Create a list of your favorite colors and print the list. 
favorite_colors = ['blue', 'green', 'red', 'purple', 'orange']
print(favorite_colors)


# 2. Create a list of numbers from 1 to 10 and print the list. 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)


# 3. Create a list of the first 5 even numbers and print the list. 
even_numbers = [2, 4, 6, 8, 10]
print(even_numbers)


# 4. Create a list of the first 5 odd numbers and print the list. 
odd_numbers = [1, 3, 5, 7, 9]
print(odd_numbers)


# 5. Create a list of your favorite movies and print the list. 
favorite_movies = ['The Godfather', 'The Shawshank Redemption', 'The Dark Knight', 'Pulp Fiction', 
'The Matrix']
print(favorite_movies)


# 6. Write a program to print the length of a given list. 
my_list = [1, 2, 3, 4, 5]
print(len(my_list))


# 7. Write a program to find the maximum number in a given list. 
my_list = [3, 6, 2, 8, 1, 9]
print(max(my_list))


# 8. Write a program to find the minimum number in a given list. 
my_list = [3, 6, 2, 8, 1, 9]
print(min(my_list))


# 9. Write a program to print the sum of all the numbers in a given list. 
my_list = [1, 2, 3, 4, 5]
print(sum(my_list))


# 10. Write a program to remove all the duplicates from a given list. 
my_list = [1, 2, 2, 3, 4, 4, 5, 5]
new_list = list(set(my_list))
print(new_list)


# 11. Write a program to remove the first and last element of a given list. 
my_list = [1, 2, 3, 4, 5]
my_list = my_list[1:-1]
print(my_list)


# 12. Write a program to reverse a given list. 
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)


# 13. Write a program to sort a given list in ascending order. 
my_list = [3, 6, 2, 8, 1, 9]
my_list.sort()
print(my_list)


# 14. Write a program to sort a given list in descending order. 
my_list = [3, 6, 2, 8, 1, 9]
my_list.sort(reverse=True)
print(my_list)


# 15. Write a program to check if a given list is empty or not.
my_list = []
if not my_list:
    print("The list is empty")
else:
    print("The list is not empty")



# 1. Write a program to find the second largest number in a given list. 
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique_list = list(set(my_list))
unique_list.sort()
second_largest = unique_list[-2]
print("The second largest number in the list is:", second_largest)


# 2. Write a program to find the second smallest number in a given list. 
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique_list = list(set(my_list))
unique_list.sort()
second_smallest = unique_list[1]
print("The second smallest number in the list is:", second_smallest)


# 3. Write a program to count the number of even numbers in a given list. 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
for num in my_list:
    if num % 2 == 0:
        count += 1
print("The number of even numbers in the list is:", count)



# 4. Write a program to count the number of odd numbers in a given list. 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
for num in my_list:
    if num % 2 != 0:
        count += 1
print("The number of odd numbers in the list is:", count)


# 5. Write a program to find the index of a given element in a list. 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element = 5
index = my_list.index(element)
print("The index of", element, "in the list is:", index)


# 6. Write a program to insert an element at a specific index in a given list. 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element = 10
index = 4
my_list.insert(index, element)
print("The list after inserting", element, "at index", index, "is:", my_list)


# 7. Write a program to remove an element from a given list by its value. 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 4
del my_list[index]
print("The list after removing the element at index", index, "is:", my_list)


# 8. Write a program to remove an element from a given list by its index. 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 4
del my_list[index]
print("The list after removing the element at index", index, "is:", my_list)


# 9. Write a program to check if a given list is sorted in ascending order. 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if my_list == sorted(my_list):
    print("The list is sorted in ascending order")
else:
    print("The list is not sorted in ascending order")


# 10. Write a program to check if a given list is sorted in descending order. 
my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
if my_list == sorted(my_list, reverse=True):
    print("The list is sorted in descending order")
else:
    print("The list is not sorted in descending order")


# 11. Write a program to merge two given lists into a single list. 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print("The merged list is:", merged_list)


# 12. Write a program to copy a given list to another list. 
my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()
print("The new list is:", new_list)


# 13. Write a program to find the largest and smallest numbers in a given list. 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
largest = max(my_list)
smallest = min(my_list)
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)



# 14. Write a program to find the average of all the numbers in a given list.
my_list = [1, 2, 3, 4, 5]
average = sum(my_list) / len(my_list)
print("The average of the numbers in the list is:", average)


# 15. Write a program to split a given list into two equal halves. 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
half = len(my_list) // 2
first_half = my_list[:half]
second_half = my_list[half:]
print("The first half of the list is:", first_half)
print("The second half of the list is:", second_half)



# 8. Find the second largest number in a list:
my_list = [1, 2, 3, 4, 5]
largest = second_largest = float('-inf')
for num in my_list:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest:
        second_largest = num
print("The second largest number in the list is:", second_largest)


# 9. Count the number of occurrences of a given element in a list:
my_list = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1]
element = 1
count = my_list.count(element)
print("The number of occurrences of", element, "in the list is:", count)



# 10.Remove the first occurrence of a given element in a list:
my_list = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1]
element = 2
if element in my_list:
    my_list.remove(element)
    print("The first occurrence of", element, "has been removed from the list.")
else:
    print("Element not found in list.")

# 5. Declare a variable my_list and assign it a list of strings. Write a function that takes a string as 
#   input and returns a new list containing all the strings from the original list that start with the 
#       input string. 
def string_start(my_list, input_string):
    new_list = []
    for string in my_list:
        if string.startswith(input_string):
            new_list.append(string)
    return new_list
my_list = ['hello', 'world', 'goodbye', 'python', 'list']
print(string_start(my_list, 'h'))


















# if...else   تمرین های 

# 1) Check if a given number is even or odd:
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")


# 2) Check if a given year is a leap year or not:
year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# 3) Check if a given character is a vowel or consonant:
ch = input("Enter a character: ")
if ch in ('a', 'e', 'i', 'o', 'u'):
    print(ch, "is a vowel")
else:
    print(ch, "is a consonant")


# 4) Check if a given number is positive, negative, or zero:
num = float(input("Enter a number: "))
if num > 0:
    print(num, "is positive")
elif num == 0:
    print(num, "is zero")
else:
    print(num, "is negative") 

# 5) Find the largest among three numbers:
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    print(a, "is the largest")
elif b >= a and b >= c:
    print(b, "is the largest")
else:
    print(c, "is the largest")


# 6) Find the smallest among three numbers:
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a <= b and a <= c:
    print(a, "is the smallest")
elif b <= a and b <= c:
    print(b, "is the smallest")
else:
    print(c, "is the smallest")


# 7) Check if a given number is a prime number or not:
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# 8) Find the factorial of a given number:
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)


# 9) Print the Fibonacci series up to a given number:
n = int(input("Enter a number: "))
a, b = 0, 1
if n >= 1:
    print(a)
if n >= 2:
    print(b)
for i in range(2, n):
    c = a + b
    a = b
    b = c
    if n >= i + 1:
        print(c)
    else:
        break


# 10) Check if a given string is a palindrome or not:
string = input("Enter a string: ")
if string == string[::-1]:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")


# 1) Checking if a string is a palindrome or not:
string = input("Enter a string: ")
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# 2) Counting the number of vowels and consonants in a string:
string = input("Enter a string: ")
vowels = 0
consonants = 0
for i in string:
    if i.lower() in 'aeiou':
        vowels += 1
    elif i.isalpha():
        consonants += 1
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)


# 3) Finding the second largest number in a list:
lst = [3, 6, 2, 8, 1, 9, 4]
largest = lst[0]
second_largest = lst[0]
for i in lst:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print("The second largest number is:", second_largest)


# 4) Finding the second smallest number in a list:
lst = [3, 6, 2, 8, 1, 9, 4]
smallest = lst[0]
second_smallest = lst[0]
for i in lst:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i < second_smallest and i != smallest:
        second_smallest = i
print("The second smallest number is:", second_smallest)

# 5) Finding the largest element in a list:
lst = [3, 6, 2, 8, 1, 9, 4]
largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print("The largest element is:", largest)


# 6) Finding the smallest element in a list:
lst = [3, 6, 2, 8, 1, 9, 4]
smallest = lst[0]
for i in lst:
    if i < smallest:
        smallest = i
print("The smallest element is:", smallest)


# 7) Checking if a number is a perfect square or not:
import math
num = int(input("Enter a number: "))
if math.isqrt(num)**2 == num:
    print("The number is a perfect square.")
else:
    print("The number is not a perfect square.")


# 8) Checking if a string is a valid identifier or not:
identifier = input("Enter an identifier: ")
if identifier.isidentifier():
    print("The identifier is valid.")
else:
    print("The identifier is not valid.")


# 9) Checking if a number is a multiple of 5 and 7:
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 7 == 0:
    print("The number is a multiple of 5 and 7.")
else:
    print("The number is not a multiple of 5 and 7.")


# 10) Checking if a year is a leap year using the 
# ternary operator:

year = int(input("Enter a year: "))
leap = True if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else False
if leap:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


# 10) Write a program to find the difference of two numbers 
# using the ternary operator.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
diff = (a - b) if a > b else (b - a)
print("The difference between the two numbers is:", diff)

# Write a program to find the smallest among four numbers 
# using the ternary operator.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
smallest = a if (a < b and a < c and a < d) else (b if (b < c and b <
d) else (c if c < d else d))
print("The smallest number is", smallest)














# Arrays  تمرین های 


# 1) Write a Python program to create an array of 5 integers and 
# display the array items.
arr = [1, 2, 3, 4, 5]
print(arr)



# 2) Write a Python program to append a new item to the end of the 
# array.
arr = [1, 2, 3, 4, 5]
arr.append(6)
print(arr)


# 3) Write a Python program to reverse the order of the items in the 
# array.
arr = [1, 2, 3, 4, 5]
arr.reverse()
print(arr)


# 4) Write a Python program to remove the first occurrence of a 
# specified element from an array.
arr = [1, 2, 3, 4, 5]
arr.remove(3)
print(arr)



# 5) Write a Python program to insert a new item before the second 
# element in an existing array
arr = [1, 2, 3, 4, 5]
arr.insert(1, 6)
print(arr)


# 6) Write a Python program to remove a specified item using the 
# index from an array.
arr = [1, 2, 3, 4, 5]
del arr[2]
print(arr)


# 7) Write a Python program to find the number of occurrences of a 
# specified element in an array.
arr = [1, 2, 3, 4, 3, 5, 3]
count = arr.count(3)
print(count)


# 8) Write a Python program to concatenate two arrays.
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = arr1 + arr2
print(arr3)


# 9) Write a Python program to find the common values between two 
# arrays.
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
common = list(set(arr1) & set(arr2))
print(common)


# 10) Write a Python program to find the elements in an array 
# that are not present in another array.
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
not_present = [x for x in arr1 if x not in arr2]
print(not_present)



# 1) Write a Python program to find the union of two arrays.
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
union_arr = list(set(arr1 + arr2))
print(union_arr)


# 2) Write a Python program to find the intersection of two arrays.
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
intersection_arr = [x for x in arr1 if x in arr2]
print(intersection_arr)


# 3) Write a Python program to find the difference between two arrays.
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
difference_arr = [x for x in arr1 if x not in arr2]
print(difference_arr)


# 4) Write a Python program to remove all duplicate elements from an array.
arr = [1, 2, 3, 2, 4, 5, 1]
unique_arr = list(set(arr))
print(unique_arr)


# 5) Write a Python program to create a 2D array and print its values.
rows = 3
cols = 3
arr = [[0]*cols for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        arr[i][j] = i * j
for i in range(rows):
    for j in range(cols):
        print(arr[i][j], end=' ')
    print()


# 6) Write a Python program to add two matrices.
X = [[1,2,3],
    [4,5,6],
    [7,8,9]]
Y = [[10,11,12],
    [13,14,15],
    [16,17,18]]
result = [[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)


# 7) Write a Python program to subtract two matrices.
X = [[1,2,3],
    [4,5,6],
    [7,8,9]]
Y = [[10,11,12],
    [13,14,15],
    [16,17,18]]
result = [[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] - Y[i][j]
for r in result:
    print(r)


# 8) Write a Python program to multiply two matrices.
# define the matrices as arrays
matrix1 = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
matrix2 = [[10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]]
# create an empty result matrix with the correct dimensions
result = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]
# iterate through each row of the first matrix
for i in range(len(matrix1)):
    # iterate through each column of the second matrix
    for j in range(len(matrix2[0])):
        # iterate through each row of the second matrix
        for k in range(len(matrix2)):
            # multiply the corresponding elements of the two matrices and 
            # add the result to the appropriate cell in the result matrix
            result[i][j] += matrix1[i][k] * matrix2[k][j]
# print the result matrix
for row in result:
    print(row)


# 9) Python program to find the transpose of a matrix:
# define a matrix
matrix = [[1, 2],
    [3, 4],
    [5, 6]]
# create an empty result matrix
result = [[0, 0, 0],
    [0, 0, 0]]
# iterate through the rows of the matrix
for i in range(len(matrix)):
    # iterate through the columns of the matrix
    for j in range(len(matrix[0])):
        result[j][i] = matrix[i][j]
# print the transpose matrix
for r in result:
    print(r)


# 10) Python program to find the sum of diagonal 
# elements of a matrix:
# define a matrix
matrix = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
# initialize the sum to 0
sum = 0
# iterate through the rows of the matrix
for i in range(len(matrix)):
    # iterate through the columns of the matrix
    for j in range(len(matrix[0])):
        # check if the current element is on the diagonal
        if i == j:
            sum += matrix[i][j]
# print the sum of diagonal elements
print("The sum of diagonal elements is:", sum)





# 1) Find the maximum element in a matrix:
def find_max(matrix):
    max_element = matrix[0][0]
    for row in matrix:
        for element in row:
            if element > max_element:
                max_element = element
    return max_element
# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Maximum element:", find_max(matrix)) # Output: 
# Maximum element: 9


# 2) Find the minimum element in a matrix:
def find_min(matrix):
    min_element = matrix[0][0]
    for row in matrix:
        for element in row:
            if element < min_element:
                min_element = element
    return min_element
# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Minimum element:", find_min(matrix)) # Output: 
# Minimum element: 1


# 3) Find the trace of a matrix:
def find_trace(matrix):
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]
    return trace
# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Trace:", find_trace(matrix)) # Output: Trace: 15


# 4) Find the determinant of a matrix:
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for j in range(n):
            minor = [[matrix[i][k] for k in range(n) if k != j] for i in 
range(1, n)]
        det += matrix[0][j] * (-1) ** j * determinant(minor)
    return det
# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Determinant:", determinant(matrix)) # Output: 
# Determinant: 0


# 5) Find the inverse of a matrix:
import numpy as np
# creating a sample matrix
matrix = np.array([[1, 2], [3, 4]])
# finding the inverse of the matrix
inverse = np.linalg.inv(matrix)
print("Original Matrix:")
print(matrix)
print("Inverse of the Matrix:")
print(inverse)


# 6) Find the rank of a matrix:
import numpy as np
# creating a sample matrix
matrix = np.array([[1, 2], [3, 4]])
# finding the rank of the matrix
rank = np.linalg.matrix_rank(matrix)
print("Original Matrix:")
print(matrix)
print("Rank of the Matrix:")
print(rank)


# 7) Find the eigenvalues and eigenvectors of a matrix:
import numpy as np
# creating a sample matrix
matrix = np.array([[1, 2], [3, 4]])
# finding the eigenvalues and eigenvectors of the matrix
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Original Matrix:")
print(matrix)
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)


# 8) Sort an array in ascending order:
# creating a sample array
array = [3, 2, 1, 5, 4]
# sorting the array in ascending order
sorted_array = sorted(array)
print("Original Array:")
print(array)
print("Sorted Array in Ascending Order:")
print(sorted_array)


# 9) Sort an array in descending order:
# creating a sample array
array = [3, 2, 1, 5, 4]
# sorting the array in descending order
sorted_array = sorted(array, reverse=True)
print("Original Array:")
print(array)
print("Sorted Array in Descending Order:")
print(sorted_array)


# 10) Sort a list of tuples based on the second element of each 
# tuple:
# create a list of tuples
tuples_list = [("apple", 3), ("banana", 2), ("cherry", 4), ("date", 1)]
# convert the list of tuples to an array
arr = np.array(tuples_list)
# sort the array based on the second column (index 1)
arr_sorted = arr[arr[:, 1].argsort()]
# convert the sorted array back to a list of tuples
tuples_list_sorted = list(map(tuple, arr_sorted))
print(tuples_list_sorted)



# 1) Write a Python program to merge two sorted arrays into a single 
# sorted array.
def merge_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    merged_arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1
    return merged_arr

# 2) Write a Python program to find the median of an array.
def find_median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        median = (arr[n//2 - 1] + arr[n//2])/2
    else:
        median = arr[n//2]
    return median


# 3) Write a Python program to find the mode of an array.
from collections import Counter
def find_mode(arr):
    counter = Counter(arr)
    mode = counter.most_common(1)
    return mode[0][0]


# 4) Write a Python program to find the average of an array.
def find_average(arr):
    n = len(arr)
    if n == 0:
        return 0
    return sum(arr)/n


# 5) Write a Python program to find the standard deviation of an array.
import math
def find_standard_deviation(arr):
    n = len(arr)
    if n == 0:
        return 0
    mean = sum(arr)/n
    variance = sum((x - mean)**2 for x in arr)/n
    std_deviation = math.sqrt(variance)
    return std_deviation


# 6) Write a Python program to find the variance of an array.
def find_variance(arr):
    n = len(arr)
    if n == 0:
        return 0
    mean = sum(arr)/n
    variance = sum((x - mean)**2 for x in arr)/n
    return variance

# 7) Write a Python program to find the range of an array.
def find_range(arr):
    if len(arr) == 0:
        return 0
    return max(arr) - min(arr)


# 8) Write a Python program to find the percentile of an array.
def find_percentile(arr, p):
    arr.sort()
    n = len(arr)
    index = (p/100) * (n-1)
    if index.is_integer():
        percentile = arr[int(index)]
    else:
        percentile = (arr[int(index)] + arr[int(index)+1])/2
    return percentile


# 9) Write a Python program to find the frequency of each element in 
# an array.

from collections import Counter
def find_frequency(arr):
    counter = Counter(arr)
    frequency_dict = dict(counter)
    return frequency_dict


# 10) Write a Python program to find the index of the first 
# occurrence of a specified element in an array.
def find_first_occurrence(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1
# example usage
arr = [2, 3, 5, 7, 7, 8, 9]
num = 7
index = find_first_occurrence(arr, num)
if index == -1:
    print(f"{num} is not found in the array.")
else:
    print(f"The index of the first occurrence of {num} is {index}.")
















# While loop   تمرین های 


# 1. Write a program that prints the numbers from 1 to 10 using a while loop.
i = 1
while i <= 10:
    print(i)
    i += 1


# 2. Write a program that asks the user to enter a number and prints the multiplication table for 
# that number up to 10.
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1


# 3. Write a program that generates a random number between 1 and 10 and asks the user to 
# guess the number. If the user's guess is too high or too low, the program should give a hint 
# and ask the user to guess again.
import random
number = random.randint(1, 10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Congratulations, you guessed the number!")
        break
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")


# 4. Write a program that asks the user to enter a password. The program should keep asking the 
# user to enter a password until the password matches a predefined password.
password = "secret"
while True:
    guess = input("Enter the password: ")
    if guess == password:
        print("Correct password!")
        break
    else:
        print("Incorrect password, try again.")


# 5. Write a program that asks the user to enter a series of numbers, one at a time. The program 
# should stop asking for numbers when the user enters a negative number. The program 
# should then print the sum of all the positive numbers entered.
sum = 0
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    sum += num
print("The sum of the positive numbers entered is:", sum)


# 6. Write a program that asks the user to enter a number and calculates the factorial of that 
# number using a while loop.
num = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print("The factorial of", num, "is", factorial)


# 7. Write a program that generates a random number between 1 and 100 and asks the user to 
# guess the number. The program should give the user hints to help them guess the number, 
# and the user should be allowed to guess up to 10 times.
import random
number = random.randint(1, 100)
guesses = 0
while guesses < 10:
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1
    if guess == number:
        print("Congratulations, you guessed the number!")
        break
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
else:
    print("Sorry, you've run out of guesses. The number was", number)


# 8. Write a program that asks the user to enter a series of numbers and prints the largest and 
# smallest numbers entered. The program should stop asking for numbers when the user 
# enters the word "done".
largest = None
smallest = None
while True:
    num = input("Enter a number or type 'done': ")
    if num == "done":
        break
    try:
        num = int(num)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except ValueError:
        print("Invalid input")
if largest is not None and smallest is not None:
    print("The largest number entered was", largest)
    print("The smallest number entered was", smallest)


# 9. Write a program that asks the user to enter a string and counts the number of vowels in the 
# string using a while loop.
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
i = 0
while i < len(string):
    if string[i] in vowels:
        count += 1
    i += 1
print("The number of vowels in the string is", count)



# 10. Write a program that asks the user to enter a series of numbers and prints the sum of the 
# even numbers entered. The program should stop asking for numbers when the user enters a /
# number that is not an integer.
sum = 0
while True:
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            sum += num
    except ValueError:
        break
print("The sum of the even numbers entered is", sum)


# 1. Write a program that asks the user to enter a series of numbers and calculates the average 
# of the numbers entered. The program should stop asking for numbers when the user enters 
# the word/ "done".
sum = 0
count = 0
while True:
    num = input("Enter a number or type 'done': ")
    if num == "done":
        break
    try:
        num = int(num)
        sum += num
        count += 1
    except ValueError:
        print("Invalid input")
if count > 0:
    average = sum / count
    print("The average of the numbers entered is", average)


# 2. Write a program that generates a random number between 1 and 10 and asks the user to 
# guess the number. The program should give the user a hint and ask the user to guess again if 
# the user'/s guess is incorrect.
import random
number = random.randint(1, 10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Congratulations, you guessed the number!")
        break
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")


# 3. Write a program that asks the user to enter a series of words and prints the words in reverse 
# order. The program should stop asking for words when the user enters the word "done".
words = []
while True:
    word = input("Enter a word or type 'done': ")
    if word == "done":
        break
    words.append(word)
i = len(words) - 1
while i >= 0:
    print(words[i])
    i -= 1


# 4. Write a program that generates a random number between 1 and 100 and asks the user to 
# guess the number. The program should give the user a hint and ask the user to guess again if 
# the user's guess is incorrect. The program should keep track of the number of guesses the 
# user has made and print the number of guesses at the end.
import random
number = random.randint(1, 100)
guesses = 0
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1
    if guess == number:
        print("Congratulations, you guessed the number!")
        break
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
print("It took you", guesses, "guesses to guess the number.")


# 5. Write a program that asks the user to enter a series of numbers and prints the product of 
# the numbers entered. The program should stop asking for numbers when the user enters 
# the word "done".
product = 1
while True:
    num = input("Enter a number or type 'done': ")
    if num == "done":
        break
    try:
        num = int(num)
        product *= num
    except ValueError:
        print("Invalid input")
print("The product of the numbers entered is", product)


# 6. Write a program that asks the user to enter a password. The program should keep asking for 
# the password until the user enters the correct password. The correct password is "python".
password = ""
while password != "python":
    password = input("Enter the password: ")
print("Welcome to the system.")


# 7. Write a program that asks the user to enter a number and then prints the digits of the 
# number in reverse order. For example, if the user enters 1234, the program should print 4 3 
# 2 1.
num = int(input("Enter a number: "))
while num > 0:
    digit = num % 10
    print(digit, end=" ")
    num = num // 10


# 8. Write a program that asks the user to enter a series of numbers and prints the sum of the 
# even numbers entered. The program should stop asking for numbers when the user enters 
# the word "done".
sum = 0
while True:
    num = input("Enter a number or type 'done': ")
    if num == "done":
        break
    try:
        num = int(num)
        if num % 2 == 0:
            sum += num
    except ValueError:
        print("Invalid input")
print("The sum of the even numbers entered is", sum)


# 9. Write a program that generates a random number between 1 and 100 and asks the user to 
# guess the number. The program should give the user a hint and ask the user to guess again if 
# the user's guess is incorrect. The program should limit the number of guesses to 5.
import random
number = random.randint(1, 100)
guesses = 0
while guesses < 5:
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1
    if guess == number:
        print("Congratulations, you guessed the number!")
        break
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
if guesses == 5:
    print("You have used up all your guesses. The number was", number)



# 10. Write a program that asks the user to enter a word and then prints the word in reverse 
# order. For example, if the user enters "python", the program should print "nohtyp".
word = input("Enter a word: ")
i = len(word) - 1
while i >= 0:
    print(word[i], end="")
    i -= 1
    
    
# 1. Write a program that takes a positive integer n as input and prints the first n prime numbers. 
# A prime number is a number that is only divisible by 1 and itself.
n = int(input("Enter a positive integer: "))
count = 0
num = 2
while count < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1
    num += 1    

# 2. Write a program that takes a string as input and prints the frequency of each character in 
# the string.
string = input("Enter a string: ")
freq = {}
for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
for ch, count in freq.items():
    print(ch, ":", count)



# 3. Write a program that takes two integers a and b as input and computes a^b (i.e., a raised to 
# the power of b) using a while loop.
a = int(input("Enter the base: "))
b = int(input("Enter the exponent: "))
result = 1
while b > 0:
    result *= a
    b -= 1
print("The result is:", result)




# 4. Write a program that takes a list of numbers as input and prints the second smallest number 
# in the list.
nums = [int(num) for num in input("Enter a list of numbers: ").split()]
smallest = float("inf")
second_smallest = float("inf")
for num in nums:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest:
        second_smallest = num
print("The second smallest number is:", second_smallest)


# 5. Write a program that takes a list of integers as input and prints the sum of all the numbers in 
# the list.
nums = [int(num) for num in input("Enter a list of numbers: ").split()]
sum = 0
i = 0
while i < len(nums):
    sum += nums[i]
    i += 1
print("The sum of the numbers is:", sum)


# 6. Write a program that takes a list of integers as input and removes all the duplicates from the 
# list.
nums = [int(num) for num in input("Enter a list of numbers: ").split()]
unique_nums = []
for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)
print("The list with duplicates removed is:", unique_nums)


# 7. Write a program that takes a string as input and prints the string in title case (i.e., the first 
# letter of each word capitalized and the rest of the word in lowercase).
string = input("Enter a string: ")
words = string.split()
title_case = []
for word in words:
    title_case.append(word.capitalize())
print("The string in title case is:", " ".join(title_case))



# 1. Write a program that takes a list of integers as input and prints the largest subsequence of 
# increasing consecutive integers in the list.
nums = [int(num) for num in input("Enter a list of numbers: ").split()]
start = 0
end = 0
max_start = 0
max_end = 0
i = 1
while i < len(nums):
    if nums[i] > nums[i-1]:
        end = i
    else:
        if end - start > max_end - max_start:
            max_start = start
            max_end = end
        start = i
        end = i
    i += 1
if end - start > max_end - max_start:
    max_start = start
    max_end = end
print("The largest subsequence of increasing consecutive integers is:", nums[max_start:max_end+1])


# 2. Write a program that takes a list of integers as input and computes the average of the 
# numbers in the list.
nums = [int(num) for num in input("Enter a list of numbers: ").split()]
sum = 0
i = 0
while i < len(nums):
    sum += nums[i]
    i += 1
average = sum / len(nums)
print("The average of the numbers is:", average)


# 3. Write a program that takes a list of integers as input and prints the largest number in the list 
# that is not divisible by any of the other numbers in the list.
nums = [int(num) for num in input("Enter a list of numbers: ").split()]
largest = 0
for i in range(len(nums)):
    is_divisible = False
    for j in range(len(nums)):
        if i != j and nums[i] % nums[j] == 0:
            is_divisible = True
            break
        if not is_divisible and nums[i] > largest:
            largest = nums[i]
print("The largest number that is not divisible by any other number is:", largest)


# 4. Write a program that takes a positive integer n as input and prints the sum of the first n 
# even numbers.
n = int(input("Enter a positive integer: "))
sum = 0
num = 2
count = 0
while count < n:
    sum += num
    num += 2
    count += 1
print("The sum of the first", n, "even numbers is:", sum)


# 5. Write a program that takes a list of integers as input and prints the product of all the 
# numbers in the list.
nums = [int(num) for num in input("Enter a list of numbers: ").split()]
product = 1
i = 0
while i < len(nums):
    product *= nums[i]
    i += 1
print("The product of the numbers is:", product)


# 6. Write a program that takes a positive integer n as input and prints the first n terms of the 
# sequence 1, 2, 4, 7, 11, 16, 22, ... . Each term in the sequence is obtained by adding the 
# current term number to the previous term.
n = int(input("Enter a positive integer: "))
terms = [1]
i = 1
while len(terms) < n:
    terms.append(terms[-1] + i)
    i += 1
print("The first", n, "terms of the sequence are:", terms)


# 7. Write a program that takes a string as input and prints the string in reverse order.
string = input("Enter a string: ")
i = len(string) - 1
while i >= 0:
    print(string[i], end="")
    i -= 1
print()


# 8. Write a program that takes a list of integers as input and removes the largest number from 
# the list.
nums = [int(num) for num in input("Enter a list of numbers: ").split()]
largest = max(nums)
nums.remove(largest)
print("The list with the largest number removed is:", nums)



# 9. Write a program that takes a positive integer n as input and prints the nth term of the 
# sequence 1, 1, 2, 3, 5, 8, 13, ... . Each term in the sequence is obtained by adding the two 
# previous terms.
n = int(input("Enter a positive integer: "))
if n == 1 or n == 2:
    term = 1
else:
    prev1 = 1
    prev2 = 1
    i = 3
    while i <= n:
        term = prev1 + prev2
        prev2 = prev1
        prev1 = term
        i += 1
print("The", n, "th term of the sequence is:", term)

















# Functions تمرین های تابع
# 1) Write a function to calculate the area of a rectangle.
def rectangle_area(length, width):
    """
    Calculates the area of a rectangle given its length and width.
    Args:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    Returns:
    float: The area of the rectangle.
    """
    return length * width

# 10) Write a function to find the minimum value in a list.
def find_min(numbers):
    min_num = numbers[0] # set the first number in the list as the 
# minimum
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num




# 1) Write a function to find the sum of a list of numbers.
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total


# 2) Write a function to find the average of a list of numbers.
def avg_list(lst):
    return sum(lst) / len(lst)


# 3) Write a function to check if a number is prime.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 4) Write a function to find all prime numbers in a range.
def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# 5) Write a function to generate a random number between two 
# given numbers.
import random
def random_num(start, end):
    return random.randint(start, end)


# 6) Write a function to count the number of vowels in a string.
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count


# 7) Write a function to count the number of consonants in a string.
def count_consonants(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char.isalpha() and char.lower() not in vowels:
            count += 1
    return count


# 8) Write a function to remove all vowels from a string.
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return "".join([char for char in s if char not in vowels])


# 9) Write a function to remove all consonants from a string.
def remove_consonants(s):
    vowels = "aeiouAEIOU"
    return "".join([char for char in s if char not in vowels and 
char.isalpha()])


# 10) Write a function to check if a string is a pangram.
def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in s.lower():
            return False
    return True


# 1) Write a function to find the factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# 2) Write a function to check if a number is a perfect square.
def is_perfect_square(n):
    root = int(n ** 0.5)
    return root ** 2 == n



# 3) Write a function to find the square root of a number.
def square_root(n):
    return n ** 0.5


# 4) Write a function to find the cube root of a number.
def cube_root(n):
    return n ** (1/3)


# 5) Write a function to check if a number is a palindrome.
def is_palindrome(n):
    return str(n) == str(n)[::-1]


# 6) Write a function to convert a string to title case.
def title_case(s):
    return s.title()


# 7) Write a function to find the length of the hypotenuse of a rightangled triangle.
def hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5


# 8) Write a function to calculate the distance between two points.
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# 9) Write a function to calculate the slope of a line.
def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


# 10) Write a function to find the midpoint of a line.
def midpoint(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)



# 1) Write a function to calculate the volume of a cube.
def cube_volume(side):
    volume = side ** 3
    return volume


# 2) Write a function to calculate the volume of a sphere.
import math
def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume


# 3) Write a function to calculate the volume of a cylinder.
import math
def cylinder_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

# 4) Write a function to calculate the area of a triangle.
def triangle_area(base, height):
    area = 0.5 * base * height
    return area


# 5) Write a function to calculate the area of a trapezium.
def trapezium_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area


# 6) Write a function to calculate the area of a parallelogram.
def parallelogram_area(base, height):
    area = base * height
    return area


# 7) Write a function to calculate the perimeter of a triangle.
def triangle_perimeter(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter


# 8) Write a function to calculate the perimeter of a trapezium.
def trapezium_perimeter(side1, side2, side3, side4):
    perimeter = side1 + side2 + side3 + side4
    return perimeter


# 9) Write a function to calculate the perimeter of a parallelogram.
def parallelogram_perimeter(side1, side2):
    perimeter = 2 * (side1 + side2)
    return perimeter


# 10) Write a function to find the roots of a quadratic equation.
import cmath
def quadratic_roots(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    root1 = (-b - cmath.sqrt(delta)) / (2 * a)
    root2 = (-b + cmath.sqrt(delta)) / (2 * a)
    return root1, root2














# Math  تمرین های 

# 1) Find the absolute value of a number.
import math
number = -5
absolute_value = math.fabs(number)
print(absolute_value)


# 2) Calculate the square root of a number.
import math
number = 25
square_root = math.sqrt(number)
print(square_root)


# 3) Round a number up to the nearest integer.
import math
number = 4.6
rounded_up = math.ceil(number)
print(rounded_up)


# 4) Round a number down to the nearest integer.
import math
number = 4.6
rounded_down = math.floor(number)
print(rounded_down)


# 5) Calculate the sine of an angle in radians.
import math
angle_in_radians = math.pi/4
sine_value = math.sin(angle_in_radians)
print(sine_value)


# 6) Calculate the cosine of an angle in radians.
import math
angle_in_radians = math.pi/4
cosine_value = math.cos(angle_in_radians)
print(cosine_value)


# 7) Calculate the tangent of an angle in radians.
import math
angle_in_radians = math.pi/4
tangent_value = math.tan(angle_in_radians)
print(tangent_value)


# 8) Convert degrees to radians.
import math
angle_in_degrees = 45
angle_in_radians = math.radians(angle_in_degrees)
print(angle_in_radians)


# 9) Convert radians to degrees.
import math
angle_in_radians = math.pi/4
angle_in_degrees = math.degrees(angle_in_radians)
print(angle_in_degrees)


# 10) Find the smallest integer greater than or equal to a number.
import math
number = 4.6
smallest_integer = math.ceil(number)
print(smallest_integer)



# 1) Find the largest integer less than or equal to a number:
import math
num = 3.6
result = math.floor(num)
print(result)

# 2) Find the difference between two numbers:
num1 = 10
num2 = 5
result = num1 - num2
print(result)


# 3) Calculate the product of two numbers:
num1 = 5
num2 = 7
result = num1 * num2
print(result)


# 4) Calculate the quotient of two numbers:
num1 = 10
num2 = 5
result = num1 / num2
print(result)


# 5) Calculate the remainder of a division operation:
num1 = 10
num2 = 3
result = num1 % num2
print(result)


# 6) Find the greatest common divisor of two numbers:
import math
num1 = 24
num2 = 36
result = math.gcd(num1, num2)
print(result)


# 7) Find the least common multiple of two numbers:
import math
num1 = 3
num2 = 5
result = (num1 * num2) / math.gcd(num1, num2)
print(result)


# 8) Calculate the factorial of a number:
import math
num = 5
result = math.factorial(num)
print(result)


# 9) Generate a random number between 0 and 1:
import random
result = random.random()
print(result)


# 10) Generate a random integer within a range of numbers:
import random
result = random.randint(1, 10)
print(result)


# 1) Calculate the natural logarithm of a number.
import math
num = 10
ln_value = math.log(num)
print(ln_value)


# 2) Calculate the base 10 logarithm of a number.
import math
num = 100
log_value = math.log10(num)
print(log_value)


# 3) Calculate the exponential function of a number.
import math
num = 2
exp_value = math.exp(num)
print(exp_value)


# 4) Calculate the power of a number to a given exponent.
import math
num = 2
exponent = 3
power_value = math.pow(num, exponent)
print(power_value)


# 5) Calculate the arc cosine of a number.
import math
num = 0.5
acos_value = math.acos(num)
print(acos_value)


# 6) Calculate the arc sine of a number.
import math
num = 0.5
asin_value = math.asin(num)
print(asin_value)


# 7) Calculate the arc tangent of a number.
import math
num = 1
atan_value = math.atan(num)
print(atan_value)


# 8) Calculate the hyperbolic sine of a number.
import math
num = 2
sinh_value = math.sinh(num)
print(sinh_value)


# 9) Calculate the hyperbolic cosine of a number.
import math
num = 2
cosh_value = math.cosh(num)
print(cosh_value)


# 10) Calculate the hyperbolic tangent of a number.
import math
num = 2
tanh_value = math.tanh(num)
print(tanh_value)


# 1) Calculate the degrees of freedom for a t-test.
import math
n = 10
df = n - 1


# 2) Calculate the probability density function for a normal distribution.
import math
def normal_pdf(x, mu=0, sigma=1):
    return (1 / (math.sqrt(2 * math.pi) * sigma)) * math.exp(-(x - mu)**2 / (2 * sigma**2))
    


# 3) Calculate the cumulative distribution function for a normal distribution.
import math
def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


# 4) Calculate the inverse of the cumulative distribution function for a 
# normal distribution.
import math
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z, low_p = -10.0, 0
    hi_z, hi_p = 10.0, 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z


# 5) Calculate the standard deviation of a list of numbers.
import math
def standard_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean)**2 for x in numbers) / len(numbers)
    return math.sqrt(variance)
# 6) Calculate the variance of a list of numbers.
def variance(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean)**2 for x in numbers) / len(numbers)
    return variance


# 7) Find the maximum value in a list of numbers.
def max_value(numbers):
    return max(numbers)


# 8) Find the minimum value in a list of numbers.
def min_value(numbers):
    return min(numbers)


# 9) Sort a list of numbers in ascending order.
def sort_ascending(numbers):
    return sorted(numbers)


# 10) Sort a list of numbers in descending order.
def sort_descending(numbers):
    return sorted(numbers, reverse=True)















# Modules  تمرین های 



# 1) Using the math module and the sqrt() function:
import math
# Calculate the square root of 16
result = math.sqrt(16)
print(result) # Output: 4.0


# 2) Using the random module and the randint() function:
import random
# Generate a random number between 1 and 10
result = random.randint(1, 10)
print(result) # Output: random number between 1 and 10


# 3) Using the datetime module and the datetime() function:
import datetime
# Create a datetime object for today's date
today = datetime.datetime.today()
print(today) # Output: current date and time


# 4) Using the os module and the getcwd() function:
import os
# Print the current working directory
cwd = os.getcwd()
print(cwd) # Output: current working directory


# 5) Using the time module and the sleep() function:
import time
# Pause the program for 5 seconds
time.sleep(5)
print("5 seconds have passed") # Output: 5 seconds have passed


# 6) Using the calendar module and the month() function:
import calendar
# Print the calendar for the current month
cal = calendar.month(datetime.date.today().year, 
datetime.date.today().month)
print(cal) # Output: calendar for the current month


# 7) Using the statistics module and the mean() function:
import statistics
# Calculate the mean of a list of numbers
numbers = [1, 2, 3, 4, 5]
mean = statistics.mean(numbers)
print(mean) # Output: mean of the list of numbers


# 8) Using the re module and the search() function:
import re
# Find the first occurrence of a pattern in a string
string = "The quick brown fox jumps over the lazy dog"
pattern = "brown"
match = re.search(pattern, string)
print(match.group()) # Output: brown


# 9) Using the json module and the load() function:
import json
# Load JSON data from a file
with open("data.json") as f:
    data = json.load(f)
print(data) # Output: JSON data from file


# 10) Using the urllib module and the request() function:
import urllib.request
# Make an HTTP request to a website
url = "http://www.example.com"
response = urllib.request.urlopen(url)
print(response.read()) # Output: contents of the website





# 1) Using the csv module and the reader() function:
import csv
# Read data from a CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row) # Output: each row of the CSV file as a list


# 2) Using the gzip module and the compress() function:
import gzip
# Compress a string
data = b'hello world'
compressed_data = gzip.compress(data)
print(compressed_data) # Output: compressed data


# 3) Using the zipfile module and the ZipFile() class:
import zipfile
# Create a zip file containing multiple files
with zipfile.ZipFile('example.zip', 'w') as zip:
    zip.write('file1.txt')
    zip.write('file2.txt')
    zip.write('file3.txt')
print("Zip file created") # Output: Zip file created


# 4) Using the sys module and the argv variable:
import sys
# Get command line arguments
arguments = sys.argv
print(arguments) # Output: list of command line arguments


# 5) Using the itertools module and the product() function:
import itertools
# Get the cartesian product of two lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
product = list(itertools.product(list1, list2))
print(product) # Output: cartesian product of the two lists


# 6) Using the collections module and the Counter() class:
import collections
# Count the frequency of items in a list
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = collections.Counter(my_list)
print(counter) # Output: frequency of items in the list


# 7) Using the heapq module and the heapify() function:
import heapq
# Create a heap from a list
my_list = [4, 1, 3, 2, 5]
heapq.heapify(my_list)
print(my_list) # Output: heap created from the list


# 8) Using the bisect module and the bisect_left() function:
import bisect
# Find the insertion point for an item in a sorted list
my_list = [1, 3, 5, 7, 9]
insertion_point = bisect.bisect_left(my_list, 6)
print(insertion_point) # Output: index where 6 should be inserted  to maintain sorted order



# 9) Using the math module and the ceil() function:
import math
# Round up a number to the nearest integer
number = 4.3
rounded_number = math.ceil(number)
print(rounded_number) # Output: 5



# 10) Using the random module and the shuffle() function:
import random
# Randomly shuffle the items in a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list) # Output: shuffled list






# 1) Import the datetime module and use the timedelta function to create a 
# time difference of 1 hour.
import datetime
time_diff = datetime.timedelta(hours=1)



# 2) Import the os module and use the listdir function to list all files in a 
# directory.
import os
files = os.listdir('/path/to/directory')



# 3) Import the time module and use the strftime function to format a 
# datetime object as a string.
import time
now = time.time()
time_string = time.strftime('%Y-%m-%d %H:%M:%S', 
time.localtime(now))



# 4) Import the calendar module and use the isleap function to check if a 
# year is a leap year.
import calendar
year = 2022
is_leap_year = calendar.isleap(year)


# 5) Import the statistics module and use the median function to calculate 
# the median of a list of numbers.
import statistics
data = [1, 3, 5, 7, 9]
median = statistics.median(data)


# 6) Import the re module and use the sub function to replace a pattern in a 
# string with another string.
import re
text = 'Hello, World!'
new_text = re.sub('Hello', 'Hi', text)


# 7) Import the json module and use the dump function to write JSON data 
# to a file.
import json
data = {'name': 'John', 'age': 30}
with open('data.json', 'w') as f:
    json.dump(data, f)

# 8) Import the urllib module and use the parse function to parse a URL into 
# its components.
import urllib.parse
url = 'https://www.example.com/path/to/page?param=value'
parsed_url = urllib.parse.urlparse(url)
# 9) Import the csv module and use the writer function to write data to a CSV 
# file.
import csv
import csv
# data to be written to CSV file
data = [['Name', 'Age', 'Gender'],
    ['John', '25', 'Male'],
    ['Sarah', '32', 'Female'],
    ['Michael', '45', 'Male']]
# open file for writing
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # write data to file row by row
    for row in data:
        writer.writerow(row)




# 10) Import the gzip module and use the decompress function to 
# decompress a gzip-compressed string.
import gzip
# gzip-compressed data as bytes
compressed_data = b'\x1f\x8b\x08\x00\xce\xffB`\x02\xffs\xca\xccIU\x04\x00N\xc2\xf8W\x 03\x00\x00\x00'
# decompress the data
decompressed_data = gzip.decompress(compressed_data)
# convert bytes to string
decompressed_data_str = decompressed_data.decode('utf-8')
print(decompressed_data_str)






# 1) To extract a file from a zip archive using the zipfile module, you can 
# use the extract function.
import zipfile
with zipfile.ZipFile('example.zip', 'r') as zip_ref:
    zip_ref.extract('example_file.txt', 'extracted_files/')
# This will extract the file "example_file.txt" from the archive 
# "example.zip" to a new directory called "extracted_files".

# 2) To exit a Python program with an error code of 1 using the sys 
# module, you can use the exit function.
import sys
sys.exit(1)
# This will exit the program with an error code of 1.



# 3) To generate all permutations of a list of numbers using the itertools 
# module, you can use the permutations function.
import itertools
numbers = [1, 2, 3]
permutations = list(itertools.permutations(numbers))
print(permutations)
# This will generate all permutations of the list [1, 2, 3].


# 4) To create a dictionary with a default value of 0 using the collections 
# module, you can use the defaultdict class.
from collections import defaultdict
my_dict = defaultdict(int)
my_dict['key1'] += 1
print(my_dict)
# This will create a dictionary with a default value of 0 and increment 
# the value associated with the key 'key1'.


# 5) To remove the smallest item from a heap using the heapq module, 
# you can use the heappop function. 
import heapq
my_heap = [4, 2, 1, 3, 5]
heapq.heapify(my_heap)
smallest_item = heapq.heappop(my_heap)
print(smallest_item)
# This will remove the smallest item from the heap and print it.



# 6) To find the insertion point for an item in a sorted list using the bisect 
# module, you can use the bisect_right function. 
import bisect
my_list = [1, 3, 5, 7, 9]
insertion_point = bisect.bisect_right(my_list, 4)
print(insertion_point)
# This will find the insertion point for the value 4 in the sorted list [1, 3, 
# 5, 7, 9].


# 7) To round down a number to the nearest integer using the math 
# module, you can use the floor function. 
import math
x = 3.7
rounded_x = math.floor(x)
print(rounded_x)
# This will round the number 3.7 down to 3.



# 8) To randomly select an item from a list using the random module, you 
# can use the choice function. 
import random
my_list = ['apple', 'banana', 'cherry']
random_item = random.choice(my_list)
print(random_item)
# This will randomly select an item from the list ['apple', 'banana', 
# 'cherry'].




# 9) To format a datetime object as a string using a custom format using 
# the datetime module, you can use the strftime function. 
import datetime
now = datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)
# This will format the current date and time as a string in the format 
# "YYYY-MM-DD HH:MM:SS".


# 10) To create a new directory using the os module, using mkdir to 
# create new directory
import os
# Create a new directory
new_dir = 'new_directory'
os.mkdir(new_dir)
# Check if the directory was created
if os.path.exists(new_dir):
    print(f"{new_dir} was created successfully!")
else:
    print(f"Failed to create {new_dir}.")
# This code first imports the os module, which provides a number of 
# functions for interacting with the operating system. It then uses the 
# os.mkdir() function to create a new directory with the name 
# "new_directory"















# iterators  تمرین های 


# 1) Iterator that returns numbers from 0 to 9:
class NumbersIterator:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 10:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration
# Usage:
numbers_iter = NumbersIterator()
for number in numbers_iter:
    print(number)


# 2) Iterator that returns the first n Fibonacci numbers:
class FibonacciIterator:
    def __init__(self, n):
        self.current = 0
        self.next = 1
        self.count = 0
        self.max_count = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.max_count:
            result = self.current
            self.current, self.next = self.next, self.current + self.next
            self.count += 1
            return result
        else:
            raise StopIteration
# Usage:
fib_iter = FibonacciIterator(10)
for number in fib_iter:
    print(number)


# 3) Iterator that returns the squares of numbers from 0 to n:
class SquaresIterator:
    def __init__(self, n):
        self.current = 0
        self.max = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration
# Usage:
squares_iter = SquaresIterator(10)
for number in squares_iter:
    print(number)



# 4) Iterator that returns the cubes of numbers from 0 to n:
class CubesIterator:
    def __init__(self, n):
        self.current = 0
        self.max = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            result = self.current ** 3
            self.current += 1
            return result
        else:
            raise StopIteration
# Usage:
cubes_iter = CubesIterator(10)
for number in cubes_iter:
    print(number)
    
    
    
# 5) Iterator that returns only the even numbers from 0 to n:
class EvenNumbersIterator:
    def __init__(self, n):
        self.current = 0
        self.max = n

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.max:
            result = self.current
            self.current += 2
            if result % 2 == 0:
                return result
        raise StopIteration
# Usage:
even_iter = EvenNumbersIterator(10)
for number in even_iter:
    print(number)
    
    
    
    
# 6) Iterator that returns only the odd numbers from 0 to n:
class OddNumbersIterator:
    def __init__(self, n):
        self.current = 1
        self.max = n

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.max:
            result = self.current
            self.current += 2
            if result % 2 == 1:
                return result
        raise StopIteration
# Usage:
odd_iter = OddNumbersIterator(10)
for number in odd_iter:
    print(number)

    
    
    
# 7) Create an iterator that returns the prime numbers from 0 to n.
class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.current = 2
    def __iter__(self):
        return self
    def __next__(self):
        while self.current < self.n:
            is_prime = True
            for i in range(2, self.current):
                if self.current % i == 0:
                    is_prime = False
                    break
            if is_prime:
                result = self.current
                self.current += 1
                return result
            else:
                self.current += 1
        raise StopIteration
n = 20
prime_iterator = PrimeIterator(n)
for num in prime_iterator:
    print(num)
    


# 8) Create an iterator that returns all the factors of a given number.
class FactorIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        while self.current <= self.n:
            if self.n % self.current == 0:
                result = self.current
                self.current += 1
                return result
            else:
                self.current += 1
n = 12
factor_iterator = FactorIterator(n)
for num in factor_iterator:
    print(num)



# 9) Create an iterator that returns the first n powers of 2.
class PowerIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        else:
            result = 2 ** self.current
            self.current += 1
            return result
n = 5
power_iterator = PowerIterator(n)
for num in power_iterator:
    print(num)



# 10) Create an iterator that returns the first n powers of 3.
class PowerIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        else:
            result = 3 ** self.current
            self.current += 1
            return result
n = 5
power_iterator = PowerIterator(n)
for num in power_iterator:
    print(num)


    
# 1) Create an iterator that returns the first n powers of 10.
class PowersOfTen:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            result = 10 ** self.current
            self.current += 1
            return result
        else:
            raise StopIteration    
    
    
# 2) Create an iterator that returns the first n multiples of a given 
# number.
class Multiples:
    def __init__(self, num, n):
        self.num = num
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            result = self.num * self.current
            self.current += 1
            return result
        else:
            raise StopIteration
    

# 3) Create an iterator that returns the first n multiples of 2.
class MultiplesOfTwo:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            result = 2 * self.current
            self.current += 1
            return result
        else:
            raise StopIteration
    
    
    
# 4) Create an iterator that returns the first n multiples of 3.
class MultiplesOfThree:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            result = 3 * self.current
            self.current += 1
            return result
        else:
            raise StopIteration

    
# 5) Create an iterator that returns the first n multiples of 10.
class MultiplesOfTen:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            result = 10 * self.current
            self.current += 1
            return result
        else:
            raise StopIteration

    
    
# 1) Create an iterator that returns the cumulative sum of a 
# given list.
class CumulativeSumIterator:
    def __init__(self, lst):
        self.cumulative_sum = 0
        self.iterator = iter(lst)
    def __iter__(self):
        return self
    def __next__(self):
        value = next(self.iterator)
        self.cumulative_sum += value
        return self.cumulative_sum    
    
    
    
    
    
    
    
# 2) Create an iterator that returns only the unique elements of 
# a given list.
class UniqueElementsIterator:
    def __init__(self, lst):
        self.iterator = iter(lst)
        self.unique_set = set()
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            value = next(self.iterator)
            if value not in self.unique_set:
                self.unique_set.add(value)
                return value
            
            
            
# 4) Create an iterator that returns the running minimum of a 
# given list.
class RunningMinimumIterator:
    def __init__(self, lst):
        self.iterator = iter(lst)
        self.running_min = float('inf')
    def __iter__(self):
        return self
    def __next__(self):
        value = next(self.iterator)
        self.running_min = min(value, self.running_min)
        return self.running_min
    
    
    
    
    
    
# 7) Create an iterator that returns the first n permutations of a 
# given list.
import itertools
class NPermutationsIterator:
    def __init__(self, lst, n):
        self.iterator = itertools.permutations(lst)
        self.n = n
        self.count = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count == self.n:
            raise StopIteration
        self.count += 1
        return next(self.iterator)

















# lambda  تمرین های 

# 1) Create a lambda function that adds two numbers.
add = lambda x, y: x + y

# 2) Create a lambda function that multiplies two numbers.
multiply = lambda x, y: x * y


# 3) Create a lambda function that subtracts two numbers.
subtract = lambda x, y: x - y


# 4) Create a lambda function that divides two numbers.
divide = lambda x, y: x / y


# 5) Create a lambda function that returns the square of a number.
square = lambda x: x**2


# 6) Create a lambda function that returns the cube of a number.
cube = lambda x: x**3


# 7) Create a lambda function that checks if a number is even.
is_even = lambda x: x % 2 == 0


# 8) Create a lambda function that checks if a number is odd.
is_odd = lambda x: x % 2 != 0


# 9) Create a lambda function that returns the maximum of two 
# numbers.
maximum = lambda x, y: x if x > y else y


# 10) Create a lambda function that returns the minimum of two 
# numbers.
minimum = lambda x, y: x if x < y else y


# 1) Check if a number is prime:
is_prime = lambda num: all(num % i != 0 for i in range(2, int(num ** 0.5) 
+ 1)) and num > 1


# 2) Check if a string is a palindrome:
is_palindrome = lambda s: s == s[::-1]


# 3) Reverse a string:
reverse_string = lambda s: s[::-1]


# 4) Convert a string to uppercase:
to_uppercase = lambda s: s.upper()


# 5) Convert a string to lowercase:
to_lowercase = lambda s: s.lower()


# 6) Return the length of a string:
string_length = lambda s: len(s)


# 7) Return the first letter of a string:
first_letter = lambda s: s[0]


# 8) Return the last letter of a string:
last_letter = lambda s: s[-1]


# 9) Return the first n elements of a list:
first_n = lambda lst, n: lst[:n]


# 10) Return the last n elements of a list:
last_n = lambda lst, n: lst[-n:]


# 1) Check if a number is prime:
is_prime = lambda num: all(num % i != 0 for i in range(2, int(num ** 0.5) 
+ 1)) and num > 1


# 2) Check if a string is a palindrome:
is_palindrome = lambda s: s == s[::-1]


# 3) Reverse a string:
reverse_string = lambda s: s[::-1]


# 4) Convert a string to uppercase:
to_uppercase = lambda s: s.upper()


# 5) Convert a string to lowercase:
to_lowercase = lambda s: s.lower()


# 6) Return the length of a string:
string_length = lambda s: len(s)


# 7) Return the first letter of a string:
first_letter = lambda s: s[0]


# 8) Return the last letter of a string:
last_letter = lambda s: s[-1]


# 9) Return the first n elements of a list:
first_n = lambda lst, n: lst[:n]


# 10) Return the last n elements of a list:
last_n = lambda lst, n: lst[-n:]



# 1) Filter prime numbers from a list:
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, 
int(n**0.5)+1))
filter_prime = lambda lst: list(filter(is_prime, lst))


# 2) Filter palindrome strings from a list:
is_palindrome = lambda s: s == s[::-1]
filter_palindrome = lambda lst: list(filter(is_palindrome, lst))


# 3) Map a list of numbers to their squares:
square_map = lambda lst: list(map(lambda x: x**2, lst))


# 4) Map a list of numbers to their cubes:
cube_map = lambda lst: list(map(lambda x: x**3, lst))


# 5) Map a list of strings to their lengths:
length_map = lambda lst: list(map(lambda s: len(s), lst))


# 6) Reduce a list of numbers to their sum:
# sum_reduce = lambda lst: functools.reduce(lambda x, y:x+y, lst)


# 7) Reduce a list of numbers to their product:
# product_reduce = lambda lst: functools.reduce(lambda x, y:x*y, lst)


# 8) Find the factorial of a number:
factorial = lambda n: 1 if n == 0 else n * factorial(n-1)


# 9) Find the nth term of the Fibonacci sequence:
fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)



# 10) Find the nth prime number:
nth_prime = lambda n: next(x for x in itertools.count(2) if 
is_prime(x) and not (n := n-1))













# class objects تمرین های 




# 1) Create a Car class with a color attribute and a method to print the 
# color.
class Car:
    def __init__(self, color):
        self.color = color

    def print_color(self):
        print("The car's color is", self.color)


# 2) Create a Person class with a name attribute and a method to print 
# the name.
class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("The person's name is", self.name)


# 3) Create a Rectangle class with height and width attributes and a 
# method to calculate the area.
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width


# 4) Create a Circle class with a radius attribute and a method to 
# calculate the area.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)


# 5) Create a Dog class with a name attribute and a method to print 
# the name and bark.
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says woof!")



# 6) Create a Cat class with a name attribute and a method to print the 
# name and meow.
class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(self.name, "says meow!")


# 7) Create a Person class with name and age attributes and a method 
# to print the name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, "is", self.age, "years old.")


# 8) Create a Student class with name and major attributes and a 
# method to print the name and major.
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def print_info(self):
        print(self.name, "is majoring in", self.major)


# 9) Create a Book class with title and author attributes and a method 
# to print the title and author.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(self.title, "by", self.author)


# 10) Create a Movie class with title and director attributes and a 
# method to print the title and director.
class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director

    def print_info(self):
        print(self.title, "directed by", self.director)






# 1) Create a House class with address, bedrooms, and bathrooms attributes 
# and a method that prints out the house's address, number of bedrooms, 
# and number of bathrooms.
class House:
    def __init__(self, address, bedrooms, bathrooms):
        self.address = address
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
    def print_house_info(self):
        print("Address:", self.address)
        print("Number of bedrooms:", self.bedrooms)
        print("Number of bathrooms:", self.bathrooms)






# 2) Create a BankAccount class with a balance attribute and methods to 
# deposit, withdraw, and check the balance.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    def check_balance(self):
        print("Current balance:", self.balance)



# 3) Create a Person class with name and age attributes and methods to 
# change the person's name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def change_name(self, new_name):
        self.name = new_name
    def change_age(self, new_age):
        self.age = new_age



# 4) Create a Circle class with a radius attribute and methods to calculate the 
# area and circumference of the circle.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14 * self.radius ** 2
    def calculate_circumference(self):
        return 2 * 3.14 * self.radius





# 5) Create a Triangle class with base and height attributes and a method to 
# calculate the area of the triangle.
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def calculate_area(self):
        return 0.5 * self.base * self.height




# 6) Create a Square class with side attribute and methods to calculate the 
# area and perimeter of the square.
class Square:
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        return self.side ** 2
    def calculate_perimeter(self):
        return 4 * self.side



# 7) Create a Dog class with name and breed attributes and a method that 
# prints out the dog's name and breed.
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def print_info(self):
        print("Name:", self.name)
        print("Breed:", self.breed)






# 8) Create a Cat class with name and color attributes and a method that 
# prints out the cat's name and color.
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def print_info(self):
        print("Name:", self.name)
        print("Color:", self.color)




# 9) Create a Student class with name and gpa attributes and a method to 
# calculate the student's letter grade based on their GPA.
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    def calculate_letter_grade(self):
        if self.gpa >= 4.0:
            return "A+"
        elif self.gpa >= 3.7:
            return "A"
        elif self.gpa >= 3.3:
            return "A-"
        elif self.gpa >= 3.0:
            return "B+"
        elif self.gpa >= 2.7:
            return "B"
        elif self.gpa >= 2.3:
            return "B-"
        elif self.gpa >= 2.0:
            return "C+"
        elif self.gpa >= 1.7:
            return "C"
        elif self.gpa >= 1.3:
            return "C-"
        elif self.gpa >= 1.0:
            return "D"
        else:
            return "F"
# The Student class has name and gpa attributes. The 
# calculate_letter_grade method returns a letter grade based on the 
# student's GPA, using the standard 4.0 scale. The letter grades are 
# calculated as follows:
# A+: 4.0
# A: 3.7
# A-: 3.3
# B+: 3.0
# B: 2.7
# B-: 2.3
# C+: 2.0
# C: 1.7
# C-: 1.3
# D: 1.0
# F: 0.0
# To test the Student class, you can create a Student object and call the 
# calculate_letter_grade method:
# student = Student("Alice", 3.8)
# print(student.calculate_letter_grade()) # Output: AThis will output "A-", since a GPA of 3.8 corresponds to an A- grade.






# 10) Create a Bank class with a list of BankAccount objects and methods to 
# add and remove accounts and to print out the account with the highest 
# balance.
class Bank:
    def __init__(self):
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)
    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
        else:
            print("Account not found")
    def print_highest_balance(self):
        if len(self.accounts) == 0:
            print("No accounts found")
        else:
            highest_balance = max(account.balance for account in 
            self.accounts)
            for account in self.accounts:
                if account.balance == highest_balance:
                    print("Account with the highest balance:", account)
                    break


# The Bank class has a list of BankAccount objects as an attribute. The 
# add_account and remove_account methods allow you to add and 
# remove BankAccount objects from the list. The print_highest_balance 
# method finds the account with the highest balance and prints its 
# information. If there are no accounts in the list, it prints "No accounts 
# found".
# To test the Bank class, you can create some BankAccount objects and 
# add them to a Bank object:
account1 = BankAccount(1000)
account2 = BankAccount(5000)
account3 = BankAccount(2000)
bank = Bank()
bank.add_account(account1)
bank.add_account(account2)
bank.add_account(account3)
bank.print_highest_balance()
# This will output:
# Account with the highest balance: <__main__.BankAccount object at 
# 0x7f0f3a0d8d30>
# Note that the output shows the memory address of the BankAccount 
# object. If you want to print more information about the account, you can 
# add a __str__ method to the BankAccount class, for example:
# class BankAccount:
#  def __init__(self, balance):
#  self.balance = balance
#  def deposit(self, amount):
#  self.balance += amount
#  def withdraw(self, amount):
#  if amount <= self.balance:
#  self.balance -= amount
#  else:
#  print("Insufficient funds")
#  def check_balance(self):
#  print("Current balance:", self.balance)
#  def __str__(self):
#  return f"BankAccount(balance={self.balance})"
# Now if you run the test code again, it will output:
# Account with the highest balance: BankAccount(balance=5000)


















# class ادامه تمرین های کلاس
# 1) Create a Book class with title, author, and year attributes and methods 
# to change the book's title, author, and year.
# 2) Create a Movie class with title, director, and year attributes and 
# methods to change the movie's title, director, and year.
# 3) Create a House class with address, bedrooms, and bathrooms attributes 
# and methods to change the house's address, number of bedrooms, and 
# number of bathrooms.
# 4) Create a BankAccount class with a balance attribute and a method that 
# adds interest to the account balance.
# 5) Create a Person class with name and age attributes and a method to 
# check if the person is an adult (age >= 18).
# 6) Create a Rectangle class with height and width attributes and a method 
# to check if the rectangle is a square.
# 7) Create a Dog class with name, breed, and age attributes and a method 
# to calculate the dog's age in dog years (1 human year = 7 dog years).
# 8) Create a Cat class with name, color, and age attributes and a method to 
# calculate the cat's age in cat years (1 human year = 4 cat years).
# 9) Create a Bank class with a list of BankAccount objects and a method to 
# find the account with the lowest balance.
# 10) Create a Book class with title, author, and year attributes and a 
# method to check if the book was written before a given year



# class پاسخ تمرین های 

# 1) Book class:
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def set_title(self, title):
        self.title = title
    def set_author(self, author):
        self.author = author
    def set_year(self, year):
        self.year = year


# 2) Movie class:
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
    def set_title(self, title):
        self.title = title
    def set_director(self, director):
        self.director = director
    def set_year(self, year):
        self.year = year



# 3) House class:
class House:
    def __init__(self, address, bedrooms, bathrooms):
        self.address = address
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
    def set_address(self, address):
        self.address = address
    def set_bedrooms(self, bedrooms):
        self.bedrooms = bedrooms
    def set_bathrooms(self, bathrooms):
        self.bathrooms = bathrooms


# 4) BankAccount class:
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def add_interest(self, rate):
        self.balance += self.balance * rate


# 5) Person class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def is_adult(self):
        return self.age >= 18


# 6) Rectangle class:
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def is_square(self):
        return self.height == self.width



# 7) Dog class:
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    def dog_years(self):
        return self.age * 7
    
    
# 8) Cat class:
class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
    def cat_years(self):
        return self.age * 4


# 9) Bank class:
class Bank:
    def __init__(self, accounts):
        self.accounts = accounts
    def lowest_balance_account(self):
        if len(self.accounts) == 0:
            return None
        lowest_account = self.accounts[0]
        for account in self.accounts[1:]:
            if account.balance < lowest_account.balance:
                lowest_account = account
        return lowest_account


# 10) Book class:
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def is_written_before(self, year):
        return self.year < year




# 1) Movie class to check if the movie was released before a given year:
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
    def released_before_year(self, year):
        return self.year < year



# 2) House class to calculate the total square footage of the house:
class House:
    BEDROOM_AREA = 150
    BATHROOM_AREA = 50
    def __init__(self, address, bedrooms, bathrooms):
        self.address = address
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
    def total_square_footage(self):
        return self.bedrooms * House.BEDROOM_AREA + self.bathrooms * House.BATHROOM_AREA


# 3) Car class to calculate the car's average mileage per year:
class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
    def avg_mileage_per_year(self):
        current_year = 2023
        age = current_year - self.year
        return self.mileage / age if age > 0 else 0


# 4) Student class to calculate the student's average grade:
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def avg_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

# 5) Rectangle class to check if the rectangle is a square and to calculate the 
# diagonal length of the rectangle:
import math
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def is_square(self):
        return self.height == self.width
    def diagonal_length(self):
        return math.sqrt(self.height ** 2 + self.width ** 2)

# 6) BankAccount class with methods to deposit, withdraw, and transfer 
# money to another account:
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
    def transfer(self, amount, other_account):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            other_account.deposit(amount)



# 7) Person class with methods to change the person's name and age and to 
# print out the person's new name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def change_name(self, new_name):
        self.name = new_name
    def change_age(self, new_age):
        self.age = new_age
    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")



# 8) Dog class to check if the dog is a puppy (age < 1 year):
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    def is_puppy(self):
        return self.age < 1



# 9) Create a Cat class with name and color attributes and a method to check 
# if the cat is a kitten (age < 1 year).
class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def is_kitten(self):
        return self.age < 1


# 10) Create a Bank class with a list of BankAccount objects and 
# methods to find the account with the highest balance, the average 
# balance of all accounts, and the total number of accounts.
class Bank:
    def __init__(self):
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)
    def remove_account(self, account):
        self.accounts.remove(account)
    def highest_balance(self):
        return max(self.accounts, key=lambda account: account.balance)
    def average_balance(self):
        total_balance = sum(account.balance for account in self.accounts)
        return total_balance / len(self.accounts)
    def total_accounts(self):
        return len(self.accounts)















# General تمرین های 

# 1. Write a program that takes an input from the user and prints "Hello, [input]!"
input_name = input("What is your name? ")
print("Hello, " + input_name + "!")


# 2. Write a program that takes two numbers from the user and prints their sum. 
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
sum = num1 + num2
print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(sum))


# 3. Write a program that takes three numbers from the user and prints the largest of the three. 
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number is: " + str(largest))


# 4. Write a program that prints the first n Fibonacci numbers, where n is an input from the 
# user. 
n = int(input("Enter the number of Fibonacci numbers to generate: "))
def fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(n):
    print(fibonacci(i))
    
    
# 5. Write a program that prints all numbers from 1 to 100, but for multiples of 3, print "Fizz" 
# instead of the number, and for multiples of 5, print "Buzz". For numbers that are multiples of 
# both 3 and 5, print "FizzBuzz".
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
        
        
# 6. Write a program that checks if a given word, is a palindrome. 
def is_palindrome(word):
    return word == word[::-1]
word = input("Enter a word: ")
if is_palindrome(word):
    print(word + " is a palindrome.")
else:
    print(word + " is not a palindrome.")
    
    
# 7. Write a program that sorts a list of numbers in ascending order. 
def sort_numbers(numbers):
    numbers.sort()
    return numbers
numbers = [int(x) for x in input("Enter a list of numbers, separated by space: ").split()]
print("Sorted list:", sort_numbers(numbers))


# 8. Write a program that checks if a given number is prime. 
def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
# 9. Write a function that takes a list of numbers and returns the average. 
def find_average(numbers):
    return sum(numbers)/len(numbers)
numbers = [int(x) for x in numbers]
# 10. Write a program that calculates the factorial of a given number.
def find_factorial(num):
    if num == 0:
        return 1
    else:
        return num * find_factorial(num-1)
num = int(input("Enter a number: "))
print("The factorial of", num, "is", find_factorial(num))



# 1. Write a Python program to calculate the area of a circle given its radius. 
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("The area of the circle is:", area)


# 2. Write a Python program to print the sum of the first 10 natural numbers. 
n = 10
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum of the first 10 natural numbers is:", sum)
print("The sum of the first 10 natural numbers is:", sum)


# 3. Write a Python program to check whether a given number is even or odd. 
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")



# 4. Write a Python program to find the largest element in a list. 
list = [5, 10, 15, 20, 25, 30]
max = list[0]
for i in range(1, len(list)):
    if list[i] > max:
        max = list[i]
print("The largest element in the list is:", max)



# 5. Write a Python program to reverse a string. 
string = input("Enter a string: ")
reverse = ""
for i in range(len(string)-1, -1, -1):
    reverse += string[i]
print("The reverse of the string is:", reverse)



# 6. Write a Python program to check whether a given string is a palindrome. 
string = input("Enter a string: ")
reverse = ""
for i in range(len(string)-1, -1, -1):
    reverse += string[i]
if string == reverse:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")




# 7. Write a Python program to calculate the factorial of a given number. 
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num+1):
    factorial *= i
print("The factorial of", num, "is:", factorial)


# 8. Write a Python program to convert a Celsius temperature to Fahrenheit. 
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(celsius, "Celsius = ", fahrenheit, "Fahrenheit")



# 9. Write a Python program to generate a random number between 1 and 10. 
import random
num = random.randint(1, 10)
print("The random number is:", num)




# 10. Write a Python program to count the number of vowels in a given string.
string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = 0
for i in string:
    if i in vowels:
        count += 1
print("The number of vowels in the string is:", count)



# 1. Write a Python program to calculate the sum and average of a list of numbers. 
numbers = [3, 5, 7, 9, 11]
sum = 0
for i in numbers:
    sum += i
average = sum / len(numbers)
print("The sum of the numbers is:", sum)
print("The average of the numbers is:", average)




# 2. Write a Python program to find the second largest element in a list. 
n = 10
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum of the first 10 natural numbers is:", sum)
print("The sum of the first 10 natural numbers is:", sum)


# 3. Write a Python program to check whether a given year is a leap year or not. 
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# 4. Write a Python program to check whether a given number is a prime number or not. 
num = int(input("Enter a number: "))
prime = True
for i in range(2, num):
    if num % i == 0:
        prime = False
        break
if prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# 5. Write a Python program to sort a list of integers in ascending order. 
numbers = [3, 5, 2, 9, 8, 10]
numbers.sort()
print("The sorted list is:", numbers)


# 6. Write a Python program to check whether a given string is a pangram or not. 
string = input("Enter a string: ")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
pangram = True
for char in alphabet:
    if char not in string.lower():
        pangram = False
        break
if pangram:
    print(string, "is a pangram")
else:
    print(string, "is not a pangram")



# 7. Write a Python program to find the length of the longest word in a sentence. 
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
lengths = []
for word in words:
    lengths.append(len(word))
print("The length of the longest word in the sentence is:", max(lengths))


# 8. Write a Python program to calculate the sum of the digits in a number. 
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print("The sum of the digits in the number is:", sum)



# 9. Write a Python program to generate a Fibonacci series up to n. 
n = int(input("Enter the number of terms: "))
fibonacci = [0, 1]
for i in range(2, n):
    next = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next)
print("The Fibonacci series is:", fibonacci)



# 10. Write a Python program to remove duplicates from a list.
numbers = [3, 5, 2, 9, 8, 10, 5, 2]
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
print("The list with duplicates removed is:", unique)


# 1. Write a Python function that takes a list of integers as input and returns a new list containing 
# only the even numbers.
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]
# example usage:
nums = [1, 2, 3, 4, 5, 6, 7, 8]
even_nums = even_numbers(nums)
print(even_nums) # Output: [2, 4, 6, 8]



# 2. Write a Python function that takes two dictionaries as input and returns a new dictionary 
# that contains only the key-value pairs that are present in both input dictionaries.
def intersect_dicts(dict1, dict2):
    return {key: value for key, value in dict1.items() if key in dict2 and dict2[key] == value}
# example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 3, 'd': 4}
intersected = intersect_dicts(dict1, dict2)
print(intersected) # Output: {'a': 1}



# 3. Write a Python function that takes a string as input and returns the most common letter in 
# the string.
def most_common_letter(string):
    letter_counts = {}
    for letter in string:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    most_common = max(letter_counts, key=letter_counts.get)
    return most_common
# example usage:
text = "The quick brown fox jumps over the lazy dog"
common_letter = most_common_letter(text)
print(common_letter) # Output: 'o'


# 4. Write a Python function that takes a list of tuples as input, where each tuple contains a 
# name and an age, and returns a list of names of people who are over a certain age.
def over_age(name_age_list, age):
    return [name for name, age_ in name_age_list if age_ > age]
# example usage:
people = [('Alice', 25), ('Bob', 35), ('Charlie', 20), ('David', 40)]
over_30 = over_age(people, 30)
print(over_30) # Output: ['Bob', 'David']


# 5. Write a Python function that takes a list of numbers as input and returns the two numbers in 
# the list that add up to a specific target.
def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
# example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result) # Output: [0, 1]



# 6. Write a Python function that takes a list of strings as input and returns a new list that contains 
# only the strings that have at least one uppercase letter.
def uppercase_strings(lst):
    return [string for string in lst if any(letter.isupper() for letter in string)]
# example usage:
strings = ['hello', 'WORLD', 'Python', 'is', 'FUN']
uppercase_strings = uppercase_strings(strings)
print(uppercase_strings) # Output: ['WORLD', 'Python', 'FUN']


# 7. Write a Python function that takes a list of integers as input and returns a new list that 
# contains the differences between adjacent elements in the input list.
def adjacent_differences(lst):
    return [lst[i+1] - lst[i] for i in range(len(lst)-1)]
# example usage:
nums = [3, 6, 9, 12, 15]
differences = adjacent_differences(nums)
print(differences) # Output: [3, 3, 3, 3]



# 8. Write a Python class Circle that represents a circle with a given radius. The class should have 
# methods to calculate the circle's area and circumference.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2
    def circumference(self):
        return 2 * 3.14159 * self.radius
# example usage:
my_circle = Circle(5)
print(my_circle.area()) # Output: 78.53975
print(my_circle.circumference()) # Output: 31.4159


# 9. Write a Python function that takes a list of dictionaries as input, where each dictionary 
# represents a person and has keys 'name' and 'age', and returns a new list of names sorted by 
# age in ascending order.
def sort_names_by_age(people):
    return [person['name'] for person in sorted(people, key=lambda x: x['age'])]
# example usage:
people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 35}, {'name': 'Charlie', 'age': 20}]
sorted_names = sort_names_by_age(people)
print(sorted_names) # Output: ['Charlie', 'Alice', 'Bob']


# 10. Write a Python function that takes a list of integers as input and returns a new list that 
# contains only the elements that appear more than once in the input list.
def repeated_elements(lst):
    return list(set([num for num in lst if lst.count(num) > 1]))
# example usage:
nums = [1, 2, 3, 2, 4, 3, 5, 6, 5]
repeated = repeated_elements(nums)
print(repeated) # Output: [2, 3, 5]
