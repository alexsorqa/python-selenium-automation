"""Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order."""

def digitize(n):
    n = str(n)
    new = [int(i) for i in n]
    return new[::-1]