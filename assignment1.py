# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:

import random
import string
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> ():
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 7 - SA_SORT -----------------------------------


def sa_sort(arr: StaticArray) -> None:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 10 - SA_INTERSECTION --------------------------


def sa_intersection(arr1: StaticArray, arr2: StaticArray, arr3: StaticArray) \
        -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 11 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 12 - ADD_NUMBERS ------------------------------


def add_numbers(arr1: StaticArray, arr2: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 13 - SPIRAL MATRIX -------------------------


def spiral_matrix(rows: int, cols: int, start: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 14 - TRANSFORM_STRING -------------------------


def transform_string(source: str, s1: str, s2: str) -> str:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))


    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))


    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(min_max(arr))


    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)


    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)


    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2**28, -2**31]:
        print(rotate(arr, steps), steps)
    print(arr)


    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10**9, 10**9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3**14)
    rotate(arr, -3**15)
    print(f'Finished rotating large array of {array_size} elements')


    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))


    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)


    print('\n# sa_sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)],
        [random.randint(-10**7, 10**7) for _ in range(5_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        sa_sort(arr)
        print(arr if len(case) < 50 else 'Finished sorting large array')


    print('\n# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)


    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = count_sort(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')


    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')


    print('\n# sa_intersection example 1')
    test_cases = (
        ([1, 2, 3], [3, 4, 5], [2, 3, 4]),
        ([1, 2], [2, 4], [3, 4]),
        ([1, 1, 2, 2, 5, 75], [1, 2, 2, 12, 75, 90], [-5, 2, 2, 2, 20, 75, 95])
    )
    for case in test_cases:
        arr = []
        for i, lst in enumerate(case):
            arr.append(StaticArray(len(lst)))
            for j, value in enumerate(sorted(lst)):
                arr[i][j] = value
        print(sa_intersection(arr[0], arr[1], arr[2]))


    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)


    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10**9, 10**9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')


    print('\n# add_numbers example 1')
    test_cases = (
        ([1, 2, 3], [4, 5, 6]),
        ([0], [2, 5]), ([0], [0]),
        ([2, 0, 9, 0, 7], [1, 0, 8]),
        ([9, 9, 9], [9, 9, 9, 9])
    )
    for num1, num2 in test_cases:
        n1 = StaticArray(len(num1))
        n2 = StaticArray(len(num2))
        for i, value in enumerate(num1):
            n1[i] = value
        for i, value in enumerate(num2):
            n2[i] = value
        print('Original nums:', n1, n2)
        print('Sum: ', add_numbers(n1, n2))


    print('\n# spiral matrix example 1')
    matrix = spiral_matrix(1, 1, 7)
    print(matrix)
    if matrix: print(matrix[0])
    matrix = spiral_matrix(3, 2, 12)
    if matrix: print(matrix[0], matrix[1], matrix[2])


    print('\n# spiral matrix example 2')
    def print_matrix(matrix: StaticArray) -> None:
        rows, cols = matrix.size(), matrix[0].size()
        for row in range(rows):
            for col in range(cols):
                print('{:4d}'.format(matrix[row][col]), end=' ')
            print()
        print()

    test_cases = (
        (4, 4, 1), (3, 4, 0), (2, 3, 10), (1, 2, 1), (1, 1, 42),
        (4, 4, -1), (3, 4, -3), (2, 3, -12), (1, 2, -42),
    )
    for rows, cols, start in test_cases:
        matrix = spiral_matrix(rows, cols, start)
        if matrix: print_matrix(matrix)


    print('\n# transform_strings example 1')
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
                  'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
                  'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
                  'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
                  'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
                  'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
                  'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
                  'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
                  'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
                  'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
                  'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')
    for case in test_cases:
        print(transform_string(case, '612HZ', '261TO'))
