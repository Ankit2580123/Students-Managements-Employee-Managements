from faker import Faker
from home.models import *
import random
fake = Faker()

def seed_db(n)->None:
    try:
        for i in range(0,n):
            dep_obj=Department.objects.all()
            random_index=random.randint(0,len(dep_obj)-1)
            employee_id= f'EMP-0{random.randint(100,999)}'
            department=dep_obj[random_index]
            employee_name=fake.name()
            employee_email=fake.email()
            employee_age=random.randint(20,55)
            employee_address=fake.address()

            employee_id_obj=EmployeeID.objects.create(employee_id=employee_id)

            employee_obj=Employees.objects.create(
                        department=department,
                        employee_id=employee_id_obj,
                        employee_name=employee_name,
                        employee_email=employee_email,
                        employee_age=employee_age,
                        employee_address=employee_address,
        )

        
    except Exception as e:
        print(e)
    