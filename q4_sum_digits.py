num1 = int(input("Enter a number:"))
total = 0
while num1 > 0:
    digit = num1 % 10
    total = total + digit
    num1 = num1//10
print("The total sum of digits is:", total)
