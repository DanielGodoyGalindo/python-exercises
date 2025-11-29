"""
Ejercicio:
Crea una función:

def describe_person(name, **details):
    ...

Uso: describe_person("Alex", age=30, job="engineer", country="USA")

Salida:

Name: Alex
age: 30
job: engineer
country: USA
"""


def describe_person(name, **details):
    # person = f"Name: {name}\n age: {details['age']}\n job: {details['job']}\n country: {details['country']}"
    person = f"Name: {name}\n"
    for key, value in details.items():
        person += f"{key}: {value}\n"
    return person


print(describe_person("Alex", age=30, job="engineer", country="USA"))
