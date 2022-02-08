import operator as op
def zero():
    return 0
def one(): #your code here
    return 1
def two():
    return 2
def three():
    return 3
def four():
    return 4
def five(f = None):
	if f is None:
		return 5
	else:
		return f(5)
def six():
    return 6
def seven():
    return 7
def eight():
    return 8
def nine():
    return 9

def plus():
    return '+'
def minus():
    return '-'
def times(number):
    return lambda x: x * number()
def divided_by():
    return '/'

print(five(times(five())))