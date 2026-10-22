# 1. Find the Largest Element numbers = [10, 5, 25, 8, 15]
# numbers=[10,5,25,8,15]
# largest=numbers[0]
# for number in numbers:
#     if number > largest:
#         largest=number
# print("Largest number is:",largest)

# Find the Smallest Element numbers = [10, 5, 25, 8, 15]
# numbers=[10,8,25,5,15]
# smallest=numbers[0]
# for number in numbers:
#     if number<smallest:
#         smallest=number
# print(f"smallest number is {smallest}")

# 3. Find Sum of All Elements numbers = [1, 2, 3, 4, 5] 
# numbers=[1,2,3,4,5]
# sum=0
# for num in numbers:
#     sum+=num
# print("sum:",sum)

# 4. Find Average of Elements numbers = [10, 20, 30, 40, 50] 
# numbers=[10,20,30,40,50]
# sum=0
# n=len(numbers)
# for num in numbers:
#     sum+=num
# average=sum/n
# print("Average:",average)

# 5. Reverse a List Without Using reverse() 
numbers = [1, 2, 3, 4, 5] 
# print(numbers[::-1])
reverse=[]
# for num in numbers:
#     reverse.insert(0,num)
# print(reverse)

# Logic-Based List Questions 
# 1. Remove Duplicates 
# numbers = [1, 2, 2, 3, 4, 4, 5]
# list=[]
# for num in numbers:
#     if num not in list:
#         list.append(num)
# print(list)

# 2. Find Second Largest Number numbers = [10, 20, 50, 40, 30] 
numbers=[10,20,50,40,30]
numbers.sort()
print("second largest number:",numbers[-2])

# 3. Separate Even and Odd Numbers numbers = [1, 2, 3, 4, 5, 6] 
# numbers=[1,2,3,4,5,6]
# even=[]
# odd=[]
# for num in numbers:
#     if num%2==0:
#         even.append(num)
#     else:
#         odd.append(num)
# print("even numbers:",even)
# print("odd numbers:",odd)

# 4. Find Common Elements Between Two Lists list1 = [1, 2, 3, 4, 5] list2 = [3, 4, 5, 6, 7] 
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# common=[]
# for num in list1:
#     if num in list2:
#         common.append(num)
# print("common elements: ",common)

# 5. Merge Two Lists Without Duplicates list1 = [1, 2, 3] list2 = [3, 4, 5] 
list1 = [1, 2, 3] 
list2 = [3, 4, 5] 
merge=[]
for num in list1:
    if num not in merge:
        merge.append(num)
for num in list2:
    if num not in merge:
        merge.append(num)
print("merged list:",merge)

# Sum of All Elements in a Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total_sum=0
for row in matrix:
    for element in row:
        total_sum+=element
print("Sum of all elements:", total_sum)

# . Find Largest Element in Matrix
matrix = [[1, 2, 3], [10, 5, 6], [7, 8, 9]]  
                        
largest = matrix[0][0] # Assume the first element is the largest initially

for row in matrix:
  for element in row:
    if element > largest:
      largest = element

print("Largest element:", largest)