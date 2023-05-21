age=input("What is your current age?")
# convert string to number
age_as_int=int(age)
# we presume end of life as 90, so from current age to end of age calculate the years
years_remaining=90-age_as_int
days_remaining=years_remaining*365
weeks_remaining=years_remaining*52
months_remianing=years_remaining*12

message=f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remianing}"
print(message)