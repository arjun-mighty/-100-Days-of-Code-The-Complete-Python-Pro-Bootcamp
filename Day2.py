print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill ? $"))
tip=int(input("What percentage of tip do you like to give 10,12 or 15 ?"))
people =int(input("How many people want to split the bill ?"))
tip_percent=tip/100
total_tipamout =bill*tip_percent
total_bill = bill+total_tipamout
bill_per_person = total_bill/people
final_amount=round(bill_per_person,2)
print("Each person should pay $"+str(final_amount))
