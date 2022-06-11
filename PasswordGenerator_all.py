""" Password Generator using Python """
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}!@#$%&*():/-"
length = 16

""" len(lower) == 4
len(upper) == 4
len(numbers) == 4
len(symbols) == 4 """

allPass = lower + upper + numbers + symbols
password = ' '.join(random.sample(allPass, length))

print("Your 16 digit password generated is : " + password)
