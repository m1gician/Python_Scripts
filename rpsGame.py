import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.

wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop
        print('Enter your move:(r)ock (p)aper (s)cissors or (q)uit')
        PlayerMove = input()
        if PlayerMove == 'q':
            sys.exit()

        if PlayerMove == 'r' or PlayerMove == 'p' or PlayerMove == 's':
            break # break out of player input loop
        
        print('Type one of r, p, s, or q.')


    #Display what the player chose:
    if PlayerMove == 'r':
        print('ROCK versus...')
    elif PlayerMove == 'p':
        print('PAPER versus...')
    elif PlayerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)

    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')

    elif randomNumber == 2:
        computerMove ='p'
        print('PAPER')

    elif randomNumber == 3: 
        computerMove = 's'
        print('SCISSORS')
        
    # Display and record the win/loss/tie:
    if PlayerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1

    elif PlayerMove == 'r' and computerMove == 's':
        print('You win!')
        wind = wins + 1

    elif PlayerMove == 'p' and computerMove =='r':
        print('You win!')
        wins = wins + 1
    
    elif PlayerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1

    elif PlayerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1

    elif PlayerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1

    elif PlayerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1

