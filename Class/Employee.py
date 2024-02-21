class Employee:
    emp_id = 101
    def __init__(self, name, salary, designation) -> None:
        self.emp_id = Employee.emp_id
        self.name = name
        self.salary = salary
        self.designation = designation
        Employee.emp_id += 1

    def show_details(self):
        print(f'ID: {self.emp_id}\nName: {self.name}\nSalary: {self.salary}\nDesignation: {self.designation}')
    
    @classmethod
    def total_employees(cls):
        return cls.emp_id - 101
    

if __name__ == "__main__":
    print(Employee.total_employees())
    #create first employee
    c1 = Employee('Abel', '100', 'Network Engineer')
    c1.show_details()
    print("-----------------")
    #create second employee
    c2 = Employee('Bruno', '50', 'Product Manager')
    c2.show_details()
    #check number of employees created
    tot_emp = Employee.total_employees()
    
    print("---------------")
    print(f'Total Employees: {tot_emp}')
