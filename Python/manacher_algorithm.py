"""
    Manacher's Algorithm is one of the most efficient way
    to find the longest palindromic substring of a given string
    in linear space and time!!!
"""


# To add Stars before and after each character.
def add_star(s):
    arr = ['*']
    for i in s:
        arr.append(i)
        arr.append('*')
    return arr


# To remove Stars from the longest palindromic substring
def remove_stars(s):
    result = []
    for i in s:
        if i != '*':
            result.append(i)
    return ''.join(result)


# Longest Substring can be calculated by finding the character
# with the maximum value of the length and longest substring is
# character including both sides equal to maximum length
def longest_palindromic_substring(string, arr, n):
    mirror, length = 0, 0
    for i in range(n):
        if arr[i] > length:
            length = arr[i]
            mirror = i
    # Optimal substring is found. We just need to remove stars to get
    # actual palindromic substring.
    return remove_stars(string[mirror-length:mirror+length+1])


def manacher_algorithm(s):
    temp = add_star(s)
    n = len(temp)
    L = [0] * n  # To store the length of longest palindrome from a given position.
    mirror = 0  # To store the mirror index
    r = 0  # To store the rightmost index of a mirror's longest palindrome
    for i in range(n):
        image = 2 * mirror - i  # To get the image of i from the mirror index
        if i < r:
            L[i] = min(r - i, L[image])
        try:
            while temp[i + 1 + L[i]] == temp[i - 1 - L[i]]:
                L[i] += 1
        except:
            pass
        if i + L[i] > r:
            mirror = i
            r = i + L[i]
    print(L)
    return longest_palindromic_substring(temp, L, n)


# output will be "abaaba" since complete string is palindrome
print(manacher_algorithm("abaaba"))
