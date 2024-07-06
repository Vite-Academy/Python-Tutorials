# <--- Interview question --->
# This question has 4 conditions that must be met:
# 1. If the input is divisible by 3, the function will return the string "fizz"
# 2. If the input is divisible by 5 it will return "Buzz"
# 3. If the input is divisible by both 3 and 5 it will return "FizzBuzz"
# 4. For any other number it will return the same input

# <--- Solution --->

def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return 'FizzBuzz'
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return 'Buzz'
    return input

print(fizz_buzz(15)) # FizzBuzz
print(fizz_buzz(9)) # Fizz
print(fizz_buzz(25)) # Buzz
print(fizz_buzz(17)) # 17


# Video tutorials [eng]:
# 1. Programming with Mosh: https://www.youtube.com/watch?v=z3-XFI_nXNM
# 2. Wrt Tech: https://www.youtube.com/watch?v=whbXCE7UPjY