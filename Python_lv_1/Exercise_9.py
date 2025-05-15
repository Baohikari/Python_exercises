#Calculate age based on entered date of birth.
import datetime
def calculate_age(input):
    for _ in input:
        age_day = abs(datetime.date.today().day - int(input[0]))
        age_month = abs(datetime.date.today().month - int(input[1]))
        age_year = abs(datetime.date.today().year - int(input[2]))
    print(f'Your accurate age is: {age_year}, {age_day} day(s) and {age_month} month(s)')

user_input = input('Enter your date of birth(e.g.: dd/mm/yyyy): ')
handle_input = user_input.split("/")
result = calculate_age(handle_input)