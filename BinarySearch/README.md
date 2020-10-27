# Problem:
Given a sorted array of integers, we need to find whether a certain integer exists in it or not. If it does, return the index else return -1. The complexity must be O(log~2~n).
So we need to make a function named binary_search which takes the arguments -- the array and integer to search, the first and the last index of the range to search from the array.
# Example/TestCases:
Consider this array: [1,2,5,7,8]
Now, if we search for 4, we get -1 in return. If we search for 7 we get 3 (index of 7 is three).
Consider this array: [2,3,4,5,7,10]
Binary search will return -1 for input 6 and, 0 for input 2.