# Course: CS261 - Data Structures
# Student Name: Alec Moldovan
# Assignment: 1
# Description: The purpose of this assignment is to give you practice with programming in Python.

import random
import string
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> ():
    """
    INPUT: A StaticArray object
    MECHANICS: Iterate through each element and find the max and min value 
    OUTPUT: Tuple (min, max)
    """
    max = arr.get(0)
    min = arr.get(0)


    # Find the max value
    for idx in range(arr.size()):
        if max < arr.get(idx):
            max = arr.get(idx)

    # Find the min value
    for idx in range(arr.size()):
        if min > arr.get(idx):
            min = arr.get(idx)

    return (min, max)


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    INPUT: A StaticArray object
    MECHANICS: Iterate through array
                1) If number in the array is divisible by 3, the corresponding element in the 
                new array should be the string ‘fizz’.
                2) If number in the array is divisible by 5, the corresponding element in the 
                new array should be the string ‘buzz’.
                3) If number in the array is both a multiple of 3 and a multiple of 5, the 
                corresponding element in the new array should be the string ‘fizzbuzz’.
                4) In all other cases, the element in the new array should have the same value as in the original array
    OUTPUT: A StaticArray object
    """
    new_arr = StaticArray(arr.size())
    for idx in range(arr.size()):

        # Check if number is divisble by 3
        if (arr[idx] % 3 == 0) and (arr[idx] % 5 != 0):
            new_arr[idx] = "fizz"

        # Check if number is divisble by 5
        elif (arr[idx] % 5 == 0) and  (arr[idx] % 3 != 0):
            new_arr[idx] = "buzz"

        # Check if number is divisble by 3 and 5
        elif (arr[idx] % 3 == 0) and (arr[idx] % 5 == 0):
            new_arr[idx] = "fizzbuzz"

        # If number is not divisble by 3 or 5
        else:
            new_arr[idx] = arr[idx]

    return new_arr

# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """
    INPUT: A StaticArray Object
    MECHANICS: Reverses the order of a StaticArray object's list (IN-PLACE)
    OUTPUT: A reversed StaticArray Object's list
    """
    j = arr.size() - 1
    i = 0
    while (i < j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        i += 1
        j -= 1
    return None




# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    INPUT: A StaticArray object AND number of shift (+int = right shift; -int = left shift)
    MECHANICS: Takes the mod of steps by the array size,
                since a rotation of either direction equal to the size outputs the same array. 
                Assign real_rot to steps % array size
            ex. 
                array size = 4
                steps = 9
                real_rot = 1

                Two times the same list is seen.
                Thereby skip to second full rotation and rotate once to the right.
    OUTPUT: A new StaticArray object with its list shifted left or right units.
    """
    # How many times do we see the same original array?
    # Rotate the remainder steps and that is your final rotated array
    size=arr.size()
    result = StaticArray(size)

    for i in range(size):
        result[i] = arr[i]


    if steps>0:
        # rotate right
        for i in range(size):
            result[i]=arr[((i-steps) % size + size) % size]
    elif steps<0:
        # rotate left
        for i in range(arr.size()):
            result[((i+steps) % size + size) % size] = arr[i]
    return result

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """
    INPUT: Two integers

    MECHANICS: 
                1. Find the number of elements expected => range
                2. Create a StaticArray of size range
                3. Stepwise increment the value from start value to end if end > start; Otherwise decrement.

    OUTPUT: A StaticArray object that contains a sequence of integers from start to end variables' values
    """
    range = abs((end-start)) + 1
    arr = StaticArray(range)
    step = 0
    while step < range:
        arr[step] = start
        step += 1
        if end < start:
            start -= 1
        else:
            start += 1
    return arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """
    INPUT: A StaticArray Object
    MECHANICS:
    OUTPUT:[0,1,2]; 0 = Not sorted; 1 = ascending order; 2 = descending order
    """
    size = arr.size()

    # import pdb; pdb.set_trace()
    if size == 1:
        return 1
    # Checking if list descends 
    elif arr[0] > arr[size - 1]:

        for i in range(1,size - 1):
            # Check if an a previous element is smaller than the current element
            if  arr[i-1] <= arr[i]:
                return 0
        return 2
    # Check if list ascends
    elif arr[0] < arr[size - 1]:

        for i in range(1,size - 1):
            # Check if an a previous element is bigger than the current element
            if arr[i-1] >= arr[i]:
                return 0
        return 1


# ------------------- PROBLEM 7 - SA_SORT -----------------------------------


