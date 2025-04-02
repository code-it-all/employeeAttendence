from datetime import date, timedelta

class Employee:
    """Manages the employee attendance records"""

    employee_list = []


    def create_employee(self, name, age):
        count = 1000
        employee = {
            'Emp_id': count+1,
            'name': name,
            'age': age,
        }
        print("Employee created successfully, employee id : ", employee['Emp_id'])
        self.employee_list.append(employee)

    def display_employee_all(self):
        for employee in self.employee_list:
            print(f"emp_id: {employee['Emp_id']}, name: {employee['name']}, age: {employee['age']}")

    def mark_attendance(self, emp_id):
        for employee in self.employee_list:
            if employee['Emp_id'] == emp_id:
                emp_attendance = []
                last_seven_date = date.today() - timedelta(days=7)
                for i in range(0, 7):
                    print(f"Date: {last_seven_date + timedelta(days=i)}")
                    emp_attendance.append(input("Enter the attendance: , 'p' for present and 'a' for absent:"))
                employee['attendance'] = {emp_attendance}

    def view_attendance(self, emp_id):
        for employee in self.employee_list:
            if employee['Emp_id'] == emp_id:
                print(employee['attendance'])

    def get_employee_id(self, name):
        for employee in self.employee_list:
            if employee['name'] == name:
                return employee['Emp_id']

    def delete_employee(self, emp_id):
        self.employee_list.remove(emp_id)
        print("Employee deleted successfully")


