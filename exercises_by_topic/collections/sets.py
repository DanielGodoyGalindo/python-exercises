"""
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
"""


def guests_management():
    print("Enter the confirmed guests:")
    confirmed_guests = ask_for_guests()
    print("Enter the arrived guests:")
    arrived_guests = ask_for_guests()
    # Confirmed guests
    print(f"\nConfirmed guests: {confirmed_guests}")
    # Arrived guests
    print(f"Arrived guests: {arrived_guests}")
    # Arrived guests that were invited
    arrived_invited = confirmed_guests & arrived_guests
    print(f"Arrived guests that were invited: {arrived_invited}")
    # Guests who were invited but did not arrive
    not_arrived_invited = confirmed_guests - arrived_guests
    print(f"Guests invited but did not come: {not_arrived_invited}")
    # Guests who came without invitation
    arrived_not_invited = arrived_guests - confirmed_guests
    print(f"Guests arrived not invited: {arrived_not_invited}")
    # Total number of guests that arrived
    print(f"Number of guests arrived: {len(arrived_guests)}")
    return "End"


def ask_for_guests():
    guests = set()
    while True:
        guest = input("Type the name of a guest ('end' to finish): ").strip().lower()
        if guest == "end":
            break
        if guest == "":
            print("Empty input not allowed!")
            continue
        if guest.isdigit():
            print("Guest name must be a text, not a number!")
            continue
        guests.add(guest)
    return guests


print(guests_management())
