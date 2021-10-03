import random
import gamedata as gd
import ascii_art as art


def win_lose(user,win_cho):
    if user == win_cho:
        return True
    else:
        return False


first_item = random.choice(gd.data)
second_item = random.choice(gd.data)
play_start = True
win_score = 0
while play_start:
    print(art.logo)
    print(f"\nCompare A: {first_item['name']}, a {first_item['description']}, from {first_item['country']}")

    print(art.vs)

    print(f"Against B: {second_item['name']}, a {second_item['description']}, from {second_item['country']}")

    user_choice = input("Who have more followers? A or B -> ").upper()

    if first_item['follower_count'] > second_item['follower_count']:
        win_choice = 'A'
    else:
        win_choice = 'B'

    win_flag = win_lose(user_choice,win_choice)
    if win_flag:
        first_item = second_item
        second_item = random.choice(gd.data)
        win_score += 1
        print(f"Correct Answer! winning count is {win_score}")
    else:
        print(f"Incorrect answer! win count is {win_score}")
        play_start = False
