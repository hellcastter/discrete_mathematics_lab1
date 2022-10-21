""" Module which helps to do simple manipulations with relations """

# 2nd task
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


# 4th task
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


# 5th task
def is_transitive(matrix: list[list[int]]) -> bool:
    """
    Here must be code for checking is matrix transitive or not
    """
    return True


# 6th task
# Unfortunately, code for this task is a little complicated,
# so it may take a while to understand this

# You need to call search_transitive_count(3) function
def _apply_to_all_matrixes(size: int, callback):
    """
    Help function for "search_transitive_count" function

    Generates all possible n-size matrix and uses callback with them.
    Function should return list of all matrixes, but it doesn't, 
    so the memory and performance are saved.

    # >>> print( *_apply_to_all_matrixes(2), lambda x: x, sep="\\n" )
    # [[0, 0], [0, 0]]
    # [[0, 0], [0, 1]]
    # [[0, 0], [1, 0]]
    # [[0, 0], [1, 1]]
    # [[0, 1], [0, 0]]
    # [[0, 1], [0, 1]]
    # [[0, 1], [1, 0]]
    # [[0, 1], [1, 1]]
    # [[1, 0], [0, 0]]
    # [[1, 0], [0, 1]]
    # [[1, 0], [1, 0]]
    # [[1, 0], [1, 1]]
    # [[1, 1], [0, 0]]
    # [[1, 1], [0, 1]]
    # [[1, 1], [1, 0]]
    # [[1, 1], [1, 1]]
    """
    matrix = [[None] * size for _ in range(size)]

    def generate_binary_matrixes(num, matrix, callback, index = 0):
        """ Generate all matrixes n-size """
        if index == num ** 2:
            callback(matrix)
            return

        row = index // num
        col = index % num

        # First assign "0" at i-th position
        # and try for all other permutations
        # for remaining positions
        matrix[row][col] = 0
        generate_binary_matrixes(num, matrix, callback, index + 1)

        # And then assign "1" at i-th position
        # and try for all other permutations
        # for remaining positions
        matrix[row][col] = 1
        generate_binary_matrixes(num, matrix, callback, index + 1)

    generate_binary_matrixes(size, matrix, callback)


def search_transitive_count(size: int) -> int:
    """
    Searches number of transitive relations. There's no universal formula for this,
    so we're forced to use method of "brut force" — generate and check every possible matrix.

    On my PC execution time for:
    n = 4: 0.15617036819458008
    n = 5: 140.1703372001648

    >>> search_transitive_count(0)
    1
    >>> search_transitive_count(1)
    2
    >>> search_transitive_count(3)
    171
    >>> search_transitive_count(4)
    3994
    """
    count = 0

    def check_transitive(matrix: list[list[int]]):
        """ Help function that must be an callback """
        nonlocal count

        if is_transitive(matrix):
            count += 1

    _apply_to_all_matrixes(size, check_transitive)

    return count
