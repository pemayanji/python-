# Inheritance -> the process of inheriting the properties of the parent class

class Person:
    def person_info(self,name,age):
        print("Inside person class")
        self.name = name
        print("Name : ",name,"Age :",age)

class Company:
    def company_info(self,company_name,location):
        print("Inside company class")
        print("Name :",company_name,"location",location)

class Employee(Person,Company):
    def employee_info(self,salary,skill):
        super().person_info("Binod",20)
        print("Inside employee class")
        print("Salary : ",salary,"Skill : ",skill)

emp = Employee()

emp.person_info("Jessi",28)

emp.employee_info(1200,"machine")
