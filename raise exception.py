#Write a basic program to demonstrate raise exceptions.

def divide(x,y):
    if type(x) != int or type(y) != int:
        raise TypeError("only int are allowed")
    elif y==0:
        raise Exception("divisor cannot be less that zero")
    else:
        z=x//y
        print("result is ",z)

divide('a',0)