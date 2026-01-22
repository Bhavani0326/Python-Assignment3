def factorial(num):

    if(num>0):
        fact=num*factorial(num-1)
        return fact
    else:
        return 1
   
num=int(input("Enter a number:"))

print(f"Factorial of {num} is:",factorial(num))

 