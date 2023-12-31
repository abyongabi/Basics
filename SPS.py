import random

ls = [('sc', 'Scissors'), ('p', 'Paper'), ('st', 'Stone')]
valid_ls = ['sc', 'p', 'st']
rank_ls = [('sc', 'p'), ('p', 'st'), ('st', 'sc')]


def game_comp_choice():
    g_comp_choice = ls[random.randint(0, 2)][0]
    for k in range(len(ls)):
        if ls[k][0] == g_comp_choice:
            print(f'The computer chose {ls[k][1]}')
            return g_comp_choice


while True:
    choice = input("What would you like play? [Sc]Scissors [P]Paper [St]Stone: ")
    choice = choice.lower()
    if choice not in valid_ls:
        print("Please enter a valid value")
        continue
    comp_choice = game_comp_choice()
    for i in range(len(rank_ls)):
        if choice == rank_ls[i][0]:
            if comp_choice == rank_ls[i][1]:
                print("You win!")
                continue
            elif comp_choice == choice:
                print("It's a draw!")
                continue
            else:
                print("You loose!")
                continue
    cont = input("Press [q] to quit...  ").lower()
    if cont == 'q':
        break
