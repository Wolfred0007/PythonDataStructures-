age=25
name="John"
salary=24000
if salary > 25000:
    print("to be taxed")
else:
    print("should not be taxed")

def annual_salary(salary_per_month):
    annual=salary_per_month*12
    return annual


result=annual_salary(salary)
print(name,end=" ")
print("is",end=" ")
print(age,end=" ")
print("years old he earns",end=" ")
print(result,end=" ")
print("per annum")
