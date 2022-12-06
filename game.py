
from random import randint

game_board = []
for spaces in range(5):
    game_board.append(['']*5)


game_board[0][0] = 'You'
game_board[2][1] = 'Joker'
HP = 5
x_value = 0
y_value = 0

choices = {"Up": 1, "Down": 2, "Left": 3, "Right": 4}

def character():

    print('Batman!')

def character_status():

        print(f'your current HP = {HP},')
        print('your coordinates are...')
        print(f'{x_value}, {y_value}')


def start_game():

    character()
    print('Its a dark starry night, you need to find Joker!')
    print(f"Here's your gps device {game_board},")
    character_status()
    print('Do you want to go up, right, or left?')
    print(f'Type in the corresponding number to your directions... \n{choices},')
    choice = input()

    if choice == '1':
        level_one()

    elif choice != '1':
        while True:
            print('The GPS is telling you to go up!')
            choice = (input("choose again... \n"))
            if choice == '1':
                level_one()
                break





def level_one():

    character_status()
    print('OH NO!')
    print("""You ran into DARTH VADER! 
Roll an even number from this dice
to jump over him and land closer to Joker!""")
    while True:
        print("Do you want to roll? \n 1 = Yes \n 2 = No")
        decision = input()

        if decision == '1':
            while True:
                dice = randint(1, 6)

                if dice == 2:
                    print(f'your rolled {dice},')
                    level_two()
                    break
                elif dice == 4:
                    print(f'your rolled {dice},')
                    level_two()
                    break
                elif dice == 6:
                    print(f'your rolled {dice},')
                    level_two()
                    break

                else:
                    print(f'you rolled {dice},')
                    print(f'roll again,')
                    print("Do you want to roll? \n 1 = Yes \n 2 = No")
                    roll_again= input()
                    if roll_again == '2':
                        game_over()
                        break
            break

        elif decision == '2':
            game_over()
            break

        elif decision != '1' or '2':
            print('Not an option!')



def level_two():

    print('...')
    print('\n You made it! \n')
    print('Do you want to go up, right, or left?')
    print(f'Type in the corresponding number to your directions... \n{choices},')
    choice = input()

    if choice == '4':
        level_three()

    elif choice != '4':
        while True:
            print('The GPS is telling you to go right!')
            choice = (input("choose again...\n"))
            if choice == '4':
                level_three()
                break


def level_three():
    print('JOKER!')
    print('To Defeat Joker, you must roll a 6 in three tries!')
    print("Do you want to roll? \n 1 = Yes \n 2 = No")
    decision = input()

    if decision == '1':
        for rolls in range(3):
            dice = randint(1,6)
            if dice == 6:
                print(f'You rolled {dice},')
                win()
                break

            else:
                print(f'You rolled {dice},')

        if dice != 6:
            game_over()








def win():
    print('\nYou Win!\n')
    print('You captured Joker and threw him in prison! \n')
    print('... \n')
    print("""            *         *      *         *
          ***          **********          ***
       *****           **********           *****
     *******           **********           *******
   **********         ************         **********
  ****************************************************
 ******************************************************
********************************************************
********************************************************
********************************************************
 ******************************************************
  ********      ************************      ********
   *******       *     *********      *       *******
     ******             *******              ******
       *****             *****              *****
          ***             ***              ***""")

    print('\nGAME OVER')

def game_over():
    print('Joker got away... GAME OVER')

def main():
    start_game()



if __name__ == "__main__":
    main()
