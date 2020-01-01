"""
    The user enters a string and a substring. 
    You have to print the number of times that the substring occurs in the given string. 
    String traversal will take place from left to right, not from right to left.
"""

def count_substring(string: str, sub_string):
    start = 0
    end = len(string)
    count = 0

    while True:
        i = string.find(sub_string, start, end)
        if i == -1:
            break
        start = i + 1
        count += 1
    return count
