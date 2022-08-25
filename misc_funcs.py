from manim import *  # includes np
from typing import Tuple


def rotate_vector_acw(vector, angle):
    """
    :param vector: a 2 length numpy array
    :param angle: an anti clockwise angle
    :return: the vector rotated anticlockwise by angle
    """
    angle = angle * np.pi / 180

    rotation = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    return rotation.dot(vector)


def cut_matrix(matrix, start, end):
    """
    Given a 2d list (matrix)
    Returns a matrix cut from a top left position (start)
        to a bottom right position (end)
    """

    new_matrix = []
    difference = (end[0]-start[0], end[1]-start[1])

    for x in range(difference[1]):
        row = []
        for y in range(difference[0]):
            try:
                row.append(matrix[start[1]+x][start[0]+y])
            except IndexError:
                return None

        new_matrix.append(row)

    return new_matrix


def coordinates_to_matrix(coordinates, dimensions):
    matrix = np.full(shape=dimensions, fill_value=0)
    for coord in coordinates:
        matrix[coord] = 1
    return matrix.T  # coordinates are flipped for numpy matrix so transpose


def cubic_s_distribution(x):
    # gradient 0 at x=0 and x=1
    # goes through (0, 0) and (1, 1)
    return -2*(x**3) + 3*(x**2)


def random_in_range(range_min, range_max, distribution_func=lambda x: x):
    return distribution_func(np.random.random())*(range_max-range_min) + range_min


def random_offset_position(start: Tuple[int, int, int], width, height, distribution_func=lambda x: x) -> Tuple[int, int, int]:
    # returns random location all directions from start, within width and height
    start = np.array(start)
    padding_h, padding_w = height/5, width/5

    random_x = random_in_range(-width/2 + padding_w, width/2 - padding_w, distribution_func)
    random_y = random_in_range(-height/2 + padding_h, height/2 - padding_h, distribution_func)

    offset = np.array([random_x, random_y, 0])
    return tuple(start + offset)


def line_centerer(text, width=17, font_size=30, **kwargs):
    """
    Splits and centers a single line of text to multiple lines based on width.
    """
    text_group = VGroup()
    newest_line = []
    # add new lines automatically
    for word in text.split(" "):
        current_line_text_obj = Text(" ".join(newest_line + [word]))
        if current_line_text_obj.width > width:
            new_line_text = Text(" ".join(newest_line), font_size=font_size, **kwargs)
            text_group.add(new_line_text)

            newest_line = [word]
        else:
            newest_line.append(word)
    new_line_text = Text(" ".join(newest_line), font_size=font_size, **kwargs)
    text_group.add(new_line_text)
    text_group.arrange(DOWN, center=True)
    return text_group
