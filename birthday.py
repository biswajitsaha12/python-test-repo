import datetime

birthday_str = input("Enter your birthday (DD-MM-YYYY): ")
birthday = datetime.datetime.strptime(birthday_str, '%d-%m-%Y').date()
#print(birthday)

today = datetime.date.today()
#print(today)

next_birthday = datetime.date(today.year, birthday.month, birthday.day)
#print(next_birthday); print(today.year); print(birthday.month); print(birthday.day)

if next_birthday < today:
    next_birthday = datetime.date(today.year + 1, birthday.month, birthday.day)

days_to_birthday = (next_birthday - today).days
print(f"Your birthday is in {days_to_birthday} days")
