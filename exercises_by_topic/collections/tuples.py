"""
🔥 Challenge: Sistema de Puntuaciones con Tuplas
Crea un programa en Python que gestione puntuaciones de jugadores usando tuplas.
🧩 Requisitos: Pide al usuario que ingrese varias puntuaciones en el formato: nombre puntuacion

Ejemplo:
Ana 120
Juan 300
Ana 200

Guarda cada entrada como una tupla: ("Ana", 120)
Agrega todas las tuplas a una lista de tuplas.
Después de ingresar los datos (ej. cuando el usuario escribe "fin"), el programa debe:
✔ Mostrar:
    Todas las tuplas ingresadas.
    La puntuación más alta, usando max().
    El jugador con más ocurrencias (quién jugó más veces).
    Una nueva lista ordenada por puntuación de mayor a menor usando sorted() con key.
"""

from collections import Counter


def scores():
    # Creates an empty list to store tuples of (name, score)
    score_list = list()

    while True:
        # Gets a player name from the user
        user_input_name = input("Insert a name: e.g. BOB: ")

        # If user types "end", stops the name input loop
        if user_input_name == "end":
            break

        # Gets a score from the user
        user_input_score = input("Insert a score: e.g. 100: ")

        # If user types "end", stops the score input loop
        if user_input_score == "end":
            break

        # Validates that the score entered is numeric
        # The built-in function isdigit() checks if the string contains only digits
        if not user_input_score.isdigit():
            print("Score must be a number.")
            continue

        # Appends a new entry to the list as a tuple (name, integer score)
        score_list.append((user_input_name, int(user_input_score)))

    # Displays the raw list entered by user
    print(f"Input data by user {score_list}")

    # zip(*score_list) unpacks the list of tuples into two separate tuples:
    # one containing all the names and one containing all the scores
    names, scores = zip(*score_list)

    # max() returns the highest value in an iterable
    # Here it returns the highest numeric score
    print(f"Max score: {max(scores)}")

    # Counter() from collections counts occurrences of each unique name
    # .items() returns pairs of (name, frequency)
    # max(..., key=lambda) returns the pair with the highest frequency
    max_freq = max(Counter(names).items(), key=lambda ele: ele[1])

    # max_freq[0] gives the name with the most occurrences
    print(f"Max frecuency by name: {max_freq[0]}")

    # sorted() sorts the tuple list using a custom key
    # lambda x: x[1] tells Python to sort by score value
    # reverse=True makes it descending order (from highest score to lowest)
    print(
        f"Sorted list by score: {sorted(score_list, key=lambda x: x[1], reverse=True)}"
    )


scores()
