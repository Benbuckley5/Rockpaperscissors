import random

def opponent():
    wins,losses,ties = 0,0,0
    while True:
        x = random.randint(1,3)
        result = 0
        if x==1:
            result='r'
        if x==2:
            result='s'
        if x==3:
            result='p'
        print(result)
        y = input('Please enter move: ')
        if result==y:
            print('Tie!')
            ties = ties +1
        elif result=='r' and y == 's':
            print('Lose!')
            losses = losses +1
        elif result=='s' and y == 'p':
            print('Lose!')
            losses = losses +1
        elif result=='p' and y == 'r':
            print('Lose!')
            losses = losses +1
        elif result=='r' and y == 'p':
            print('Win!')
            wins = wins +1
        elif result=='s' and y == 'r':
            print('Win!')
            wins = wins +1
        elif result=='p' and y == 's':
            print('Win!')
            wins = wins +1    
        print(f'Wins: {wins}, Losses: {losses}, Ties {ties}')




opponent()

