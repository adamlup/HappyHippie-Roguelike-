import random

def get_random_number():
    number_list = []
    while len(number_list) < 3:
        digit = random.randint(0, 9)
        if digit not in number_list:
            number_list.append(digit)
    print(number_list)
    return number_list        


def get_user_input():
   while True:
    user_guess = input("Enter the number: ")

    if user_guess.isalpha():
        print("Enter only digits")

    elif len(user_guess) != 3:
        print("Input hasnt 3 digits")

    else:
        return list(user_guess)


def compare_user_input_witth_answer(user_guess, correct_answer):
    index = 0
    hint_list = []

    for a in correct_answer:
        if str(a) == user_guess[index]:
            hint_list.insert(0, "HOT")
            
        elif str(a) in user_guess:
            hint_list.append("WORM")    
        index += 1

        if not hint_list:
            hint_list.append("cold")

        return hint_list


def check_result(hint_list):
    if hint_list == ["HOT"] * 3:
        return True    


def boss():
    correct_answer = get_random_number()

    tries_left = 10
    while tries_left > 0:
        user_guess = get_user_input()
        result = compare_user_input_witth_answer(user_guess, correct_answer)
        print(result)
        if check_result(result):
            print("WIN")
            break
        tries_left -= 1
    if tries_left == 0:
        print("LOSE")    


