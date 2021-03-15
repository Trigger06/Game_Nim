from Game_Nim.function import arrange_the_stones
from Game_Nim.function import take_stones
from Game_Nim.function import position_stones
from Game_Nim.function import isLose



player_1 = input('Первый игрок представься ')
player_2 = input('Второй игрок представься ')
user_name = player_1

arrange_the_stones()
while True:
    print(position_stones())
    print('Ходит игрок', user_name)
    position = input('Какой ряд ты выбираешь? ')
    quantity = input('Сколько хочешь взять? ')
    take_stones(position=int(position), quantity=int(quantity))
    if user_name == player_1: user_name = player_2
    else: user_name = player_1
    if isLose():
        break

print('Победил игрок ', user_name)
