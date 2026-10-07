# #add 2 no.s entered by the user
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
print("sum:",a+b)

#find difference between 2 numbers
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
print("difference:",a-b)

# #multiply 3 numbers
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
print("product:",a*b*c)

#divide 1 no. by another
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
print(a/b)

#Write a program to calculate the square of a number. 
num = int(input("Enter a number: "))
square = num*num   #(num**2)
print("Square =", square)

#Write a program to calculate the cube of a number. 
a=int(input("Enter a number: "))
cube = num ** 3 #(num*num*num)
print("Cube =", cube)

#Write a program to calculate the average of three numbers. 
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
avg=(a+b+c)/3
print("average:",avg)

#program to calculate the total price of 5 notebooks if the price of one notebook is entered by the user. 
price=int(input("enter pice of one notebook:"))
b=price*5
print("total price of 5 notebooks:", b)

#program to find the quotient and remainder when one integer is divided by another. 
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
print("quotient:",a/b)
print("remainder:",a%b)

#A shop has 47 chocolates. If each box holds 6 chocolates, calculate: ● The number of completely filled boxes. ● The number of chocolates left over. 
chocolates=47
box=6
filled_boxes = chocolates // box
left_over = chocolates % box
print("filled boxes:" ,filled_boxes)
print("Chocolates left over =", left_over)

#pgm to convert a given number of minutes into complete hours and remaining minutes.
minutes=int(input("enter minutes:"))
hours=minutes//60
remaining_minutes=minutes%60
print("Hours =", hours)
print("Remaining =",remaining_minutes)

#convert 367 sec into minutes and remaining seconds
seconds = 367
minutes=seconds//60
remaining_seconds=seconds%60
print("Minutes =", minutes)
print("Remzining Seconds=",remaining_seconds)

#teacher wants to distribute 53 students into groups of 8.calculate the no. of complete groups and the student left over.
students=53
group=8
complete_groups=students//group
students_left=students%group
print("complete groups =", complete_groups)
print("Students left =",students_left)

#extract the last digit of a positive integer using the modulus operator
num = int(input("Enter a positive integer: "))
last_digit = num%10
print("Last digit =",last_digit)

# remove the last digit of a +ve intger using floor division
num = int(input("Enter a positive integer: "))
result = num//10
print("Number after removing last digit =", result)

#shopping bill:customer buys 3 pens=15rs each & 2 notebooks=40rs each.total bill?
pens = 3*15
notebooks = 2*40
total = pens + notebooks
print("Total bill = RS", total)

#salary calculation: an employee earns rs800 per day. calculate their salary for 26 working days
daily_salary= 800
working_days = 26
salary = daily_salary * working_days
print("salary =Rs",salary)

#distance conversion: convert a distance given in kms into meters and cms
km=float(input("Enter distance in Km"))
meters = km * 1000
centimeters = km * 100000 #1km=1000m 1meter = 100cm  1km=1000*100 = 100,000cm
print("Meters =", meters)
print("Centimeters =", centimeters)

#Rectangle: Accept the length and width of a rectangle & calculate its area and perimeter
length = float(input("Enter the length: "))
width = float(input("Enter width: "))
area = length* width
perimeter = 2 * (length + width)
print("Area =",area)
print("perimeter =",perimeter)

#Simple Interest: Accept the principal amount, annual interest rate and time in years. SI=(PRT)/100
P = float(input("Enter principal amount: "))
R = float(input("Enter annual interest rate: "))
T = float(input("Enter time in years: "))
SI = (P*R*T)/100
print("Simple Interest =", SI)

#Bill sharing:Accept a restaurant bill & the no. of friends.calculate how much each friend should pay if the bill is shared equality 
bill=float(input("Enter restaurant bill: "))
friends = int(input("Enter number of friends: "))
each_person = bill/friends
print("Each friend should pay =",each_person)

#Travel calculation:a car travels 180km using 12litres of fuel.calculate its mileage in km per liter.
distance = 180
fuel = 12 
mileage=distance/fuel
print("Mileage =", mileage, "km/l")

#unit price: accept the total price of a packet of rice and its weight in kilograms.calculate price per kg
price = float(input("Enter total price: "))
weight = float(input("Enter weight in kg: "))
price_per_kg = price / weight
print("Price per kg =", price_per_kg)

#time conversion:Accept a total number of hours and convert it into complete days and remaining hours.
hours = int(input("Enter total hours: "))
days = hours//24
remaining_hours=hours%24
print("complete days =",days)
print("Remaining hours =",remaining_hours)

#power calculation:accept a number and an exponent,then calculate the result using the ** operator
num = int(input("Enter a number: "))
expo = int(input("Enter a exponent: "))
power_calculation = num**expo
print("Result =",power_calculation)