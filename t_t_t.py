import random
from colorama import init, Fore, Back, Style
init()

board = [[' ', '1', '2', '3', 'X'],
         ['1', '∎', '∎', '∎'],
         ['2', '∎', '∎', '∎'],
         ['3', '∎', '∎', '∎'],
         ['Y']]


def if_x_wrong():
    if user_coordinates_X == 3:
        coordinates_X = random.randrange(user_coordinates_X - 1, user_coordinates_X + 1)
    elif user_coordinates_X == 2:
        coordinates_X = random.randrange(user_coordinates_X - 1, user_coordinates_X + 2)
    else:
        coordinates_X = random.randrange(user_coordinates_X, user_coordinates_X + 2)
    return coordinates_X


def if_y_wrong():
    if user_coordinates_Y == 3:
        coordinates_Y = random.randrange(user_coordinates_Y - 1, user_coordinates_Y + 1)
    elif user_coordinates_Y == 2:
        coordinates_Y = random.randrange(user_coordinates_X - 1, user_coordinates_X + 2)
    else:
        coordinates_Y = random.randrange(user_coordinates_Y, user_coordinates_Y + 2)
    return coordinates_Y


def win():
    for w in range(1, len(board)):
        crosses_count = 0
        for n in range(1, len(board[w])):
            if board[w][n] == 'X':
                crosses_count += 1
            if crosses_count == 3:
                return 'Player won!'
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


def lose():
    for w in range(1, len(board)):
        crosses_count = 0
        for n in range(1, len(board[w])):
            if board[w][n] == 'O':
                crosses_count += 1
            if crosses_count == 3:
                return 'Bot won!'
    for w in range(1, len(board) - 1):
        crosses_count = 0
        for o in range(1, len(board) - 1):
            if board[o][w] == 'O':
                crosses_count += 1
            if crosses_count == 3:
                return 'Bot won!'
    for w in range(1, len(board) - 1):
        crosses_count = 0
        for n in range(1, len(board) - 1):
            if board[n][n] == 'O':
                crosses_count += 1
            if crosses_count == 3:
                return 'Bot won!'
    for w in range(1, len(board)):
        crosses_count = 0
        stat = len(board) - 2
        for n in range(1, len(board) - 1):
            if board[n][stat] == 'O':
                crosses_count += 1
                stat -= 1
            if crosses_count == 3:
                return 'Bot won!'


# for y in range(1, len(board)):
#     for x in range(1, len(board[y])):
#         board[y][x] = Fore.BLUE + str(board[y][x])

for i in range(len(board)):
    print(' | '.join(board[i]))
print()

gameRunning = True

play_with = input('I want to play with (bot / player): ')

if play_with == 'bot':
    while gameRunning:
        user_coordinates_X = input('Enter X coordinate: ')

        if user_coordinates_X == 'n':
            gameRunning = False
            break

        user_coordinates_Y = input('Enter Y coordinate: ')

        user_coordinates_Y = int(user_coordinates_Y)
        user_coordinates_X = int(user_coordinates_X)

        if board[user_coordinates_Y][user_coordinates_X] != 'O':
            board[user_coordinates_Y][user_coordinates_X] = 'X'
            for i in range(len(board)):
                print(' | '.join(board[i]))
            print()

        if_win = win()

        if if_win == 'Player won!':
            print('Player won!')
            gameRunning = False
            break
################################################################################################################
        # coordinates_Y = random.randrange(1, 4)
        # coordinates_X = random.randrange(1, 4)
        coordinates_X = if_x_wrong()
        coordinates_Y = if_y_wrong()

        if gameRunning:
            while board[coordinates_Y][coordinates_X] == 'X' or board[coordinates_Y][coordinates_X] == 'O':
                coordinates_X = if_x_wrong()
                coordinates_Y = if_y_wrong()

        if board[coordinates_Y][coordinates_X] != 'X':
            board[coordinates_Y][coordinates_X] = 'O'
            for i in range(len(board)):
                print(' | '.join(board[i]))
            print()

        if_lose = lose()

        if if_lose == 'Bot won!':
            print('Bot won!')
            gameRunning = False
            break
else:
    while gameRunning:
        print('player_1')
        user_coordinates_X = input('Enter X coordinate: ')

        if user_coordinates_X == 'n':
            gameRunning = False
            break

        user_coordinates_Y = input('Enter Y coordinate: ')

        user_coordinates_Y = int(user_coordinates_Y)
        user_coordinates_X = int(user_coordinates_X)

        if board[user_coordinates_Y][user_coordinates_X] != 'O':
            board[user_coordinates_Y][user_coordinates_X] = 'X'
            for i in range(len(board)):
                print(' | '.join(board[i]))
            print()

        if_win = win()

        if if_win == 'Player won!':
            print('Player_1 won!')
            gameRunning = False
            break
################################################################################################################
        print('player_2')
        coordinates_Y = int(input('Enter Y coordinate: '))
        coordinates_X = int(input('Enter X coordinate: '))

        if board[coordinates_Y][coordinates_X] != 'X':
            board[coordinates_Y][coordinates_X] = 'O'
            for i in range(len(board)):
                print(' | '.join(board[i]))
            print()

        if_lose = lose()

        if if_lose == 'Bot won!':
            print('Player_2 won!')
            gameRunning = False
            break
input()
