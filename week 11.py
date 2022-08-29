#Write a program to demonstrate else clause, finally with try except.
# try
# except
# else
# finally
# def divide(x,y):
#     try:
#         z=x//y
#     except ZeroDivisionError:#if specific error will occur in try then except executes
#         print("you are dividing by 0")
#     except Exception as a: # if any unknown error will occur then this will execute
#         print(a)
#
#     else:   #if there will be no error in try block then else will be executed
#         print("your result is",z)
#     finally: # it will be executed every time
#         print("function executed")
#
# divide(10,0)

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




