# Exercise 1: Traffic Light Simulator 
# Write a program that takes a light color string ("red", "yellow", or "green") as input.
# If the color is "red", print "Stop".
# If the color is "yellow", print "Slow down".
# If the color is "green", print "Go".
# If it is anything else, print "Invalid color".

color=input("Enter traffic light color (red yelow or green): ").strip().lower()
if color=="red":
    print("Stop")
elif color=="yellow":
    print("Slow down")
elif color=="green":
    print("green")
else:
    print("Invalid color")

# Exercise 2: Even or Odd? 
# Write a program that asks the user for a whole number.Print "Even" if the number is even.Print "Odd" if the number is odd.
# Hint: Use the modulo operator %. A number is even if number % 2 == 0.

num=int(input("Enter a whole number: "))
if num%2==0: #even
    # num%2!=0: #odd
    print("Even number")
else:
    print("odd number")

# Basic If-Else Questions

# 1. Write a program that checks if a number is positive, negative, or zero.
num=int(input("enter a number: "))
if num>0:
    print("positive number")
elif num<0:
    print("Negative number")
else:
    print("zero")

# 2. Check if a given number is even or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Determine if a user is eligible to vote (age >= 18).
age=int(input("enter your age: "))
if(age>=18):
    print("eligible to vote")
else:
    print("Not Eligible")

# 4. Write a program that takes a temperature input and prints "Cold" if it's below 20°C, "Warm" if between 20-30°C, and "Hot" if above 30°C.
temp=float(input("Enter the temperature: "))
if temp>30:
    print("Hot")
elif temp>=20 and temp<=30:  #elif 20 <= temp <= 30:
    print("warm")
else:
    print("cold")

# 5. Check if a given year is a leap year.

# Divisible by 4   → Leap Year
# Divisible by 100 → Not Leap Year
# Divisible by 400 → Leap Year again

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

# Nested If Questions
# 6. Take input for marks and print grades as per the following:
#    - 90+ → A
#    - 80-89 → B
#    - 70-79 → C
#    - 60-69 → D
#    - Below 60 → F
mark = int(input("Enter marks: "))
if mark>=90:
    print("Grade A")
else:
    if mark>=80:
        print("Grade B")
    else:
        if mark>=70:
            print("Grade C")
        else:
            if mark >= 60:
                print("Grade D")
            else:
                print("Grade F")
     


# 7. Write a program to check if a number is positive and even; otherwise, print "Not positive or not even."
num=int(input("enter the number: "))
if num>0:
    if num%2==0:
        print("Positive and even")
    else:
        print("Not positive or not even")
else:
    print("Not positive or not even")


# 8. Given three numbers, find the largest number among them.
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))

if a>b:
    if a>c:
        print("Largest number =",a)
    else:
        print("Largest number =", c)
else:
    if b>c:
        print("Largest number=",b)
    else:
        print("Largest number=",c)
       

# If-Elif-Else Questions
# 9. A shop gives discounts based on purchase amount:
#    - Above ₹5000 → 20% discount
#    - ₹2000-₹5000 → 10% discount
#    - Below ₹2000 → No discount
#    Write a program to calculate the final bill amount.

amount=float(input("Enter the purchase amount: "))
if amount>5000:
    discount = amount * 20/100 
    print("discount: ",discount)
elif amount>=2000 and amount<=5000:
    discount = amount *10/100
    print(discount)
elif amount<2000:
    discount= 0
    print("no discount")
final_bill=amount-discount
print(final_bill,"is the final amount")

# 10. Convert a numerical day (1-7) into its corresponding weekday name (1 → Monday, 2 → Tuesday, etc.).
day=int(input("enter a day number(1 to 7): "))
if day==1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number")

# *For Loop Questions*
# 1. Print numbers from 1 to 10 using a `for` loop.
for n in range(1,11):
    print(n)

# 2. Print the multiplication table of a given number.
num=int(input("enter the number: "))
for i in range(1,11):
    print(num, "*", i,"=",num*i)

# 3. Find the sum of all numbers from 1 to `n`.
n=int(input("enter n: "))  
sum=0
for i in range(1,n+1):
    sum+=i
    print("Sum =",sum)

# print the first n fibonacci numbers
n = int(input("Enter n: "))

a = 0
b = 1
count = 0

while count < n:
    print(a)
    c = a + b
    a = b
    b = c
    count += 1

# 5. Print a pattern like:
   
#    *
#    **
#    *
#    **
for i in range(2):
    print("*")
    print("**")
   
# 6. Reverse a string using a loop.
string=input("enter a string")
reverse=""
for ch in string:
    reverse=ch + reverse
    print("Reversed string:", reverse)

