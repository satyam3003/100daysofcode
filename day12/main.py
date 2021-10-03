import random
import ascii_art as art

def guess_no(num):
    win_flag = False
    guess = int(input("Place your guess: "))
    if guess == num:
        print(f'Congratulations! Your guess {guess} is correct...')
        win_flag = True
    elif num > guess:
        print("Guess too low")
    else:
        print("Guess too high")
    return win_flag


continue_play = True
while continue_play:
    number = random.randint(1,100)
    print(art.logo)
    level = input("Enter level: easy or hard - ")
    if level == "easy":
        i = 10
    else:
        i = 5

    print(f"You have {i} attempts")
    play = True
    while i != 0 and play:
        play = not guess_no(number)
        if play:
            i -= 1
            print(f"Attempts left: {i}")
            if i == 0:
                print(f"You lose correct answer was: {number}")

    cont_game = input("\nPlay again: y or n: ")
    if cont_game == 'n':
        print("Bye bye.....................")
        continue_play = False