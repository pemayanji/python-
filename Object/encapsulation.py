class Employee:

    def __init__(self,name,project,salary):
        self.name = name  #public member
        self._project = project  #protected
        self.__salary = salary  #private

    def Show(self):
        print("Name :",self.name)

emp = Employee("Madhav","Xavier",1000)
emp.Show()
print(emp.name)
print(emp._project)
print(emp._Employee__salary)

