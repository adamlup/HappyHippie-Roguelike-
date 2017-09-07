import random
import os
import sys
import end

skull = ('''                 \033[91muuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"\033[0m
     ''')

hangman = ['''\033[93m
  +---+
  |   |
      |
      |
      |
      |
=========\033[0m''', '''\033[93m
  +---+
  |   |
  \033[94mO   \033[93m|\033[0m
  \033[94m|   \033[93m|
      |
      |
=========\033[0m''', '''\033[93m
  +---+
  |   |
  \033[94mO   \033[0m\033[93m|\033[0m
 \033[94m/|\  \033[0m\033[93m|
      |
      |
=========\033[0m''', '''\033[93m
  +---+
  |   |
  \033[94mO   \033[0m\033[93m|\033[0m
 \033[94m/|\  \033[0m\033[93m|\033[0m
 \033[94m/    \033[0m\033[93m|
      |
=========\033[0m''', '''\033[93m
  +---+
  |   |
  \033[94mO   \033[0m\033[93m|\033[0m
 \033[94m/|\  \033[0m\033[93m|\033[0m
 \033[94m/ \  \033[0m\033[93m|
      |
=========\033[0m''']


def letter(used):
    counter = 0
    while counter == 0:
        guess = input("\033[1m\033[95m\nEnter a letter: \033[0m")
        guess = guess.upper()
        if len(guess) == 1:
            counter = 1
            break
        if guess in used:
            print("\nYou already used this letter ", guess)

    return str(guess)


def game():
    words = ["DEADLINE", 'FEEDBACK', 'OPENSPACE', 'MILESTONE', 'TARGET']
    word = random.choice(words)
    max_wrong = 0
    wrong = 5
    used = []
    a = 0
    so_far = "_" * len(word)
    print("\033[1m\033[95mAre you sure you know the corporation language? Check yourself in Hangman challenge.\033[0m")
    while wrong > max_wrong and so_far != word:
        print(hangman[a])
        print("\nYou have \033[93m", wrong, "\033[0mlifes")
        print("\nYou already used this letters ", used)
        print("\nThe searched word looks like this:", ' '.join(so_far))
        guess = letter(used)

        while guess in used:
            print("\nYou already used this letter ", guess)
            guess = input("\033[1m\033[95m\nEnter a letter: \033[0m")
            guess = guess.upper()
            while True:
                if len(guess) > 1:
                    guess = input("\033[1m\033[95m\nOnly one letter: \033[0m")
                    guess = guess.upper()
                else:
                    break

        used.append(guess)
        os.system("clear")

        if str(guess) in word:
            print("\nGood, ", guess, " is in a word")
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new

        else:
            print("\nUnfortunately, ", str(guess), " is not in the word")
            wrong -= 1
            a += 1

    if wrong == max_wrong:
        print(skull)
        print("\nSearched word is, ", word)
        end.lose_screen()

    else:
        print("Congratulations you find the word")
        print("\nSearched word is, ", word)
        return
