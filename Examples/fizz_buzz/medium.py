# <--- Interview question --->
#  FizzBuzz Problem: Write a program that prints the numbers from 1 to 100. But 
#  for multiples of three print "Fizz" instead of the number and for the 
#  multiples of five print "Buzz".  For numbers which are multiples of both 
#  three and five print "FizzBuzz".
#  
#  Multiples of 3: 3, 6, 9, 12, 15*, ...
#
#  Multiples of 5: 5, 10, 15*, 20, 25, ...
#
#  Some numbers like 15 are multiples of both 3 and 5.
#
#  If we divide 3 by a number and there is no remainder that number is a multiple 
#  of 3.  Finding a multiple of 5 (or any other number) works the same way.
#
#  FizzBuzz Sequence...
#
#  1
#  2
#  Fizz
#  4
#  Buzz
#  Fizz
#  7
#  8
#  Fizz
#  Buzz
#  11
#  Fizz
#  13
#  14
#  FizzBuzz
#  16
#  ...


# <--- Solution --->

for n in range(1,101):
  if (n % 3 == 0 and n % 5 == 0):
    print("FizzBuzz")
  elif (n % 3 == 0):
    print("Fizz")
  elif (n % 5 == 0):
    print("Buzz")
  else:
    print(n)


# Video tutorials [eng]:
# 1. Portfolio Courses: https://www.youtube.com/watch?v=4pJzmDbqN7U