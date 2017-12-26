emp_id=1001
basic_sal=15000.00
allowances=6000.00
monthly_gross_salary=basic_sal+allowances
if monthly_gross_salary<=5000.00:
       income_tax=0
elif ((monthly_gross_salary>5000.00) and (monthly_gross_salary<=10000.00)):
       income_tax=(10*monthly_gross_salary)/100
elif ((monthly_gross_salary>10000.00) and (monthly_gross_salary<=20000.00)):
       income_tax=(20*monthly_gross_salary)/100
else:
       income_tax=(30*monthly_gross_salary)/100
       net_salary=monthly_gross_salary-income_tax
       print("employee id is",emp_id)
       print("basic salary is:",basic_sal) 
       print("allowance is:",allowances) 
       print("gross pay is:",monthly_gross_salary)
       print("income tax to be paid is:",income_tax)
       print("net salary is:",net_salary)
