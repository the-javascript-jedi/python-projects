bill=float(input("Enter the bill amount: "))
tip=int(input("Enter the tip amount: "))
people=int(input("Enter the members: "))

tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
bill_per_person=round(total_bill/people,2)
# round the amount to 2 decimal places by formatting to two decimals
rounded_final_amount="{:.2f}".format(bill_per_person)

print(f"the tip is {total_tip_amount}, the total is ${total_bill} and the bill per person is {rounded_final_amount}")