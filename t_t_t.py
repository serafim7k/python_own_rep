import random
from colorama import init, Fore, Back, Style
init()

board = [[' ', '1', '2', '3', 'X'],
         ['1', '∎', '∎', '∎'],
         ['2', '∎', '∎', '∎'],
         ['3', '∎', '∎', '∎'],
         ['Y']]


def win():
    for w in range(1, len(board)):
        crosses_count = 0
        for n in range(1, len(board[w])):
            if board[w][n] == 'X':
                crosses_count += 1
            if crosses_count == 3:
                return 'Player won!\n'
    for w in range(1, len(board) - 1):
        crosses_count = 0
        for o in range(1, len(board) - 1):
            if board[o][w] == 'X':
                crosses_count += 1
            if crosses_count == 3:
                return 'Player won!'
    for w in range(1, len(board) - 1):
        crosses_count = 0
        for n in range(1, len(board) - 1):
            if board[n][n] == 'X':
                crosses_count += 1
            if crosses_count == 3:
                return 'Player won!'
    for w in range(1, len(board)):
        crosses_count = 0
        stat = len(board) - 2
        for n in range(1, len(board) - 1):
            if board[n][stat] == 'X':
                crosses_count += 1
                stat -= 1
            if crosses_count == 3:
                return 'Player won!'


# for y in range(1, len(board)):
#     for x in range(1, len(board[y])):
#         board[y][x] = Fore.BLUE + str(board[y][x])

for i in range(len(board)):
    print(board[i])
print()

gameRunning = True

play_with = input('I want to play with (bot / player): ')

if play_with == 'bot':
    while gameRunning:
        user_coordinates_Y = int(input('Enter Y coordinate: '))

        if user_coordinates_Y == 'n':
            gameRunning = False
            break

        user_coordinates_X = int(input('Enter X coordinate: '))

        if board[user_coordinates_Y][user_coordinates_X] != 'O':
            board[user_coordinates_Y][user_coordinates_X] = 'X'
            for i in range(len(board)):
                print(board[i])
            print()

        if_win = win()

        if if_win == 'Player won!':
            print('Player won!')
            gameRunning = False
            break
################################################################################################################
        coordinates_Y = random.randrange(1, 4)
        coordinates_X = random.randrange(1, 4)

        while board[coordinates_Y][coordinates_X] == 'X' or board[coordinates_Y][coordinates_X] == 'O':
            coordinates_Y = random.randrange(1, 4)
            coordinates_X = random.randrange(1, 4)

        if board[coordinates_Y][coordinates_X] != 'X':
            board[coordinates_Y][coordinates_X] = 'O'
            for i in range(len(board)):
                print(board[i])
            print()
else:
    while gameRunning:
        print('player_1')
        user_coordinates_Y = input('Enter Y coordinate: ')

        if user_coordinates_Y == 'n':
            gameRunning = False
            break

        user_coordinates_X = input('Enter X coordinate: ')

        user_coordinates_Y = int(user_coordinates_Y)
        user_coordinates_X = int(user_coordinates_X)

        if board[user_coordinates_Y][user_coordinates_X] != 'O':
            board[user_coordinates_Y][user_coordinates_X] = 'X'
            for i in range(len(board)):
                print(board[i])
            print()

        if_win = win()

        if if_win == 'Player won!':
            print('Player won!')
            gameRunning = False
            break
################################################################################################################
        print('player_2')
        coordinates_Y = int(input('Enter Y coordinate: '))
        coordinates_X = int(input('Enter X coordinate: '))

        if board[coordinates_Y][coordinates_X] != 'X':
            board[coordinates_Y][coordinates_X] = 'O'
            for i in range(len(board)):
                print(board[i])
            print()