# 7. Print all even numbers from 1 to 50.
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")

# for i in range(2, 51, 2):
#     print(i, end=" ")

# *While Loop Questions*
# 8. Print numbers from `n` to 1 using a `while` loop.
n = int(input("Enter a number: "))
while n>=1:
    print(n)
    n-=1
    
# 9. Find the factorial of a number using a `while` loop.
num = int(input("Enter a number: "))

fact = 1
i = 1

while i <= num:
    fact = fact * i
    i += 1

print("Factorial =", fact)

# 10. Print all digits of a number separately.
# num = input("Enter a number: ")
# i = 0
# while i < len(num):
#     print(num[i])
#     i += 1

num = int(input("Enter a number: "))

while num > 0:
    digit = num % 10
    print(digit)
    num //= 10

# 11. Count the number of digits in a given number.
num = int(input("Enter a number: "))
count=0
while num>0:
    count+=1
    num=num//10
print("Number of digits = ",count)

# 12. Keep taking user input until they enter "exit".
text=""
while text != "exit":
    text=input("Enter something").lower()
    print("Program ended")

# *Loop Control Statements*
# 13. Use `break` to stop the loop when a number is found in a list.
nums = [10, 20, 30, 40, 50]
for n in nums:
    if n==30:
        print("found")
        break

# 14. Use `continue` to skip printing even numbers from 1 to 20.
for i in range(1,21):
    if i %2==0:
        continue
    print(i)

# 15. Use `pass` inside a loop without affecting its flow.
for i in range(1,4):
    if i==3:
        pass
    print(i)

# *Match Statements*

# 1. *Day classifier*: Take a number 1-7 and print the weekday. Use `case 6|7` for weekend.
day=int(input("enter day number: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6|7:
        print("weekend")
    case _:
        print("Invalid day")



# 2. *Simple calculator*: Input `a, b, op` where op is `+ - * /`. Use `match op` to pick the operation.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
match op:
    case "+":
        print("Result =", a+b)
    case "-":
        print("Result =", a-b)
    case "*":
        print("Result =", a * b)
    case "/":
        print("Result =", a / b)
    case _:
        print("Invalid operator")

# 3. *Grade checker*: Input marks 0-100. `case 90 | 91 | ... | 100` → A, `case 80..89` → B, etc. Use guards like `case x if x >= 90`.
marks=int(input("Enter marks: "))
match marks:
    case x if x>=90:
        print("Grade A")
    case x if x >= 80:
        print("Grade B")
    case x if x >= 70:
        print("Grade C")
    case x if x >= 60:
        print("Grade D")
    case x if x >= 0:
        print("Grade F")
    case _:
        print("Invalid marks")

# 4. *HTTP status handler*: Input status code. `case 200` → OK, `case 404` → Not Found, `case 500..599` → Server Error, `case x if x >= 400` → Client Error.
status = int(input("Enter status code: "))
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case x if x>=500 and x<=599:   #case x if 500 <= x <= 599:
        print("Server Errorr")
    case x if x >= 400:
        print("Client Error")
    case _:
        print("Unknown Status")

# 5. *Chess board color*: You just did 1/0 board. Now input `row, col` and `match (row%2, col%2)` to print if that square is white/black.
row = int(input("Enter row: "))
col = int(input("Enter column: "))
match (row % 2, col % 2):
    case (0,0)| (1,1):
        print("Black")
    case (1,0)|(0,1):
        print("White")
    case _:
        print("Invalid")

# 6. *Command parser*: Input a list like `["add", 5, 3]` or `["quit"]`. `match cmd` where `case ["add", a, b]`, `case ["quit"]`, `case _` for invalid.
cmd=["add",5,3]

match cmd:
    case["add",a,b]:
        print("Sum =",a+b)
    case ["quit"]:
        print("Exiting..")
    case _ :
        print("Invalid Command")

# 7. *File type checker*: Input filename `"photo.jpg"`. Split by `.` then `match parts` → `case [name, "jpg" | "png"]` → Image, `case [name, "py"]` → Python file.
filename = input("Enter filename: ")
parts = filename.split(".")
match parts:
    case [name,"jpg"|"png"]:
        print("Image file")
    case [name, "py"]:
        print("Python File")
    case _:
        print("Unknown File")

# 8. *Shape area calculator*: Input tuple like `("circle", 5)` or `("rect", 4, 3)`. `match shape` with destructuring to calculate area.
shape=("circle",5)

match shape:
    case ("circle",r):
        area= 3.14 * r * r
        print("Area =",area)
    case ("rect",l,b):
        area=l*b
        print("Area =",area)
    case _:
        print("Invalid shape")