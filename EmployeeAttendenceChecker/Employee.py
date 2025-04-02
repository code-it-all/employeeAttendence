from datetime import date, timedelta

class Employee:
    """Manages the employee attendance records"""

    employee_list = []

    count = 1000

    def create_employee(self, name, age):

        employee = {
            'Emp_id': self.count+1,
            'name': name,
            'age': age,
        }

        self.count += 1
        print("Employee created successfully, employee id : ", employee['Emp_id'])
        self.employee_list.append(employee)

    def display_employee_all(self):
        for employee in self.employee_list:
            print(f"emp_id: {employee['Emp_id']}, name: {employee['name']}, age: {employee['age']}")

    def mark_attendance(self, emp_id):
        print(self.employee_list)
        for employee in self.employee_list:
            if employee['Emp_id'] == emp_id:
                emp_attendance = []

                last_seven_date = date.today() - timedelta(days=7)
                for i in range(7):
                    current_date = last_seven_date + timedelta(days=i)
                    while True:
                        attendance = input(f"Enter the attendance for {current_date}: , 'p' for present and 'a' for absent:").strip().lower()
                        if attendance in ['p', 'a']:
                            break
                        else:
                            print("Invalid input, please enter 'p' for present and 'a' for absent")


                if 'attendance' in employee:
                    employee['attendance'].append(emp_attendance)
                else:
                    employee['attendance'] = emp_attendance

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


