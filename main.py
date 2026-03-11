# task 1  (кількість днів між заданою датою і поточною датою)

def get_days_from_today(date):
    pass



get_days_from_today("2021-10-09") #157



# task 2

def get_numbers_ticket(min, max, quantity):
    pass




lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)



# task 3 

def normalize_phone(phone_number):
    pass





raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)



# task 4

'''from datetime import datetime, date, timedelta

users = [
    {"name": "Bill Gates", "birthday": "1995.3.15"},
    {"name": "Steve Jobs", "birthday": "2000.3.21"},
    {"name": "Jinny Lee", "birthday": "1996.3.12"},
    {"name": "Sarah Lee", "birthday": "1987.3.13"},
    {"name": "Jonny Lee", "birthday": "1978.3.22"},
    {"name": "John Doe", "birthday": "1982.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")

def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list

prepared_users = prepare_user_list(users)

def find_next_weekday(start_date, weekday):

    days_ahead = weekday - start_date.weekday() 

    if days_ahead <= 0: 
        days_ahead += 7

    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today() 

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days <= days:
            birthday_this_year = adjust_for_weekend(birthday_this_year)

            congratulation_date_str = date_to_string(birthday_this_year)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays


print(get_upcoming_birthdays(prepared_users, days=7))'''