class Employee:
    # member variable i.e, class variable
    company = "XYZ"

    # method
    def display(self):
        self.company = "ABC"
        print("Company name : ",self.company)
        print("Company name 2 : ",Employee.company)

# object
emp = Employee()
emp.display()
