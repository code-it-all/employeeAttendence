from datetime import date, timedelta, datetime

class Employee:
    """Manages the employee attendance records"""

    employee_list = [{'Emp_id': 1, 'name': 'John', 'age': 30, 'attendance': []},
                     {'Emp_id': 2, 'name': 'Jane', 'age': 25, 'attendance': []},
                     {'Emp_id': 3, 'name': 'Jack', 'age': 35, 'attendance': []},]


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
            print(employee)
            # print(f"emp_id: {employee['Emp_id']}, name: {employee['name']}, age: {employee['age']}")

    def mark_attendance(self, emp_id):
        # print(self.employee_list)
        # print("inside mark_attendance function")
        for employee in self.employee_list:
            # print(employee)
            if employee['Emp_id'] == emp_id:
                if 'attendance' not in employee:
                    employee['attendance'] = []
                emp_attendance = employee['attendance']
                last_seven_date = date.today() - timedelta(days=7)
                for i in range(7):
                    current_date = last_seven_date + timedelta(days=i)
                    attendance = input(f"Enter the attendance for {current_date}: , 'p' for present and 'a' for absent:").strip().lower()
                    employee_attendance = {
                        'date': current_date,
                        'attendance': attendance
                    }
                    emp_attendance.append(employee_attendance)
                print(emp_attendance)
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
        records = [record for record in self.employee_list if record["Emp_id"] != emp_id]
        self.employee_list = records

    def report(self):
        for employee in self.employee_list:
            print(f"Employee ID: {employee['Emp_id']}, Name: {employee['name']}, Age: {employee['age']}")
            print("Attendance Report:")
            for i in employee['attendance']:
                print(f"Attendance: {i}")
            print("----------------------------------------")



