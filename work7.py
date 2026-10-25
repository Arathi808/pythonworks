# 1. Student Marks 
# ○ Ask the user to enter marks of 5 students into a list. 
# ○ Print the list.
# ○ Find and print the highest and lowest marks.
# ○ Count how many students scored above 50. 

marks=[]  #empty list to store the marks

for i in range(5): # 1. Ask the user for 5 marks using a loop
    mark=int(input("Enter marks of students: "))
    marks.append(mark)
print("Mark List: ",marks)

highest_mark=max(marks)
lowest_mark=min(marks)
print(f"Highest mark: {highest_mark}")  #print("Highest Mark:", max(marks))
print(f"Lowest mark: {lowest_mark}")   #print("Lowest Mark:", min(marks))

count=0  # Count how many students scored above 50
for mark in marks:
    if mark>50:
        count+=1
print("Students scoring above 50:", count)

# 2. Even and Odd Numbers 
# ○ Ask the user to enter 10 numbers. 
# ○ Store them in a list. 
# ○ Create two separate lists: one for even numbers and one for odd numbers. 
# ○ Print both lists. 

numbers=[]  
for i in range(10): 
    number=int(input("enter 10 numbers: "))
    numbers.append(number)  
print("Numbers:",numbers)   
list1=[]   
for number in numbers: 
    if number%2==0: 
        list1.append(number)  
list2=[] 
for number in numbers:   
    if number%2!=0:   
        list2.append(number) 
print(f"even numbers: {list1}")
print(f"odd numbers: {list2}")

# 3. Positive, Negative and Zero 
# ○ Ask the user to enter 10 numbers. 
# ○ Store them in a list. 
# ○ Count how many are positive, negative and zero. 

numbers=[]
for i in range(10):
    number=int(input("enter 10 numbers:"))  
    numbers.append(number) 
print("numbers:", numbers)  
 
pos_count = 0
neg_count = 0
zero_count = 0
for num in numbers: 
    if num>0:  
        pos_count+=1 
    elif num<0:
        neg_count+=1
    else:
        zero_count += 1
print("positive numbers count:",pos_count) 
print("negative numbers count: ",neg_count)
print("zeroes count:",zero_count)

# 4. Search an Element 
# ○ Ask the user to enter 5 numbers. 
# ○ Ask for another number to search. 
# ○ Check whether the number exists in the list. 
# ○ If it exists, display its position.

list=[]
for i in range(5):
    number=int(input("enter 5 numbers: "))
    list.append(number)
print("numbers:",list)
search_num=int(input("enter the number to be searched: "))

if search_num in list:
    print("number is in the list at position",list.index(search_num))
else:
    print("number not in the list")


# my_list = []

# for i in range(5):
#     number = int(input("enter 5 numbers: "))
#     my_list.append(number)

# print("numbers:", my_list)
# search_num = int(input("enter the number to be searched: "))

# if search_num in my_list:
#     # Find all positions using enumerate
#     positions = []
#     for i, num in enumerate(my_list):
#         if num == search_num:
#             positions.append(i)
            
#     print("number is in the list at positions:", positions)
# else:
#     print("number not in the list")

# 5. Shopping Cart 
# ○ Ask the user how many products they want to add. 
# ○ Enter the price of each product and store them in a list. 
# ○ Calculate the total. 
# ○ If the total is above ₹5000, give a 10% discount. 
# ○ Display the final amount. 

prices=[]
product=int(input("how many products you want to add: "))

for i in range(product):
    price=int(input("enter the price of the products: "))
    prices.append(price)

total=sum(prices)
print("Total price:", total)
if total>5000:
    discount = total * 0.10
    final_amount=total-discount
    print("You got a 10% discount!")
    print("Final amount to pay:", final_amount)
else:
    print("Final amount to pay:", total)

# 6. Number Analyzer 
# ○ Ask the user to enter 10 numbers. 
# ○ Store them in a list. 
# ○ Display: 
# ■ Sum 
# ■ Average 
# ■ Largest number 
# ■ Smallest number 
# ■ Number of even numbers 
# ■ Number of odd numbers
number=[]
for i in range(10):
    enter=int(input("enter 10 numbers:"))
    number.append(enter)
