""" Module which helps to do simple manipulations with relations """

def reflexive_relation(matrix: list[list[int]]) -> list[list[int]]:
    """
    Finds reflexive relation of matrix.
    To be simple, changes main diagonal to 1

    >>> reflexive_relation([
    ...     [0, 0, 0, 1, 0],
    ...     [0, 0, 0, 1, 0],
    ...     [0, 1, 0, 0, 0],
    ...     [1, 0, 0, 0, 0],
    ...     [0, 1, 0, 1, 1]
    ... ])
    [[1, 0, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 1, 1]]

    >>> reflexive_relation([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    for i, row in enumerate(matrix):
        row[i] = 1

    return matrix

def symmetrical_relation(matrix: list[list[int]]) -> list[list[int]]:
    """
    Finds symmetrical relation. For every pair (a, b) must be (b, a) in hiccup.

    >>> symmetrical_relation([
    ...     [0, 0, 0, 1, 0],
    ...     [0, 0, 0, 1, 0],
    ...     [0, 1, 0, 0, 0],
    ...     [1, 0, 0, 0, 0],
    ...     [0, 1, 0, 1, 1]
    ... ])
    [[0, 0, 0, 1, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 1, 0, 0, 1], [0, 1, 0, 1, 1]]

    >>> symmetrical_relation([
    ...     [0, 1, 0, 1],
    ...     [0, 0, 0, 0],
    ...     [0, 1, 1, 0],
    ...     [1, 0, 1, 0],
    ... ])
    [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 1, 1], [1, 0, 1, 0]]
    """
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 1:
                matrix[j][i] = 1

    return matrix
