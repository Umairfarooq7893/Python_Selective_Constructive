##### WAP to find the sum of first n natural numbers using "for loop":(input("Enter a number: "))
n1 = int(input("Enter a number:"))
sum = 0
for el in range(1,n1+1):
    sum += el
print("Sum of first",n1,"natural numbers is: ", sum)

## WAP to find the sum of first n natural numberss using "while loop":
n2 = int(input("Enter a number:"))
sum = 0
i = 1
while i <= n2:
    sum += i
    i += 1
    print("sum of first",n2,"natural numbers is:",sum)    # following loop syntax
print("sum of pehlai",n2,"natural numbers ha:",sum)       # pinting the final sum ,outside the loop


##### WAP to find the factorial of first n natural numbers using "while loop":
n3 = int(input("Enter a number :"))
fact = 1
i    = 1
while i <= n3:
    fact *= i
    i += 1
    print("factorial of",n3,"is:",fact)   # following loop syntax
print("factorial of",n3,"ha:",fact)       # printing the final factorial, outside the loop


##WAP to find the factorail of first n natural numbers using "for loop":
n4 = int(input("Enter a number:"))
fact = 1
for el in range(1,n4+1):
    fact *= el
    print("factorial of",n4,"is:",fact)   # following loop syntax
print("factorial of",n4,"ha:",fact)       # printing the final factorial, outside the loop





