# ------------------ Blackjack Project ----------------------
import ascii_art as art
import random
from replit import clear


def card_selection():
    list_of_ucard = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return list_of_ucard[random.randint(0, len(list_of_ucard) - 1)]


def sum_card(get_list):
    return sum(get_list)


print(art.logo)
player_money = 1000
print(f"You have ₹{player_money}")
first_logo = 0
play_game = True
while play_game:
    if first_logo != 0:
        print(art.logo)
    first_logo = 1
    bet_amount = int(input("Enter bet money: "))
    win_flag = False
    tie_flag = False
    end_this_game = False
    player_list = []
    comp_list = []
    while len(player_list) < 2:
        player_list.append(card_selection())
    print(f"Your cards: {player_list}")

    comp_list.append(card_selection())
    print(f"Computer cards: {comp_list}\n")

    player_sum = sum_card(player_list)
    if player_sum == 21 and len(player_list) == 2:
        print("Its a blackJack! You Won!!! 🤩")
        win_flag = True
        end_this_game = True

    while not end_this_game:
        draw = True
        while draw:
            draw_ask = input("Do you want to draw a card ? y or n: ")
            if draw_ask == 'y':
                player_list.append(card_selection())
                print(player_list)
            else:
                draw = False

        player_sum = sum_card(player_list)
        print(f"\nYour cards are {player_list} Your card sum is {player_sum}")

        if player_sum > 21 and player_list.count(11) != 0:
            print("Taking 11 as 1....")
            player_list[player_list.index(11)] = 1
            player_sum = sum_card(player_list)
            print(f"\nYour cards are {player_list} Your card sum is {player_sum}")

        if player_sum > 21:
            print("You Lose 😕")
            win_flag = False
            end_this_game = True

        while not end_this_game:
            comp_list.append(card_selection())
            comp_sum = sum_card(comp_list)
            while comp_sum < 17:
                comp_list.append(card_selection())
                comp_sum = sum_card(comp_list)

            print(f"Computer cards are {comp_list} Computer card sum is {comp_sum}\n")
            if comp_sum > 21:
                print("You win.🤩")
                win_flag = True
            elif comp_sum > player_sum:
                print("You lose.😕")
                win_flag = False
            elif player_sum > comp_sum:
                print("You win 🤩")
                win_flag = True
            elif player_sum == comp_sum:
                print("Its a tie..")
                tie_flag = True
            end_this_game = True

    if not tie_flag:
        if win_flag:
            player_money = player_money + bet_amount
            print(f"You have ₹{player_money} left...")
        if not win_flag:
            player_money -= bet_amount
            print(f"You have ₹{player_money} left...")

    if player_money > 0:
        play = input("Do you want to play again? y or n: ")
        clear()
        if play == 'n':
            play_game = False
    else:
        play_game = False
        print("Bring more money tomorrow.. bye..")
