from collections import Counter


# 1. List Statistics
def list_statistics():
    user_input = ""
    user_list = []
    while user_input.upper() != "EXIT":
        user_input = input("Enter a number (or type EXIT to finish): ")
        try:
            user_input = float(user_input)
            user_list.append(user_input)
        except ValueError:
            if user_input != "EXIT":
                print("You have to enter a number!")
    if user_list:
        print("The MAXIMUM number is: ", max(user_list))
        print("The MINIMUM number is: ", min(user_list))
        print("The SUM of all numbers is: ", sum(user_list))
        print("The AVERAGE of all numbers is: ", sum(user_list) / len(user_list))
    else:
        print("No numbers were entered.")


# list_statistics()


# 2. Remove Duplicates from a List
def no_duplicates_list():
    words_list = []
    unique_list = []
    user_input = ""
    while user_input.upper() != "EXIT":
        user_input = input("Enter a word (or type EXIT to finish): ")
        if user_input.upper() != "EXIT":
            words_list.append(user_input)
    for word in words_list:
        if words_list.count(word) == 1:
            unique_list.append(word)
    unique_list.sort()
    print("Sorted unique words: ", unique_list)


# no_duplicates_list()


# 3. Palindrome checker
def palindrome_checker(word: str):
    word = word.lower()
    if word == word[::-1]:  # slicing
        print(word, "is a palindrome!")
    else:
        print(word, "is not a palindrome :(")


# palindrome_checker("Racecar")


# 4. Count Word Occurrences
def count_word_occurrences():
    sentence = input("Type a sentence: ")
    split_sentece = sentence.lower().split()
    # Use Counter, a class that counts repeated elements in a collection
    counted_words = Counter(split_sentece)
    # dict() creates a dictionary using counter object
    print(dict(counted_words))


# count_word_occurrences()


# 5. Find Prime Numbers in a Range
def find_prime_numbers():
    prime_numbers = []
    number = int(input("Insert a number"))
    num_copy = number
    while number > 0:
        if is_prime(number):
            prime_numbers.append(number)
        number -= 1
    prime_numbers.reverse()
    print(f"The prime numbers from 1 to {num_copy} are {prime_numbers}")


def is_prime(number: int) -> bool:
    count = 0
    divisor = number
    while number > 0:
        if divisor % number == 0:
            count += 1
        number -= 1
    # Ternary operator
    return True if count == 2 else False


find_prime_numbers()
