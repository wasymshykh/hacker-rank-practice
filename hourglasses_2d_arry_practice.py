"""
    Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.
"""

import math


def print_other(o_arr, maximum):
    print("------")
    flag = True
    m = 0
    for ii in range(0, len(o_arr)):
        for jj in range(0, len(o_arr[ii])):
            print(str(o_arr[ii][jj]) + " ", end="")
            if ii == 0 or ii == 2 or (ii == 1 and jj == 1):
                m += o_arr[ii][jj]

        print("")
    if flag:
        if m > maximum:
            return m
    return max


if __name__ == "__main__":

    mx = -math.inf

    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

    for r in range(0, len(arr) - 2):
        for c in range(0, len(arr[r]) - 2):
            other = []
            for i in range(r, r + 3):
                other.append([])
                for j in range(c, c + 3):
                    other[i - r].append(arr[i][j])
            mx = print_other(other, mx)

    print(mx)
