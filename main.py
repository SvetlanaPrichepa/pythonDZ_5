# Напишите программу, удаляющую из текста все слова, содержащие "абв".

line = 'фывабвйцу кенабвджэ, ячсабвнгш, йцукенгвба'
while ',' in line or '.' in line or ';' in line:
    line = line.replace(',', '')
    line = line.replace('.', '')
    line = line.replace(';', '')
print(line)

arr = line.split()
print(arr)

arr2 = []
for word in arr:
    if 'абв' not in word:
        arr2.append(word)
print(arr2)

data=' '.join(list(filter(lambda slovo: not 'абв' in slovo, data.split())))
print(data)

# Создайте программу для игры с конфетами человек против человека.
# Реализовать игру игрока против игрока в терминале.
# Игроки ходят друг за другом, вписывая желаемое количество конфет.
# Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил

def input_dat(name):
    x = int(
        input(f"{name}, введите количество конфет, которое возьмете от 1 до 100: "))
    while x < 1 or x > 100:
        x = int(input(f"{name}, вы ввели неправильное количество конфет, попробуйте еще раз: "))
    return x

def p_print(name, k, counter, value):
    print(
        f"Ходил {name}, он взял {k}, у него {counter}. На столе осталось {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 2)  # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 100:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")


# 2.Создайте программу для игры в ""Крестики-нолики"".
print('*'*100)
print('\n')
print('А теперь давайте сыграем в крестики нолики!')

board = list(range(1,10))

def design_board(board):
    print('-'*12)
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*12)
design_board(board)

def choice(tic_tac):
    valid = False
    while not valid:
        player_index = input('Ваш ход, выберите ячейку ' + tic_tac + ' --> ')
        try:
            player_index =int(player_index)
        except:
            print('Что то не то нажали')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(board[player_index-1]) not in 'XO'):
                board[player_index-1] = tic_tac
                valid = True
            else:
                print('Занято')
        else:
            print('Еще раз попробуй')

def victory_check(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def game(board):
    counter =0
    vic = False
    while not vic:
        design_board(board)
        if counter % 2 == 0:
            choice('X')
        else:
            choice('0')
        counter +=1
        if counter > 4:
            tt_win = victory_check(board)
            if tt_win:
                print(tt_win,'Победа')
                vic = True
                break
            if counter == 9:
                print('Победила, ДРУЖБА)')
        design_board(board)
game(board)