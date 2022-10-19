""" Module which helps to do simple manipulations with relations """

def reflexive_relation(matrix: list[list[int]]) -> list[list[int]]:
    """
    Finds reflexive relation of matrix.
    To be simple, changes main diagonal to 1.
    Returns matrix.

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
    Returns matrix.

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


def search_equivalence_classes(matrix: list[list[int]]) -> list[list[int]]:
    """
    Finds equivalence classes of matrix. Matrix must be symmetrical, reflexive and reflective.
    Returns list of classes. Classes are lists of ints.

    >>> search_equivalence_classes([
    ... [1, 1, 0, 0],
    ... [1, 1, 0, 0],
    ... [0, 0, 1, 0],
    ... [0, 0, 0, 1]
    ... ])
    [[1, 2], [3], [4]]

    >>> search_equivalence_classes([
    ... [1, 0, 1, 1],
    ... [0, 1, 0, 0],
    ... [1, 0, 1, 1],
    ... [1, 0, 1, 1]
    ... ])
    [[1, 3, 4], [2]]
    """
    classes = [set() for _ in range(len(matrix))]

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 1:
                classes[i].add(j + 1)
                classes[j].add(i + 1)


    # delete repeating classes
    unique_classes = []
    for i in classes:
        list_class = list(i)

        if list_class not in unique_classes:
            unique_classes.append(list_class)


    return unique_classes
