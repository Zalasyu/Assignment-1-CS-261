import pytest
from assignment1 import *
from static_array import *

def test_min_max_avg_case():
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
         arr[i] = value
    assert min_max(arr) == (-5,8)

def test_min_max_one_ele():
    arr = StaticArray(1)
    arr[0] = 100
    assert min_max(arr) == (100, 100)

def test_min_max_all_same_values():
    arr = StaticArray(3)
    arr[0] = 3
    arr[1] = 3
    arr[2] = 3
    assert min_max(arr) == (3,3)

def test_min_max_neg_and_zero():
    arr = StaticArray(5)
    for i, value in enumerate([-10, -30, -5, 0, -10]):
         arr[i] = value
    assert min_max(arr) == (-30, 0)

def test_fizz_buzz_avg_case(capfd):
    source = [val for val in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
         arr[i] = value

    print(arr)
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 7 [-5, -1, 3, 7, 11, 15, 19]\n"

    print(fizz_buzz(arr))
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 7 ['buzz', -1, 'fizz', 7, 11, 'fizzbuzz', 19]\n"

def test_reverse(capfd):
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
         arr.set(i, value)

    print(arr)
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 6 [-20, -13, -6, 1, 8, 15]\n"

    reverse(arr)
    print(arr)
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 6 [15, 8, 1, -6, -13, -20]\n"

    reverse(arr)
    print(arr)
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 6 [-20, -13, -6, 1, 8, 15]\n"
    
def test_rotate_1(capfd):
    source = [x for x in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
         arr.set(i, value)

    print(arr)
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 6 [-20, -13, -6, 1, 8, 15]\n"
    
    print(rotate(arr,1), 1)
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 6 [15, -20, -13, -6, 1, 8] 1\n"

    print(rotate(arr, 2), 2)
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 6 [8, 15, -20, -13, -6, 1] 2\n"

    print(rotate(arr, 0), 0)
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 6 [-20, -13, -6, 1, 8, 15] 0\n"

    print(rotate(arr, -1), -1)
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 6 [-13, -6, 1, 8, 15, -20] -1\n"

    print(rotate(arr, -2), -2)
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 6 [-6, 1, 8, 15, -20, -13] -2\n"

    print(rotate(arr, 28), 28)
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 6 [-6, 1, 8, 15, -20, -13] 28\n"

    print(rotate(arr, -100), -100)
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 6 [8, 15, -20, -13, -6, 1] -100\n"

    print(rotate(arr, 2**28), 2**28)
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 6 [-6, 1, 8, 15, -20, -13] 268435456\n"

    print(rotate(arr, -2**31), -2**31)
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 6 [-6, 1, 8, 15, -20, -13] -2147483648\n"

    print(arr)
    out, err = capfd.readouterr()
    assert out == "STAT_ARR Size: 6 [-20, -13, -6, 1, 8, 15]\n"

def test_sa_range(capfd):
    cases = [
     (1, 3), (-1, 2), (0, 0), (0, -3),
     (-105, -99), (-99, -105)
    ]
    expected = ["1 3 STAT_ARR Size: 3 [1, 2, 3]\n",
                "-1 2 STAT_ARR Size: 4 [-1, 0, 1, 2]\n",
                "0 0 STAT_ARR Size: 1 [0]\n",
                "0 -3 STAT_ARR Size: 4 [0, -1, -2, -3]\n",
                "-105 -99 STAT_ARR Size: 7 [-105, -104, -103, -102, -101, -100, -99]\n",
                "-99 -105 STAT_ARR Size: 7 [-99, -100, -101, -102, -103, -104, -105]\n"
                ]
    i = 0
    for start, end in cases:
         print(start, end, sa_range(start, end))
         out, err = capfd.readouterr()
         assert out == expected[i]
         i += 1


def test_is_sorted(capfd):
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple'])

    expected = ["Result: 1 STAT_ARR Size: 8 [-100, -8, 0, 2, 3, 10, 20, 100]\n",
                "Result: 1 STAT_ARR Size: 5 ['A', 'B', 'Z', 'a', 'z']\n",
                "Result: 2 STAT_ARR Size: 5 ['Z', 'T', 'K', 'A', '5']\n",
                "Result: 0 STAT_ARR Size: 6 [1, 3, -10, 20, -30, 0]\n",
                "Result: 0 STAT_ARR Size: 6 [-10, 0, 0, 10, 20, 30]\n",
                "Result: 2 STAT_ARR Size: 5 [100, 90, 0, -90, -200]\n",
                "Result: 1 STAT_ARR Size: 1 ['apple']\n"
                ]
    count = 0
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)
        out, err = capfd.readouterr()
        assert out == expected[count]
        count += 1

def test_sa_sort(capfd):
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)],
        [random.randint(-10**7, 10**7) for _ in range(5_000)])

    expected = ["STAT_ARR Size: 9 [1, 10, 2, 20, 3, 30, 4, 40, 5]\n",
                "STAT_ARR Size: 9 [1, 2, 3, 4, 5, 10, 20, 30, 40]\n",
                "STAT_ARR Size: 5 ['zebra2', 'apple', 'tomato', 'apple', 'zebra1']\n",
                "STAT_ARR Size: 5 ['apple', 'apple', 'tomato', 'zebra1', 'zebra2']\n",
                "STAT_ARR Size: 4 [(1, 1), (20, 1), (1, 20), (2, 20)]\n",
                "STAT_ARR Size: 4 [(1, 1), (1, 20), (2, 20), (20, 1)]\n",
                "Started sorting large array\n",
                "Finished sorting large array\n" ]

    count = 0
    for case in test_cases:
        arr = StaticArray(len(case))

        for i, value in enumerate(case):
            arr[i] = value

        print(arr if len(case) < 50 else 'Started sorting large array')
        out, err = capfd.readouterr()
        assert out == expected[count]
        sa_sort(arr)
        print(arr if len(case) < 50 else 'Finished sorting large array')
        out, err = capfd.readouterr()
        assert out == expected[count + 1]
        count += 2



