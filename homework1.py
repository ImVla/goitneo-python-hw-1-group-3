from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)}
]

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)

    today = datetime.today().date()
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        
        birthday_this_year = birthday.replace(year = today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)
        
        delta_days = (birthday_this_year - today).days
         
        if 0 <= delta_days < 7:
            birthday_day_of_week = (today + timedelta(days = delta_days)).strftime("%A")
            birthdays_per_week[birthday_day_of_week].append(name)
    
    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")

get_birthdays_per_week(users)

print(users)







