#1. radius of a circle and return the area of the circle
import math
def area_of_circle(radius):
    area = math.pi * radius ** 2
    return area
radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
print(f"The area of the circle with radius {radius} is: {area}")

#2. function to accept three numbers and returns the largest of the three numbers.
def largest_of_three(num1, num2, num3):
    largest = max(num1, num2, num3)
    return largest
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
largest = largest_of_three(num1, num2, num3)
print(f"The largest of the three numbers is: {largest}")

#3. function that takes a string and returns its length without using the built-in len() function.
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count
input_string = input("Enter a string: ")
length = string_length(input_string)
print(f"The length of the string is: {length}")

#4. function that checks whether a given number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

#5. recursive function to find the nth Fibonacci number.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the position of the Fibonacci number you want to find: "))
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")

#6. recursive function to reverse a string.




#7. program to find the sum of all numbers from 1 to n using for loop.
def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n = int(input("Enter a number: "))
print(f"The sum of all numbers from 1 to {n} is: {sum_of_numbers(n)}")

#8. program to count how many even numbers are present in a list. 
def count_even_numbers(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count
numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
even_count = count_even_numbers(numbers)
print(f"The number of even numbers in the list is: {even_count}")

#9. program to print all prime numbers between 1 and 100.
def print_prime_numbers():
    for num in range(2, 101):
        if is_prime(num):
            print(num, end=' ')
print("Prime numbers between 1 and 100 are:")
print_prime_numbers()




