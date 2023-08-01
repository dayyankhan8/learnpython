from datetime import date
# Enter your age details as per instructions
birth_year=input("Enter your year of birth: ")
birth_month=input("Enter your month of birth:")
birth_days=input("Enter your date of birth:")
today = date.today()
your_age_years=today.year-int(birth_year)
your_age_months=today.month-int(birth_month)
your_age_days=today.day-int(birth_days)
# this will print your age
print("Your age is ", your_age_years,"years ",your_age_months, "months", your_age_days, "days")