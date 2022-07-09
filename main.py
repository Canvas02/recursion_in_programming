# Copyright 2022 Canvas02 <Canvas02@protonmail.com>.
# SPDX-License-Identifier: MIT

# Taken from video:
#    Name: Recursion in Programming - Full Course
#    Channel: freeCodeCamp.org (https://www.youtube.com/c/Freecodecamp)
#    Link: https://www.youtube.com/watch?v=IJDJ0kBx2LM

from math import floor


def main():
    data: list[int] = [-5, 20, 10, 3, 2, 0]
    merge_sort(data, 0, len(data) - 1)


def merge_sort(data: list[int], start: int, end: int) -> None:
    """!DOESN'T WORK!"""
    def merge(data: list[int], start: int, mid: int, end: int):
        # make temp to not modify original
        temp: list[int]

        i: int = start
        j: int = mid + 1
        k: int = 0

        while i <= mid and j <= end:    # while both sub-lists have values
            if data[i] <= data[j]:
                temp[k] = data[i]
                i += 1
                k += 1
            else:
                temp[k] = data[j]
                k += 1
                j += 1

        # add the rest of the values
        # left
        while i <= mid:
            temp[k] = data[i]
            k += 1
            i += 1

        # right
        while j <= end:
            temp[k] = data[j]
            k += 1
            j += 1

        i = start
        while i <= end:
            data[i] = temp[i - start]

            i += 1

    if start < end:
        mid: int = floor((start + end) / 2)
        merge_sort(data, start, mid)
        merge_sort(data, mid + 1, end)
        merge(data, start, mid, end)


def fib_no_opt(n: int) -> int:
    """fibonacci not optimized"""
    if n == 0 or n == 1:
        return n
    else:
        return fib_no_opt(n - 1) + fib_no_opt(n - 2)


def binary_search(l: list[int], left: int, right: int, x: int) -> int:
    """
    Searches for an element in a sorted list,
    returns index of element or -1 if not found
    """

    if left > right:
        return -1

    mid: int = floor((left + right) / 2)

    if x == l[mid]:
        return mid

    if x < l[mid]:
        return binary_search(l, left, mid - 1, x)
    else:
        return binary_search(l, mid + 1, right, x)


def recursive_sum(x: int, acc: int = 0) -> int:
    """
    Returns sum of digits in number
    """
    if x == 0:
        return acc

    return recursive_sum(x - 1, acc + x)


def find_binary(decimal: int, result: str = "") -> str:
    """
    Converts decimal to binary
    Edge cases:
        if given 0 returns empty string
        if given negative number throws error
    """
    if decimal == 0:
        return result

    result = str(decimal % 2) + result
    return find_binary(decimal // 2, result)


def reverse_str(input: str) -> str:
    if input == "":
        return ""

    return reverse_str(input[1:]) + input[0]


def is_palindrome(input: str) -> bool:
    if len(input) == 0 or len(input) == 1:
        return True

    if(input[0] == input[-1]):
        return is_palindrome(input[1:-1])

    return False

# ------------------------------------------------


def fact(x: int, acc: int = 1) -> int:
    if x == 0:
        return acc

    return fact(x - 1, x * acc)


def sum_of_n(n: int, acc: int = 0) -> int:
    if n == 0:
        return acc

    return sum_of_n(n // 10, n % 10 + acc)


if __name__ == "__main__":
    main()
