import random
heap = []
# from main_ import player_1, player_2


def arrange_the_stones():
    global heap
    heap = []
    for _ in range(5):
        heap.append(random.randint(5, 20))


def take_stones(position, quantity):
    while True:
        if 1 <= position <= len(heap):
            heap[position - 1] -= quantity
            break


def position_stones():
    return heap


def isLose():
    return sum(heap) == 0
