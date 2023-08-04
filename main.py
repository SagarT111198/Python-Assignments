#  create one empty list add prime no to list 50

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_primes_up_to(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


limit = 50
prime_numbers = find_primes_up_to(limit)

print(prime_numbers)


# Print user input table
num = int(input("Enter a number: "))

print("Multiplication Table for {num}:")
for i in range(1, 11):
    result = num * i
    print(f"{num} * {i} = {result}")


#  Print palindrome string taking input as string
def is_palindrome(s):
    return s == s[::-1]


user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# Take input as string and reverse it

user_input = input("Enter a string: ")

reversed_string = user_input[::-1]

print("Reversed string:", reversed_string)


