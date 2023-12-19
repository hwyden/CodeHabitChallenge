# DESCRIPTION:
'''
Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.
'''

# SOLUTION
import re

def is_digit(n):
    return bool(re.match(r'\A\d\Z', str(n)))