def sa_sort(arr: StaticArray) -> None:
    """
    INPUT: A StaticArray object (unsorted)
    MECHANICS:
    OUTPUT: A sorted ascending ordered StaticArray object list
    """
    size = arr.size()
    if size > 1:
        # Floor division
        mid = size//2
        if size % 2 == 0:
            low = StaticArray(mid)
            high = StaticArray(mid)
        else:
            low = StaticArray(mid)
            high = StaticArray(mid+1)

        # Initialize low end StaticArray
        for idx in range(0, mid):
            low[idx] = arr[idx]


        # Initialize high end StaticArray
        for count, idx in enumerate(range(mid, size)):
            high[count] = arr[idx]


        sa_sort(low)
        sa_sort(high)
        
        i = 0
        j = 0
        k = 0

        while i < low.size() and j < high.size():
            if low[i] < high[j]:
                arr[k] = low[i]
                i += 1
            else:
                arr[k] = high[j]
                j += 1
            k += 1
        while i < low.size():
            arr[k] = low[i]
            i += 1
            k += 1

        while j < high.size():
            arr[k] = high[j]
            j += 1
            k += 1

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    INPUT: A StaticArray object (Elements are sorted)
    MECHANICS: Takes out duplicates from StaticArray Object
    OUTPUT: A sort StaticArray object with no duplicates
    """
    size = arr.size()
    new_arr = StaticArray(size)

    if size == 1:
        return arr

    new_arr[0] = arr[0]
    for i in range(1, size):
        if arr[i] != arr[i-1]:
            new_arr[i] = arr[i]

    count_Nones = 0
    for i in range(size):
        if new_arr[i] == None:
            count_Nones += 1

    final_size = size - count_Nones
    final_arr = StaticArray(final_size)

    # import pdb; pdb.set_trace()
    final_arr[0] = new_arr[0]
    count = 1
    i = 1
    while i < final_size:
        if new_arr[count] == None:
            count += 1
        else:
            final_arr[i] = new_arr[count]
            i += 1
            count += 1


    return final_arr



# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    INPUT: A StaticArray (Contains a list of integers (+/-) from -10^9 to +10^9)
    MECHANICS: Perform a non-comparison sort
    OUTPUT: A sorted Static
    """
    size = arr.size()
    # We must assume any of the possible elements are possible.
    max = -int(10**9)
    min = int(10**9)

    # Find the max and min value in the passed StaticArray
    for i in range(size):
        if min > arr[i]:
            min = arr[i]
        if max < arr[i]:
            max = arr[i]

    # Offset the max value due to negative values present
    max = (max - min) + 1

    # Create our count and output StaticArray objects
    count = StaticArray(max)
    out_arr = StaticArray(size)

    # Fill count array with zeros
    for i in range(count.size()):
        count[i] = 0

    # Track occurences of each unique element in passed StaticArray
    for i in range(size):
        val = count[arr[i] -min]
        count.set(arr[i] - min, val + 1)

    # Get the Running Sum
    # This will help for placement later
    # We sum the value of the previous index with the value of the current index
    # The value at that index represents that there is/are 'value' occurenes of values 
    #                   less than or equal to the index value
    for i in range(1, max):
        count.set(i, count[i] + count[i-1])


    # Start working backwards on the array and forwards on the count array.
    # This finds the index of each integer of the OG array in the our count array
    # Placement Commences
    i = size - 1
    while i >= 0:
        # Descending Order
        idx = count[arr[i] - min] - 1
        out_arr.set(size - idx -1, arr[i])

        count.set(arr[i] - min, count[arr[i] - min] - 1)
        i -= 1
    return out_arr



# ------------------- PROBLEM 10 - SA_INTERSECTION --------------------------
def countNones(arr:StaticArray) -> StaticArray:
    """
    INPUT: A StaticArray object
    MECHANICS: Resize the passed StaticArray object that may contian Nones in it
                to a new StaticArray object with no Nones
    OUTPUT: A StaticArray with no None elements
    """
    size = arr.size()
    count_Nones = 0
    for i in range(size):
        if arr[i] == None:
            count_Nones += 1

    final_size = size - count_Nones
    final_arr = StaticArray(final_size)

    # import pdb; pdb.set_trace()
    final_arr[0] = arr[0]
    count = 1
    i = 1
    while i < final_size:
        if arr[count] == None:
            count += 1
        else:
            final_arr[i] = arr[count]
            i += 1
            count += 1
    return final_arr

def sa_intersection(arr1: StaticArray, arr2: StaticArray, arr3: StaticArray) \
        -> StaticArray:
    """
    INPUT: Three Sorted StaticArray Objects
    MECHANICS: Filter out elements not shared by all three StaticArray objects
    OUTPUT: A StaticArray object that is the intersection of all three StaticArray  objects
    """
    # Preprocess arrays
    tot_size = int(arr1.size() + arr2.size() + arr3.size())
    size1 = arr1.size()
    size2 = arr2.size()
    size3 = arr3.size()

    match_arr = StaticArray(tot_size)

    # No Matches array
    no_arr = StaticArray(1)

    # If the combined arr is less than 3, then an element is not shared by all arrays.
    if match_arr.size() < 3:
        return no_arr
    #initialize
    idx = 0
    i=j=k=0
    while((i<size1) and (j<size2) and (k < size3)):
        if ((arr1[i] == arr2[j]) and (arr2[j] == arr3[k])):
            match_arr[idx] = arr1[i]
            idx += 1
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    if match_arr[0] == None:
        return no_arr

    final_arr = countNones(match_arr)


    return final_arr



