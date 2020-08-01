# Author: Makaliah Dickinson
# Date: 8/1/2020
# Description: Write a class named that has private data members for an employee's name, ID_number, salary,
#              and email_address.It should have an init method that takes four values and uses them to initialize the
#             data members. It should have get methods named get_name, get_ID_number, get_salary, and get_email_address.
#              Write a separate function (not part of the Employee class) that takes as parameters a list of names, a
#              list of ID numbers, a list of salaries and a list of email addresses.

class Employee:  # this is the employee class
    def __init__(self,emp_names, emp_ids, emp_sals, emp_emails):  # this is the init method
        self.emp_names = emp_names # to initialise the variables
        self.emp_ids= emp_ids
        self.emp_sals = emp_sals
        self.emp_emails= emp_emails

    def get_name(self):   # the get methods to get the values of the variables
        return self.emp_names

    def get_ID_number(self):
        return self.emp_ids

    def get_salary(self):
        return self.emp_sals

    def get_email_address(self):
        return self.emp_emails


def make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails):  # to make the list into employee object
    result = {} # initialising a dictionary
    for i in range(len(emp_names)):  # then iterating in the list and creating a employee object and setting to dictionary key as id
        emp = Employee(emp_names[i], emp_ids[i], emp_sals[i], emp_emails[i])
        result[emp_ids[i]] = emp
    return result



emp_names = ["Jean", "Kat", "Pomona"]
emp_ids = ["100", "101", "102"]
emp_sals = [30, 35, 28]
emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
for i in result:
    print(result.get(i).get_name(),result.get(i).get_ID_number(),result.get(i).get_salary(),result.get(i).get_email_address())