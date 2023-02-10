num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))
if num1>num2 and num1>num3:
    greatestInt=num1
    if num2>num3:
        smallestInt=num3
    else:
        smallestInt=num2
if num2>num1 and num2>num3:
    greatestInt=num2
    if num1>num3:
        smallestInt=num3
    else:
        smallestInt=num1
if num3>num2 and num3>num1:
    greatestInt=num3
    if num2>num1:
        smallestInt=num1
    else:
        smallestInt=num2
print("Greatest number",greatestInt,"\nSmallest number", smallestInt)


