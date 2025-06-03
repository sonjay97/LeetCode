"""
Author: @jay.shah
Date: June 3, 2025

# Problem

This problem is covertly asking us to do a modified binary search. The reason I say "covertly" is because at the very end of the problem statement, it says "you must write an algorithm that runs in O(log n) time". This is key giveaway. O(log n) time constraints almost always mean search optimization using binary search. awesome. now I know that the question is asking me to perform binary search on a rotated array that can be rotated 1 to n times. That means the array will be rotated at least once. I don't need to worry about cases where the array is NOT rotated. awesome. I can come up with some variables that will help me in this problem: left, middle, and right. Classic binary search variables.

# Solution

The solution to finding the smallest value in a rotated array is to use a modified binary search. But what do I mean by modified? Well, think about a rotated array as having an inflection point. Since I know this array will always have at least one rotation, for example: [4, 5, 6, 7, 2, 3], I can think of the point where 7 -> 2 as the "inflection point". I am going to look for this inflection point as I perform binary search on the array. Whenever mid + 1 < mid, i return mid + 1, since I know I've hit my inflectino point (I'm at 7 and my mid + 1 value is 2, 2 < 7, return 2). Whenever mid - 1 > mid, return mid. (think this: if i'm at 2 and 7 > 2, return 2). Otherwise, if middle > right, I know the subsection of array i'm searching is still rotated, therefore my inflection point is to the right, middle = left + 1, if middle < right, I know my array is sorted to the right, and my inflection point is to the left of the array, hence right = middle - 1. Boom. Modified binary search

# Intuition

I didn't have a clue how to solve this problem when first looking at it, I mean, I do code in python after all, and in python I can do something like "find min in list" and python will do it. But. This question is asking for an O(log n) run time. "find min in list" does not have an O(log n) run time. I would say understanding how to modify a binary search is the key challenge for this problem, I mean sure, I know how to do a basic binary search, but understanding that I can modify it was new ground for me, and I'm sure it is for you to. As long as I can modify my search critera to perform a search on sorted subarrays of the list, I know my binary search will work. I can identify the subarrays by paying attention to an "inflection point", i.e the point where the largest number then turns to the smallest number, which is the smallest value in the array (the point of "rotation").

# Algorithm ideas

Whenever I use binary search, I can also use a modified version. The modifying part is the hard bit. How can I take advantage of binary search's runtime on a partially sorted array? I can identify that my answer will always be next to a value larger than it. If the array is rotated at least once, a big value will be behind the smallest value always. So that means I have an "in". If the value directly before middle is larger than middle, bingo, I found the smallest value. Return that bad boy. Otherwise keep searching (with a twist, the left side should be greater than the right side because of the roation). My first false start with this problem was thinking I could do this with python's super easy "find smallest number in list" syntax. Python is awesome. but alas this syntax does not run within the time constraints.

# Algorithm

left, right = 0, len(nums) - 1

while left >= right # remember this is a rotated array, so the value on the left will be bigger than the right to start
    middle = (left + right)// 2

    if nums[middle - 1] > nums[middle]:
        return middle
    elif nums[middle + 1] < nums[middle]:
        return middle + 1
    elif nums[middle] > nums[right]:
        left = middle + 1
    else:
        right = middle - 1

# Algorithm Notes

Example input: [4, 5, 6, 7, 2, 3], when middle is 6, we check around it to see if the value before is larger indicating an inflection point and giving us the answer, since the middle value 6 is larger than the right side (3), we know the inflection point is yet to come on the right side, thus I increase the left bound and search the right side, the middle value is 2 now, and the value before 2 is 7 meaning I've found the answer. Badda boom badda bing.
"""

# Code

def minimum_in_rotated_sorted_array(nums):
    left, right = 0, len(nums) - 1

    while left <= right:
        middle = (left + right) // 2

        if nums[middle - 1] > nums[middle]:
            return middle
        if nums[middle + 1] < nums[middle]:
            return middle + 1
        if nums[middle] > nums[right]:
            left = middle + 1
        else:
            right = middle - 1

nums = [4, 5, 6, 7, 2, 3]
print(minimum_in_rotated_sorted_array(nums))