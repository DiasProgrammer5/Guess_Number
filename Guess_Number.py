import random
import ast

streak_name = 'win_streak.txt'

def save_value(value, filename):
    with open(filename, 'w') as file:
        file.write(str(value))

def load_value(filename):
    with open(filename, 'r') as file:
        return file.read().strip()
    
try:
    win_streak = ast.literal_eval(load_value(streak_name))
    print('Your current win streak is %s' % win_streak)

except:
    win_streak = 0

def main():

    print('\033[1m' + '\033[96m' + 'Guess the Number' + '\033[0m')
    max_trys = int(input('How many trys do you want: '))
    trys = 1
    win = 0
    cont = 0
    
    global win_streak

    x = random.randint(1, 99)
    try: 
        while trys <= max_trys and win == 0:
            try:
                guess = int(input('{}ª Attempt: '.format(trys)))
            except ValueError:
                print('Please enter a valid number.')
                continue
            if guess > 99:
                print('The number needs to be lower or equal a 99!')
            elif guess < 1:
                print('The number needs to be higher or equal a 1!')
            else:    
                if guess == x:
                    print('\033[1m' + '\033[92m' + 'Congrats, you guessed the number correctly!' + '\033[0m') 
                    win = 1
                    cont = 1
                    win_streak += 1
                    save_value(win_streak, streak_name) 
                elif guess > x:
                    print('The number is ' + '\033[4m' + 'lower!' + '\033[0m')
                    trys += 1
                elif guess < x:
                    print('The number is ' + '\033[4m' + 'higher!' + '\033[0m')
                    trys += 1

        if trys > max_trys :
            print('\033[1m' + '\033[91m' + 'Game Over, the correct number it was ' + '\033[4m' + '{}'.format(x) + '\033[0m')
            cont = 1
            win_streak = 0
            save_value(win_streak, streak_name)
        
        print('\nYour win Streak: {}\n'. format(win_streak))
            
        if cont == 1:
            while True: 
                play_more = input('Do you want play more? (y/n): ')
                if play_more == 'y' or play_more == 'Y' or play_more == 'n' or play_more == 'N':
                    break
            if play_more == 'y' or play_more == 'Y':
                main()
            else:
                print('Exiting...')
        
    except ValueError:
        print('\033[91m' + 'Erro, tem de colocar um nº válido' + '\033[0m')
        
if __name__ == "__main__":
    main()