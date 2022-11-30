import pygame

"""

Функция "check_seed" отслеживает семечки (съел ли пакман семечко, обновляет очки и выводит их на экран)

matrix - непосредственно наша матрица
counter_of_seeds - количество очков
position = [x, y] - позиция пакмана

Функция возвращает массив, в котором:
1 значение - обновлённое количество очков (следовательно надо в main перезаписать это значение, чтобы потом вновь его передать)
2 значение - булевое значение, было ли семечко съедено

"""


def check_seed(position, matrix, points, screen):
    if matrix[position[0]][position[1]] == 2:
        points += 2
        r = [points, True]
    elif matrix[position[0]][position[1]] == 4:
        points += 5
        r = [points, True]
    else:
        r = [points, False]

    f = pygame.font.Font(None, 42)
    text = f.render(str(12), 1, (255, 255, 255))
    screen.blit(text, (740, 15))

    return r
