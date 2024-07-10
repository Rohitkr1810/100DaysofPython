print("Welcome to the Tip Calculator !!!")
total_bill =  float(input("What was the total bill? \n"))
tip_percent = int(input("What percentage of tip you wish to give?\n(Eg. 10 12 or even 5 or 0 \n"))
members = int(input("How many people to split the bill?\n"))

bill_tip = total_bill + tip_percent*total_bill/100
bill_per_person = round(bill_tip/members,2)
print(f"Each person should pay {bill_per_person}")
