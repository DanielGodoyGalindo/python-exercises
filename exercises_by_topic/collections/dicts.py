"""
🧩 Challenge: Base de Datos de Empleados con Diccionarios
🎯 Objetivo: Crear un programa que almacene empleados con formato:

{"nombre": "juan", "departamento": "ventas", "salario": 2000}

Y permitir:
Añadir empleados
Buscar empleados por nombre
Mostrar todos los empleados
Calcular salario promedio
Mostrar cuántos empleados hay por departamento
"""


def employees_exercise():
    employees = []
    user_input = ""
    while user_input != "end":
        user_input = show_menu()
        if user_input == "1":
            employee = add_user()
            if employee:
                employees.append(employee)
                print("User added!\n")
        elif user_input == "2":
            employee_name = input("Please insert the name of a employee: ")
            if not employee_name.isdigit():
                found_employee = search_user(employee_name, employees)
                print(
                    f"Exployee found: {found_employee}\n"
                ) if found_employee else print("Employee not found!\n")
        elif user_input == "3":
            if employees:
                print(f"Employees: {employees}")
            else:
                print("No employees at the moment!\n")
        elif user_input == "4":
            if employees:
                print(f"Avg salary: {avg_salary(employees)}")
            else:
                print("No employees at the moment!\n")
        elif user_input == "5":
            output = employees_by_department(employees)
            if output:
                print(f"Employees by department: {output}\n")
            else:
                print("No employees found!\n")
        elif user_input == "6":
            break
    return "BYE"


def show_menu():
    print(
        "******* MENU *******\n1. Add user\n2. Search user\n3. Show all users\n4. Calculate average salary\n5. Number of employees by department\n6. End\n"
    )
    option = input("Select an option: ")
    return option


def validate_employee_name_and_department(input):
    if input == "":
        print("Input can't be an empty string!")
        return False
    if input.isdigit():
        print("Input must be a string not a number!")
        return False
    return True


def validate_salary(salary):
    if salary == "":
        print("Salary can't be empty!")
        return False
    if not salary.isdigit():
        print("Salary must be a number!")
        return False
    return True


def add_user():
    while True:
        employee_name = input("Please, enter a employee name (type 'end' to quit): ")
        if employee_name.lower() == "end":
            return None
        # name
        if not validate_employee_name_and_department(employee_name):
            continue
        department_name = input("Enter a department name: ")
        # department
        if not validate_employee_name_and_department(department_name):
            continue
        # salary
        salary = input("Enter salary: ")
        if not validate_salary(salary):
            continue
        employee = {
            "name": employee_name,
            "department": department_name,
            "salary": int(salary),
        }
        return employee


def avg_salary(employees):
    return sum(emp["salary"] for emp in employees) / len(employees)


def search_user(user_name, employees):
    for idx, emp in enumerate(employees):
        if emp["name"] == user_name:
            return employees[idx]
    return None


def employees_by_department(employees):
    employees_by_department = {}  # dict to store departments and the number of employees
    for emp in employees:
        dept = emp["department"]  # get dept name
        if dept not in employees_by_department:
            employees_by_department[dept] = 1
        else:
            employees_by_department[dept] += 1
    return employees_by_department


print(employees_exercise())
