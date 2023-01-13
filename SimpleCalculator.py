"""Language: Python 2.7.18"""

"""Takes two numbers and a sign to calculate the answer."""
def calculator(first_number,sign,second_number):
    if sign=="+":
        return first_number+second_number
    elif sign=="-":
        return first_number-second_number
    elif sign=="*":
        return first_number*second_number
    elif sign=="/":
        return first_number/second_number
    else:
        print "invalid sign"

"""Prints the answer"""
print calculator(int(input("Enter an integar: ")),raw_input("Enter sign: "),int(input("Enter an integar: ")))