# ------------------- PROBLEM 11 - SORTED SQUARES ---------------------------



def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    INPUT: A StaticArray Object
    MECHANICS: Square each element and resort
    OUTPUT: A sorted StaticArray with elements squared from previous StaticArray object
    """
    pass


# ------------------- PROBLEM 12 - ADD_NUMBERS ------------------------------


def add_numbers(arr1: StaticArray, arr2: StaticArray) -> StaticArray:
    """
    INPUT: Two StaticArray objects (Represents positive numbers)
    MECHANICS: Add digits together as a regular addition with carry over capabilities
    OUTPUT: A StaticArray object with the new represented number
    """
    tot_size = arr1.size() + arr2.size()
    temp_arr = StaticArray(tot_size)
    # Account for different sized arrays
    if arr1.size() > arr2.size():
        temp_arr2 = StaticArray(arr1.size())

        for i in range(temp_arr2.size()):
            temp_arr2[i] = 0

        if arr2.size() == 1:
            idx_arr2 = 1
        else:
            idx_arr2 = temp_arr2.size() - arr2.size()

        i = 0
        while(idx_arr2 < temp_arr2.size() and i < arr2.size()):
            temp_arr2[idx_arr2] = arr2[i]
            i += 1
            idx_arr2 += 1

        arr2 = temp_arr2
    elif arr2.size() > arr1.size():
        temp_arr1 = StaticArray(arr2.size())

        for i in range(temp_arr1.size()):
            temp_arr1[i] = 0

        if arr1.size() == 1:
            idx_arr1 = 1
        else:
            idx_arr1 = temp_arr1.size() - arr1.size()

        i = 0
        while(idx_arr1 < temp_arr1.size() and i < arr1.size()):
            temp_arr1[idx_arr1] = arr1[i]
            i += 1
            idx_arr1 += 1

        arr1 = temp_arr1
        

    # Add Digits!
    idx1 = arr1.size() - 1
    idx2 = arr2.size() - 1
    carry_over = 0
    idx = temp_arr.size() - 1
    while ((idx1 >= 0) and (idx2 >= 0)):
        sum = carry_over + arr1[idx1] + arr2[idx2]
        carry_over = int(sum /10)
        temp_arr[idx] = sum % 10
        idx -= 1
        idx1 -= 1
        idx2 -= 1
    if carry_over != 0:
        temp_arr[idx] = carry_over

    idx = 0
    for i in range(tot_size):
        if temp_arr[i] != None:
            temp_arr[idx] = temp_arr[i]
            temp_arr[i] = None
            idx += 1

    final_arr = countNones(temp_arr)

    
    return final_arr







# ------------------- PROBLEM 13 - SPIRAL MATRIX -------------------------

def spiral_matrix(rows: int, cols: int, start: int) -> StaticArray:
    """
    INPUT: Three integers (# rows, # cols, #start int)
    MECHANICS: 
                1. Create a 2D matrix (StaticArray of StaticArrays [rows x cols])
                2. Fill Matrix by increment of one
                3. Neg start integer starts at pos bottom left
                        and 
                  Positive start integer starts ar pos top right
                4. Postive start int spiral clockwise to center
                        and
                  Negative start integer sprials counterclockwise to center
    OUTPUT: A Spirally-filled 2D Matrix
    """
    pass

# ------------------- PROBLEM 14 - TRANSFORM_STRING -------------------------


def transform_string(source: str, s1: str, s2: str) -> str:
    """
    INPUT: Three strings (source [to be translated], s1 [trigger], s2 [replacement])
    MECHANICS: Source should be processed one character at 
    a time, and the output string should be constructed according to the following rules:
    1) If the character from the source string is present in s1, it should be replaced by the 
    character at the same index in s2.
    2) Otherwise, if the character is:
        a) Uppercase letter -> replace with ' '
        b) Lowercase letter -> replace with '#'
        c) Digit -> replace with '!'
        d) Anything else -> replace with '='
    OUTPUT: A transformed string
    """
    final_form = ''
    # Traverse the source and start transforming
    for ch in source:
        # Is there a trigger? Is ch in s1?
        tg_idx = s1.find(ch)
        if tg_idx >= 0:
            final_form = final_form + s2[tg_idx]
        elif ch.isupper():
            final_form = final_form + ' '
        elif ch.islower():
            final_form = final_form + '#'
        elif ch.isdigit():
            final_form = final_form + '!'
        else:
            final_form = final_form + '='
    return final_form


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
