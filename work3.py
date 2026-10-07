# 1. Student Grade Calculator 
# A college wants to automatically assign grades based on a student's marks:
# ● 90–100 → A+ ● 80–89 → A ● 70–79 → B ● 60–69 → C ● 50–59 → D ● Below 50 → Fail 
# Accept the student's mark and display the appropriate grade. 

mark = float(input("Enter the student's mark: "))
if mark >= 90 and mark <= 100:
    print("Grade: A+")
elif mark >= 80 and mark < 90:
    print("Grade: A")
elif mark >= 70 and mark < 80:
    print("Grade: B")   
elif mark >= 60 and mark < 70:
    print("Grade: C")
elif mark >= 50 and mark < 60:
    print("Grade: D")
else:
    print("Grade: Fail")

# 2. ATM Withdrawal System An ATM should process a withdrawal request.
# ● If the requested amount is greater than the account balance → display Insufficient Balance 
# ● If the amount is not a multiple of ₹100 → display Enter an amount in multiples of ₹100
# ● Otherwise → display Withdrawal Successful Accept the account balance and withdrawal amount. 

balance = float(input("Enter your account balance: "))
withdrawal_amount = float(input("Enter the withdrawal amount: "))
if withdrawal_amount > balance:
    print("Insufficient Balance")   
elif withdrawal_amount % 100 != 0:
    print("Enter an amount in multiples of ₹100")
else:
    print("Withdrawal Successful. Remaining Balance: ₹", balance)

# 3. Online Shopping Delivery Charge
# An e-commerce website calculates delivery charges based on the order value: 
# ● ₹5,000 or more → Free delivery ● ₹2,000–₹4,999 → ₹50 delivery charge ● Below ₹2,000 → ₹100 delivery charge 
# Calculate and display the delivery charge and final payable amount. 

order_value = float(input("Enter the order value: "))
if order_value >= 5000:
    delivery_charge = 0
    print("Free delivery")
elif order_value >= 2000:
    delivery_charge = 50
    print("Delivery charge: ₹50")
else:
    delivery_charge = 100
    print("Delivery charge: ₹100")

final_payable = order_value + delivery_charge
print("Final payable amount: ₹", final_payable)

# 4. Employee Performance Rating 
# A company rates employees based on their performance score: 
# ● 90 or above → Excellent ● 75–89 → Very Good ● 60–74 → Good ● 40–59 → Needs Improvement ● Below 40 → Poor
# Accept the performance score and display the rating. 

performance_score = float(input("Enter the employee's performance score: "))
if performance_score >= 90:
    print("Rating: Excellent")  
elif performance_score >= 75:
    print("Rating: Very Good")
elif performance_score >= 60:
    print("Rating: Good")
elif performance_score >= 40:
    print("Rating: Needs Improvement")
else:
    print("Rating: Poor")

# 5. Electricity Bill Calculator An electricity provider charges according to usage: 
# ● First 100 units → ₹2/unit ● Next 100 units → ₹3/unit ● Next 200 units → ₹5/unit ● Above 400 units → ₹7/unit 
# Accept the number of units consumed and calculate the total electricity bill. 

units_consumed = float(input("Enter the number of units consumed: "))
if units_consumed <= 100:
    bill = units_consumed * 2
elif units_consumed <= 200:
    bill = (100 * 2) + ((units_consumed - 100) * 3)
elif units_consumed <= 400:
    bill = (100 * 2) + (100 * 3) + ((units_consumed - 200) * 5)
else:
    bill = (100 * 2) + (100 * 3) + (200 * 5) + ((units_consumed - 400) * 7)

print("Total electricity bill: ₹", bill)


# 6. Movie Ticket Pricing A cinema determines ticket prices based on age:
# ● Below 5 → Free ● 5–12 → ₹100 ● 13–59 → ₹200 ● 60 or above → ₹120
# Accept the customer's age and display the ticket price.
age = int(input("Enter age: "))

if age < 5:
    print("Ticket Price: Free")
elif age <= 12:
    print("Ticket Price: ₹100")
elif age <= 59:
    print("Ticket Price: ₹200")
else:
    print("Ticket Price: ₹120")



# 7. Traffic Fine System A traffic department calculates fines based on vehicle speed.
# ● Up to 60 km/h → No fine ● 61–80 km/h → ₹500 ● 81–100 km/h → ₹1,000 ● Above 100 km/h → ₹2,000 and License Review 
# Accept the vehicle speed and display the appropriate result. 

speed = int(input("Enter vehicle speed: "))

if speed <= 60:
    print("No fine")
elif speed <= 80:
    print("Fine: ₹500")
