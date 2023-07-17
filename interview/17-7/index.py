
# PART 1
def checkPalindrome(num):
    if str(num)==str(num)[::-1]:
        return True
    return False

num=1213
result=checkPalindrome(num) 

# print(result)

#PART 2

company = {
    'employees': {
        'John': {'age': 35, 'job_title': 'Manager'},
        'Emma': {'age': 28, 'job_title': 'Software Engineer'},
        'Kelly': {'age': 41, 'job_title': 'Senior Developer'},
        'Sam': {'age': 30, 'job_title': 'Software Engineer'},
        'Mark': {'age': 37, 'job_title': 'Senior Manager'},
        'Sara': {'age': 32, 'job_title': 'Software Engineer'},
    }
}


def average_age_of_employees_with_s_job_title(company):
    sum=0
    employee_number=0

    employees= company.get('employees', {})
    
    for employee in employees.values():
        job_title= employee.get('job_title', '')
        if job_title.startswith("S"):
            sum+= employee.get('age',0)
            employee_number+=1
    
    if employee_number==0:
        return 0
    else:
        return sum / employee_number

print(average_age_of_employees_with_s_job_title(company))
