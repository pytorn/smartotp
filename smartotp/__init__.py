__version__ = '0.0.1'

from functions import *


def otp():
    otp_functions = Generate()
    numbers = otp_functions.generate_palindrome()
    return numbers[random.randint(0,len(numbers))]
