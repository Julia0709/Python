#! /usr/local/bin/python3


def startup():
    print("========= WELCOME TO POISON PENNY =======")
    print("|    You Don't want the last penny!!   |")
    print("========================================= \n")

    return int(input("Choose game mode 1 or 2: \n1 --- Player vs Computer \n2 --- Player vs Player \n"))


def display_current_state(p, tk, ttl):
    if p == 1:
        plyr = "Player 2"
    else:
        plyr = "Player 1"

    print("\n" + plyr + " took " + str(tk) + " pennies.")
    print("Total: " + str(ttl) + " left. \n")


def get_user_input_check_if_done(p, ttl):
    tk = int(input("player " + str(p) + " take your penny(s): "))
    while tk != 1 and tk != 2:
        print("Invalid input! Please take 1 or 2 pennies.")
        tk = int(input("p " + str(p) + " take your penny(s) again: "))
    ttl -= tk
    p = 1 if p == 2 else 2
    if ttl <= 0:
        print("player " + str(p) + " Won!")
        return True, ttl, tk, p

    return False, ttl, tk, p


def computer_move(d, ttl, tk):
    if ttl == 1:
        tk = 1
    elif ttl == 2:
        tk = 1
    elif ttl == 3:
        tk = 2
    elif ttl == 4:
        tk = 1
    elif ttl == 5:
        tk = 2
    else:
        from random import randint
        tk = randint(1, 2)

    if ttl <= 0:
        print("player 1 Won!")
        return True, ttl, tk
    else:
        ttl -= tk
        return False, ttl, tk


n = startup()
total = int(input("How many pennies you want to start with? "))
done = False
player = 1
take = 0
while total > 0 and not done:

    if n == 1 and player == 2:
        print("player " + str(player) + " take your penny(s): ")
        done, total, take = computer_move(done, total, take)
        player = 1
    else:
        done, total, take, player = get_user_input_check_if_done(player, total)

    display_current_state(player, take, total)

print("GAME OVER")
