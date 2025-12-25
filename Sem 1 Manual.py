# Convert Celsius to Fahrenheit
temperature = float(input("please enter temperture in Celsius:"))   # Fahrenheit
Fahrenheit = (temperature * 9/5)+32     # -32) *5/9
print("temperature in Fahrenheit:",Fahrenheit)  # Celsius:",Celsius)

# Odd $ Even check
num = int(input("Enter any Number to test whether it is odd or even:"))
if(num % 2)== 0:
    print("Number is Even")
else:
    print("Number is Odd")

# Largest Number
a= int(input("Enter 1st number"))
b= float(input("Enter 2nd number"))
c= int(input("Enter 3rd number"))
largest =0
if a>b and a>c:
    largest= a
if b>a and b>c:
    largest= b
if c>b and c>a:
    largest= c
print(largest, "is the Largest number.")

# Program to check if a number is prime or not
num = int(input("Enter a Number"))

flag = False
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
