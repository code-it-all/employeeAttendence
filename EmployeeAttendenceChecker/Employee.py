class Employee:
    """Manages th employee attendance records"""

    employee_list = []

    def create_employee(self, emp_id, name, age, salary):
        employee = {
            'Emp_id': emp_id,
            'name': name,
            'age': age,
            'salary': salary,
        }
        self.employee_list.append(employee)
        print("Employee created successfully")

    def display_employee_all(self):
        for employee in self.employee_list:
            print(f"emp_id: {employee['Emp_id']}, name: {employee['name']}, age: {employee['age']}, salary: {employee['salary']}")

    def mark_attendance(self, emp_id, attendance_date, status):
        for employee in self.employee_list:
            if employee['Emp_id'] == emp_id:
                employee['attendance'] = {
                    'date': attendance_date,
                    'status': status
                }
                print(employee)
        print("Attendance marked successfully")

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