elif speed <= 100:
    print("Fine: ₹1000")
else:
    print("Fine: ₹2000")
    print("License Review")

# 8. Restaurant Billing System A restaurant provides discounts based on the total bill: 
# ● ₹5,000 or above → 20% discount ● ₹3,000–₹4,999 → 15% discount ● ₹1,000–₹2,999 → 10% discount ● Below ₹1,000 → No discount
# Calculate the discount and final bill amount. 
bill=float(input("Enter the total bill amount: "))
if bill >= 5000:
    discount = bill * 20 / 100
elif bill >= 3000:
    discount = bill * 15 / 100
elif bill >= 1000:
    discount = bill * 10 / 100
else:
    discount = 0

final_bill = bill - discount

print("Discount:", discount)
print("Final bill:", final_bill)


# 9. College Admission Decision A college evaluates applicants based on their entrance examination score.
# ● 90+ → Direct Admission ● 75–89 → Admission + Interview ● 60–74 → Waitlisted ● Below 60 → Not Eligible 
# Accept the entrance score and display the admission status. 

score=int(input("Enter the entrance score: "))
if score >= 90:
    print("Direct Admission")
elif score >= 75:
    print("Admission + Interview")
elif score >= 60:
    print("Waitlisted")
else:
    print("Not Eligible")


# 10. Bank Loan Risk Category A bank categorizes applicants based on their credit score:
# ● 750 or above → Low Risk ● 650–749 → Medium Risk ● 550–649 → High Risk ● Below 550 → Very High Risk Additionally, 
# if the applicant has an existing loan default, display Loan Approval Requires Manual Review, regardless of the score. 

score=int(input("Enter the credit score: "))
defaulted=input("Has the applicant defaulted on a loan before? (yes/no): ").strip().lower()
if defaulted == "yes":
    print("Loan Approval Requires Manual Review")
else:
    if score>=650 and score<750:
        print("Medium Risk")
    elif score>=550 and score<650:
        print("High Risk")
    else:
        print("Very High Risk")


# 11. Hotel Room Pricing A hotel charges different prices depending on the room type:
# ● Standard → ₹2,000/night ● Deluxe → ₹3,500/night ● Suite → ₹5,000/night 
# If the customer stays for more than 5 nights, provide a 10% discount on the total room cost.
#     Accept room type and number of nights and calculate the final bill.
room=input("Enter room type:")
nights=int(input("Enter number of nights:"))
if room == "Standard":
        price = 2000
elif room == "Deluxe":
    price = 3500
elif room == "Suite":
    price = 5000
else:
    price = 0
    print("Invalid room type")

total = price * nights

if nights > 5:
    discount = total * 10 / 100
else:
    discount = 0

final_bill = total - discount

print("Final bill:", final_bill)


# 12. Employee Bonus Calculator A company calculates annual bonuses based on performance: 
# ● Performance ≥ 90 → 20% of annual salary ● Performance 75–89 → 15% ● Performance 60–74 → 10% ● Below 60 → No bonus 
# Accept annual salary and performance score and calculate the bonus. 

salary = float(input("Enter annual salary: "))
performance = int(input("Enter performance score: "))

if performance >= 90:
    bonus = salary * 20 / 100
elif performance >= 75:
    bonus = salary * 15 / 100
elif performance >= 60:
    bonus = salary * 10 / 100
else:
    bonus = 0

print("Bonus:", bonus)


# 13. Mobile Data Plan A telecom provider recommends a plan based on monthly data usage: 
# ● Below 5 GB → Basic Plan – ₹199 ● 5–20 GB → Standard Plan – ₹399 ● 21–50 GB → Premium Plan – ₹699 ● Above 50 GB → Unlimited Plan – ₹999 
# Accept the customer's monthly data requirement and recommend a plan. 

data = float(input("Enter monthly data usage in GB: "))

if data < 5:
    print("Basic Plan - ₹199")
elif data <= 20:
    print("Standard Plan - ₹399")
elif data <= 50:
    print("Premium Plan - ₹699")
else:
    print("Unlimited Plan - ₹999")

# 14. Parking Fee Calculator A parking facility charges according to parking duration:
# ● Up to 2 hours → ₹30 ● 3–5 hours → ₹50 ● 6–10 hours → ₹100 ● More than 10 hours → ₹150 
# If the vehicle is an electric vehicle, apply a 20% discount. Calculate the final parking fee.

hours = int(input("Enter parking duration in hours: "))
ev = input("Is it an electric vehicle? (yes/no): ")

if hours <= 2:
    fee = 30
