number=int(input("Enter a number"))
def factorial(num):
    input=num
    if( num==0 or num==1):
        return 1
    else:
        return ( num * factorial (num -1))
print("The factorial of the number",number,"is",factorial(number))