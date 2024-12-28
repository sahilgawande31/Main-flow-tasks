# 1. Sum of two integers

def sum_of_two_integers(a, b):
    return a + b
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

result = sum_of_two_integers(num1, num2)
print("The sum of the two integers is:", result)

# 2. Even or Odd

def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))

result = odd_or_even(num)
print(f"The number {num} is {result}.")

# 3. Factorial calculation

import math

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial not defined for negative numbers.")
else:
    print(f"The factorial of {num} is: {math.factorial(num)}")

#4. Function to generate the Fibonacci sequence
def fibonacci_sequence(n):
    if n <= 0:
        return []  
    elif n == 1:
        return [0]  
    elif n == 2:
        return [0, 1]  

    fib = [0, 1]  
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])  
    return fib


num = int(input("Enter the number of Fibonacci numbers to generate: "))

print(f"The first {num} numbers in the Fibonacci sequence are: {fibonacci_sequence(num)}")


#5. Function to reverse a string using a loop
def reverse_string_loop(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

input_string = input("Enter a string: ")

print("Reversed string (using loop):", reverse_string_loop(input_string))


#6. Function to check if a string is a palindrome
def is_palindrome(s):
    
    s = s.replace(" ", "").lower()
    return s == s[::-1]  


input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#7. Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

input_year = int(input("Enter a year: "))

if is_leap_year(input_year):
    print(f"{input_year} is a leap year.")
else:
    print(f"{input_year} is not a leap year.")

#8. Function to check if a number is an Armstrong number
def is_armstrong(number):
    digits = str(number)
    num_digits = len(digits)
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    return armstrong_sum == number

input_number = int(input("Enter a number: "))

if is_armstrong(input_number):
    print(f"{input_number} is an Armstrong number.")
else:
    print(f"{input_number} is not an Armstrong number.")

# main problem 

# Function to encrypt a message
def encrypt_message(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            encrypted_message += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_message += char  
    return encrypted_message

def decrypt_message(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            decrypted_message += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted_message += char 
    return decrypted_message

# Main program to handle continuous operations
def main():
    saved_message = None  
    while True:
        choice = input("Enter '1' to Encrypt, '2' to Decrypt, or 'q' to quit: ")

        if choice == "1":
            message = input("Enter message to encrypt: ")
            key = int(input("Enter key (number): "))
            saved_message = encrypt_message(message, key)
            print("Encrypted message:", saved_message)
        elif choice == "2":
            if saved_message:
                key = int(input("Enter key (number): "))
                print("Decrypted message:", decrypt_message(saved_message, key))
            else:
                print("No message available to decrypt. Please encrypt a message first.")
        elif choice.lower() == 'q':
            print("Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice! Please enter '1', '2', or 'q'.")

if __name__ == "__main__":
    main()
