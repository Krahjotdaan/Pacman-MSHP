import pygame

from Map.map import Matrix
my_mat = Matrix()

gridDisplay = pygame.display.set_mode((800, 600))
def createSquare(x, y, color, grid_node_width = 20, grid_node_height = 20):
    pygame.draw.rect(gridDisplay, color, [x, y, grid_node_width, grid_node_height])

class Settings:
    BACKGROUND_COLOR = pygame.Color('black')
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    @staticmethod
    def visualizeGrid(grid_node_width = 20, grid_node_height = 20):
        grid_node_width = 20
        grid_node_height = 20
        y = 0  # мы начинаем с верхней части экрана
        for row in my_mat.get_matrix():
            x = 0  # для каждой строки мы снова начинаем с левой части экрана
            for item in row:
                if item == 1:
                    createSquare(x, y, (0, 0, 255)) # синий - стенки
                elif item == 2:
                    createSquare(x, y, (245, 245, 220)) # бежевый - маленькие семечки
                elif item == 3:
                    createSquare(x, y, (255, 0, 0)) # красный - большие семечки
                elif item == 4:
                    createSquare(x, y, (255, 165, 0)) # красный - большие семечки
                else:
                    createSquare(x, y, (0, 0, 0))

                x += grid_node_width  # для каждого элемента в этой строке мы перемещаемся на один шаг вправо
            y += grid_node_height  # для каждой новой строки мы перемещаемся на один шаг вниз
        pygame.display.update()
