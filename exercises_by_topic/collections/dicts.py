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


def employees():
    employees = []
    user_input = ""
    while user_input != "end":
        show_menu()
    while True:
        employee_name = input("Please, enter a employee name (type 'end' to quit): ")
        if employee_name.lower() == "end":
            break
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
            "salary": salary,
        }
        employees.append(employee)
    return employees


def show_menu():
    print(
        "1. Add user\n2. Search user\n3.Show all users\n4. Calculate average salary\n5. NUmber of employees per department"
    )
    option = input("Select an option")
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


print(employees())
