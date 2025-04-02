import Employee

employee = Employee.Employee()


user_active = True



while user_active:
    print("Please selected the operation you want to perform: ")
    print("1. Create an Employee")
    print("2. View all Employees")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Delete Employee")
    print("6. Exit")
    user_choice = int(input("Enter your choice: "))



    if user_choice == 1:

        employee_name = input("Enter employee name: ")
        employee_age = int(input("Enter employee age: "))
        employee.create_employee(employee_name, employee_age)


    elif user_choice == 2:
        employee.display_employee_all()


    elif user_choice == 3:
        emp_id = input("Enter employee id who is present: ")
        employee.mark_attendance(emp_id)

    elif user_choice == 4:
        emp_name = input("Enter employee name who's attendance needs to be checked: ")
        employee.view_attendance(employee.get_employee_id(emp_name))

    elif user_choice == 5:
        emp_name = input("Enter employee name who is to be deleted: ")
        employee.delete_employee(employee.get_employee_id(emp_name))

    elif user_choice == 6:
        user_active = False
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
