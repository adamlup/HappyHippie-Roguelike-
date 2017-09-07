import random
import sys
import end


def get_random_number():
    number_list = []
    while len(number_list) < 3:
        digit = random.randint(0, 9)
        if digit not in number_list:
            number_list.append(digit)
    return number_list


def get_user_input():
    while True:
        user_guess = input("Try to guess 3 digits number: ")

        if user_guess.isalpha():
            print("Enter only digits")

        elif len(user_guess) != 3:
            print("Your guess hasnt 3 digits")

        else:
            return list(user_guess)


def compare_user_input_witth_answer(user_guess, correct_answer):
    hint_list = []
    index = 0
    for a in correct_answer:
        if str(a) == user_guess[index]:
            hint_list.insert(0, "HOT")

        elif str(a) in user_guess:
            hint_list.append("WORM")
        index += 1

    if not hint_list:
        hint_list.append("cold")

    return hint_list


def boss(score):
    correct_answer = get_random_number()
    while score != 0:
        print("\nChances to guess = ", score)
        user_guess = get_user_input()
        hint_list = compare_user_input_witth_answer(user_guess, correct_answer)
        print(hint_list)
        if hint_list == ['HOT'] * 3:
            return
        else:
            score -= 1
    if score == 0:
        end.lose_screen()
