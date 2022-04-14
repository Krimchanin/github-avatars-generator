from PIL import Image, ImageDraw, ImageEnhance
import random


def generate(size, block_size, block_count, color=None, block_color=None):
    if color is None:
        color = '#f0f0f0'

    if block_color is None:
        block_color = _random_color()

    matrix_size = int(size / block_size) - 1
    matrix = _create_matrix(matrix_size, block_count)

    source_img = Image.new('RGB', (size, size), color=color)

    draw = ImageDraw.Draw(source_img)
    for x in range(0, matrix_size):
        for y in range(0, matrix_size):
            if not matrix[x][y]:
                continue

            block_x = ((x + 1) * block_size) - (block_size / 2)
            block_y = ((y + 1) * block_size) - (block_size / 2)

            xy_start = (block_x, block_y)
            xy_end = (block_x + block_size - 1, block_y + block_size - 1)

            draw.rectangle((xy_start, xy_end), fill=block_color)

    return source_img


def _create_matrix(size, points_count):
    matrix = [[0 for x in range(size)] for x in range(size)]

    plotted = 0
    while plotted < points_count:
        x = random.randrange(0, size)
        y = random.randrange(0, size)

        if matrix[x][y]:
            continue

        central = (x == (size / 2))

        matrix[x][y] = True
        plotted += 1

        if not central:
            matrix[size - x - 1][y] = True
            plotted += 1

    return matrix


def _random_color():
    palette_presets = [
        (225, 30, 30),
        (30, 225, 30),
        (30, 30, 225),
        (190, 60, 210),
        (220, 220, 90),
        (210, 120, 110),
        (150, 220, 225)
    ]

    r, g, b = palette_presets[random.randrange(0, len(palette_presets))]

    variation = 30
    r = min(255, max(0, r + random.randint(-variation, variation)))
    g = min(255, max(0, g + random.randint(-variation, variation)))
    b = min(255, max(0, b + random.randint(-variation, variation)))

    return r, g, b
