# Write a program to input: number of hours worked per week, remuneration per standard hour, 
# from which calculate the employee's actual salary. 
# Know that: the standard number of hours per week is 44 hours, and each hour exceeding the standard is paid one and 
# a half times more than the standard hour.
worktime_per_week = int(input('Enter work time per week: '))
salary_per_worktime = int(input('Enter remuneration per standard hour: '))
def actual_salary(worktime, remuneration, salary = 1):
    if(worktime <= 44):
        salary = worktime * remuneration
    if(worktime > 44):
        salary = 44 * remuneration + ((worktime - 44) * (1.5 * remuneration))
    return salary

calculate_actual_salary = actual_salary(worktime_per_week, salary_per_worktime)
print(f'Your actual salary is: {calculate_actual_salary}')