print("Entered numbers: ",number)
print("sum: ",sum(number))
print("Average:",sum(number)/len(number))
print("Largest number: ",max(number))
print("smallest number: ",min(number))
even_count=0
even=[]
for num in number:
    if num%2==0:
        even.append(num)
        even_count+=1
print("even numbers: ",even)
odd_count=0
odd=[]
for num in number:
    if num%2!=0:
        odd.append(num)
        odd_count+=1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)


#if zeroes is included
# zeros = []

# for num in number:
#     if num == 0:
#         zeros.append(num)
#         zero_count += 1
#     elif num % 2 == 0:
#         even.append(num)
#         even_count += 1
#     else:
#         odd.append(num)
#         odd_count += 1

# 7. Remove Negative Numbers 
# ○ Ask the user to enter numbers into a list. 
# ○ Create a new list containing only positive numbers. 
# ○ Display both lists
list1=[]

numbers=int(input("how many numbers :"))
for num in range(numbers):
    number=int(input("enter the numbers:"))
    list1.append(number)

print("entered numbers: ",list1)

positive=[]
for num in list1:
    if num > 0:
        positive.append(num)
             
if positive:
    print("positive numbers:", positive)
else:
    print("no positive numbers")

# 8. Find Duplicate Values 
# ○ Ask the user to enter 10 numbers. 
# ○ Find which numbers occur more than once. 
# ○ Display the duplicate numbers. 
# Example: 
# Input: 10 20 10 30 40 20 50 
# Output: 10 20

list1=[]
for i in range(10):
    numbers=int(input("enter the numbers: "))
    list1.append(numbers)
print("Entered numbers: ",list1)
duplicates=[]
for num in list1:
    if list1.count(num)>1 and num not in duplicates:  #When you use .count(num) on a list like [10, 20, 10, 20], Python checks the entire list every single time.When the loop hits the first 10, Python sees it appears twice, so it adds 10 to your duplicates list.But when the loop reaches the second 10 later on, Python checks it again, sees it appears twice, and would add 10 a second time!
        duplicates.append(num)
print("Duplicate numbers: ", duplicates)

# 9. Write a Python program to check whether a given number is a palindrome.  
# Hint: 121 → reversed: 121 → Palindrome  
# original = int(input("Enter a number: "))
# temp = original
# reversed_num = 0

# Loop to reverse the number mathematically
# while temp > 0:
#     digit = temp % 10                      # Step 1: Grab the last digit
#     reversed_num = reversed_num * 10 + digit # Step 2: Add it to our reversed number
#     temp = temp // 10                      # Step 3: Chop off the last digit

# # Check if the original matches the reversed version
# if original == reversed_num:
#     print(original, "is a palindrome! 🎉")
# else:
#     print(original, "is not a palindrome.")

user_input = input("Enter a number: ")

# Reverse the string using slicing [::-1]
reversed_input = user_input[::-1]

# Check if the original matches the reversed version
if user_input == reversed_input:
    print(user_input, "is a palindrome!")
else:
    print(user_input, "is not a palindrome.")

# 10. Write a Python program to check whether a given number is an Armstrong number.  
# Hint: 153 → 1³ + 5³ + 3³ = 153 → Armstrong 

n = int(input("Enter a number: "))
temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** 3
    n = n // 10

if sum == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")  #temp = n saves the original number. n % 10 gets the last digit.digit ** 3 calculates the cube of the digit.sum = sum + digit ** 3 adds the cubes.n // 10 removes the last digit.Finally, compare sum with temp.

# 11. Write a Python program to check whether a given number is a prime number.  
# Hint: 7 → factors: 1, 7 → Prime 

n = int(input("Enter a number: "))

if n <= 1:
    print("Not a prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")


# 12. Write a Python program to find the largest digit in a given number.  
# Hint: 5832 → Largest digit: 

n = int(input("Enter a number: "))
largest = 0

while n > 0:
    digit = n % 10

    if digit > largest:
        largest = digit

    n = n // 10

print("Largest digit:", largest)

