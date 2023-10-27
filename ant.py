from PIL import Image
import numpy as np

# Инициализация
size = 1024
field = np.zeros((size, size), dtype=np.uint8)
x, y = size // 2, size // 2
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Вверх, вправо, вниз, влево
direction = 0  # Начальное направление - вверх

# Цикл движения муравья
while 0 <= x < size and 0 <= y < size:
    if field[y, x] == 0:  # Если клетка белая
        direction = (direction + 1) % 4  # Поворот по часовой стрелке
    else:  # Если клетка черная
        direction = (direction - 1) % 4  # Поворот против часовой стрелки
    field[y, x] = 1 - field[y, x]  # Инвертирование цвета клетки
    x, y = x + directions[direction][0], y + directions[direction][1]  # Перемещение муравья

# Создание и сохранение изображения
img = Image.fromarray(field * 255, 'L')
img.save('ant_path.png')

# Подсчет количества черных клеток
black_cells = np.sum(field)
print('Число черных клеток:', black_cells)
