emp_list = [
          {'name':'aman','salary':5000},
          {'name':'arman','salary':15000},
          {'name':'mohan','salary':3500},
          {'name':'rohan','salary':6000}
]



def max_salary_emaployee():
          max_emp = None
          max_salary = 0
          for emp in emp_list:
                    if emp['salary'] > max_salary:
                              max_salary = emp['salary']
                              max_emp = emp
          return max_emp

ans = max_salary_emaployee()
print(ans)