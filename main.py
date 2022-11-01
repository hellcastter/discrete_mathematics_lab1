""" Module which helps to do simple manipulations with relations """

# 1st task
def read_matrix(file_name: str) -> list[list[int]]:
    """ Reads and returns matrix from .txt file """
    with open(file_name, encoding='utf-8') as file:
        matrix = file.read().split('\n')

    result = []

    for row in matrix:
        integer_row = list(map(int, row))
        result.append(integer_row)

    return result

def write_matrix(matrix: list[list[int]], file_name: str):
    """
    Creates a new file in which overwrites the input matrix according to the conditions
    """
    string = ''
    for row in matrix:
        string += ''.join(str(n) for n in row) + '\n'

    with open(file_name, 'w', encoding = 'utf-8') as file:
        file.write(string.strip())


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


# 3rd task
def transitive_closure(matrix: list[list[int]]) -> list[list[int]]:
    """
    Turns matrix into transitive relation according to Warshall's algorithm

    >>> transitive_closure([[0, 0, 0, 0], [1,0, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0]])
    [[0, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]]
    """
    size = len(matrix)
    size_range = range(size)

    for k in size_range:
        for i, row in enumerate(matrix):
            if i == k:
                continue

            if row[k] == 0:
                continue

            for j, col in enumerate(row):
                matrix[i][j] = col or matrix[k][j]

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
    Сhecks whether the relation is transitive one according to Warshall's algorithm.

    >>> is_transitive([[1,1,1,1], [1,1,1,1], [0,0,0,1], [0,0,0,0]])
    True
    >>> is_transitive([[1,1,1,1], [1,1,1,1], [0,1,0,1], [1,0,1,0]])
    False
    """
    size = len(matrix)
    size_range = range(size)

    for k in size_range:
        for row in size_range:
            if row == k:
                continue

            if matrix[row][k] == 0:
                continue

            for col in size_range:
                temp = matrix[row][col]
                new_value = matrix[row][col] or matrix[k][col]

                if temp != new_value:
                    return False

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
    n = 5: 94.90624475479126

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
