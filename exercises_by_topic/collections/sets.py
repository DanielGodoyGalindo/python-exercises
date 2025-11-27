'''
🧩 Challenge: Gestión de Invitados con Sets
🎯 Objetivo:

Aprender:

✔ set()
✔ eliminación automática de duplicados
✔ add()
✔ remove()
✔ in
✔ unión → |
✔ intersección → &
✔ diferencia → -

📝 Ejercicio:

Tenemos dos listas de invitados:

Invitados confirmados
Invitados que realmente han asistido

El programa deberá:

Pedir invitados confirmados y guardarlos en un set()
Pedir invitados que han llegado y guardarlos en otro set()

Mostrar:

invitados duplicados eliminados (propiedad del set)
invitados que asistieron y estaban en lista (intersección)
invitados confirmados que no vinieron (diferencia)
personas que vinieron sin estar invitadas (diferencia inversa)

Confirmed guests: {'ana', 'jorge', 'marta', 'ana'}
Arrived guests: {'marta', 'carlos'}

Guests who arrived and were invited: {'marta'}
Confirmed but did not arrive: {'ana', 'jorge'}
Arrived but not invited: {'carlos'}
'''

def guests_management():
    ask_for_confirmed_guests()
    return None

def ask_for_confirmed_guests():
    guests = set()
    guest = ""
    while guest != "end":
        guest = input("Type the name of a confirmed guest ('end' for exit): ")
        if not guest.isdigit():
            guests.add(guest)
    guests.discard("end")
    print(guests)
    return guests

def ask_for_arrived_guests():
    guests = set()
    return guests

print(guests_management())