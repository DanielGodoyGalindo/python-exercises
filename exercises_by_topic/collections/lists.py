"""
🧩 Challenge: Gestión de Inventario con Listas
Crea un script que mantenga una lista de productos en un inventario.

🎯 Requisitos:
Crear una lista vacía llamada inventory.
Pedir al usuario que ingrese nombres de productos.
Cada producto se agrega a la lista.
Cuando el usuario escriba "end", se termina la entrada.

Después del ingreso:
Mostrar todos los productos
Mostrar cuántos productos hay
Mostrar si existe un producto duplicado
Ordenar la lista alfabéticamente
Eliminar un producto específico si el usuario lo pide
"""

from collections import Counter


def inventory():
    # Create an empty list that will store all product names entered by the user
    inventory = list()

    while True:
        current_product = input("Write a product name: ")
        current_product = current_product.lower()
        # Remove leading and trailing spaces from the input
        current_product = current_product.strip()
        if current_product == "":
            print("Empty input not allowed!")
            continue
        # If the user types "end", exit the loop and finish the input phase
        if current_product == "end":
            break
        # Check if the input consists only of digits
        # Products should be actual text, not numeric values
        if current_product.isdigit():
            print("Only strings are allowed!")
            continue
        # Add the cleaned product name to the list
        inventory.append(current_product)

    # Display the full list of products entered
    print(f"Inventory: {inventory}")
    # Display the number of occurrences for each product using Counter
    # e.g., Counter({'apple': 2, 'banana': 1})
    print(f"Total products: {Counter(inventory)}")
    # Create a list of duplicated products by checking if an item appears more than once
    duplicates = [i for i in set(inventory) if inventory.count(i) > 1]
    print(f"Product duplicates found: {duplicates}")
    # Display the inventory sorted alphabetically
    print(f"Sorted inventory: {sorted(inventory)}")
    # Ask the user for a product name to remove from the list
    item_to_remove = input("Which product do you want to remove?: ")
    if item_to_remove in inventory:
        inventory.remove(item_to_remove)
        print(f"Updated inventory: {inventory}")
    else:
        print(f"Product '{item_to_remove}' not found in inventory")
    return "END"


print(inventory())