elif hours <= 5:
    fee = 50
elif hours <= 10:
    fee = 100
else:
    fee = 150

if ev == "yes":
    fee = fee - (fee * 20 / 100)

print("Final parking fee:", fee)

# 15. Online Exam Result A student must satisfy both conditions to pass:
# ● Theory mark ≥ 40 ● Practical mark ≥ 40 If both are passed, calculate the average: ● Average ≥ 75 → Distinction ● Average ≥ 60 → First Class ● Average ≥ 50 → Second Class ● Otherwise → Pass If either subject is below 40, display Fail.

theory = int(input("Enter theory mark: "))
practical = int(input("Enter practical mark: "))
if theory >= 40 and practical >= 40:
    average = (theory + practical) / 2
    if average >= 75:
        print("Distinction")
    elif average >= 60:
        print("First Class")
    elif average >= 50:
        print("Second Class")
    else:
        print("Pass")
else:
    print("Fail")

#  16. Flight Baggage Fee An airline allows 15 kg of free baggage. 
# ● Up to 15 kg → No extra charge ● 16–20 kg → ₹500 ● 21–30 kg → ₹1,000 ● Above 30 kg → ₹2,000
# If the passenger is travelling in Business Class, the free baggage limit is 25 kg. 
# Calculate the applicable baggage charge.

baggage = float(input("Enter baggage weight: "))
class_type = input("Enter class (Economy/Business): ")

if class_type == "Business":
    limit = 25
else:
    limit = 15

if baggage <= limit:
    charge = 0
elif baggage <= 20:
    charge = 500
elif baggage <= 30:
    charge = 1000
else:
    charge = 2000

print("Baggage charge:", charge)


# 17. E-Commerce Return Eligibility An online store evaluates return requests. A product can be returned if: 
# ● It was purchased within 7 days, ● The product is unused, ● The product is returnable. I
# f all conditions are satisfied → Return Approved. Otherwise, display the appropriate reason for rejection.

days = int(input("Enter number of days since purchase: "))
unused = input("Is the product unused? (yes/no): ")
returnable = input("Is the product returnable? (yes/no): ")

if days > 7:
    print("Return Rejected: Purchased more than 7 days ago")
elif unused != "yes":
    print("Return Rejected: Product is used")
elif returnable != "yes":
    print("Return Rejected: Product is not returnable")
else:
    print("Return Approved")

# 18. Salary Tax Calculator A simplified tax system uses the following annual income slabs:
# ● Up to ₹3 lakh → No tax ● ₹3–6 lakh → 5% ● ₹6–10 lakh → 10% ● Above ₹10 lakh → 20% 
# Accept the annual salary and calculate the tax amount and final salary after tax. 
salary = float(input("Enter annual salary: "))

if salary <= 300000:
    tax = 0
elif salary <= 600000:
    tax = salary * 5 / 100
elif salary <= 1000000:
    tax = salary * 10 / 100
else:
    tax = salary * 20 / 100

final_salary = salary - tax

print("Tax:", tax)
print("Final salary:", final_salary)


# 19. Ride Fare Calculator A ride-sharing application calculates fares based on distance:
# ● First 5 km → ₹100 ● 6–15 km → ₹15/km ● 16–30 km → ₹12/km ● Above 30 km → ₹10/km
# If the ride is booked during peak hours, an additional 20% surcharge is applied. 
# Calculate the final fare.
distance=float(input("Enter the distance of the ride in km: "))
peak_hours = input("Is it peak hours? (yes/no): ").strip().lower()
    
if distance <= 5:
    fare = 100
elif distance <= 15:
    fare = 100 + (distance - 5) * 15
elif distance <= 30:
    fare = 100 + (10 * 15) + (distance - 15) * 12
else:
    fare = 100 + (10 * 15) + (15 * 12) + (distance - 30) * 10

if peak_hours == "yes":
    fare = fare + (fare * 20 / 100)

print("Final fare:", fare)



# 20. Employee Leave Approval System An employee requests leave from a company. 
# The request should be evaluated as follows:
# ● If requested days are greater than available leave → Leave Rejected ● If available leave is sufficient and requested days ≤ 3 → Leave Automatically Approved ● If requested days are 4–7 → Manager Approval Required ● More than 7 days → HR Approval Required Accept available leave and requested leave and display the appropriate decision. 

available = int(input("Enter available leave: "))
requested = int(input("Enter requested leave: "))

if requested > available:
    print("Leave Rejected")
elif requested <= 3:
    print("Leave Automatically Approved")
elif requested <= 7:
    print("Manager Approval Required")
else:
    print("HR Approval Required")