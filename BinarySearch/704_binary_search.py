"""
Author: @jay.shah
Date: June 1, 2025


# Problem

Given a sorted array of integers, find the integer index of "target" using an algorithm that runs in O(log n) time complexity.
I'll intialize variables such as left, right, and mid to identify what position in the array I'm in.

# Solution

I'll identify the middle of the array using the left and right side (start and end) of the array. Then I'll see if the middle value is equal to my target. If the value at the middle index is not equal to my target then I will see if the middle value is greater than my target. If yes, then I know my target is towards the left of the middle value. I can decrease the right boundary and set it equal to the "middle value - 1" and effectively reduce the search to half the array. Otherwise if the middle value is smaller than the target, I know my target is a larger value and must be towards the right of the array. Thus I will set the left boundary to "middle + 1" and effectively reduce the array size to half. I need to remember that my while loop logic should continue looping until the left boundary is "less than or equal to" the right boundary, if the array size is 1 then the while loop logic will not execute if I only set the left boundary to be "less than" the right boundary. I always want to the while loop logic to execute even if the length of the array is 1.

# Intuition

The key challenge posed by this problem is the time constraint. The solution should run in O(log n) time. The main approach I've taken to deal with this challenge is by using a binary search. Binary search provides an O(log n) run time that fits the constraints of this problem.

# Algorithm Ideas

My first false start with this problem was my lack of understanding the time constraints. Using python, I knew it was pretty easy to say "if target in nums return True" or some variation of that. This answer would be incorrect though because the time constraints are exceeded when nums is very large. Thus, I was stumped on the problem. I had to learn binary search from scratch.

# Algorithm

left, right = beginning of array, end of array
while left is less than or equal to right
    calculate middle index = left + right // 2
    if nums[middle] == target
        return middle index
    elif nums[middle] > target:
        right = middle - 1
    else:
        left = middle + 1
    
# Algorithm Notes

It was not clear to me why this algorithm worked the first time I looked at it. The key to me understanding binary search was to pay attention to the if conditions. if the middle value is equal to my target then I have the answer, if the middle value is greater than the target, than the answer is in the left side of the array, and I search the opposite side of the array if the middle value is less than the target. You wouldn't believe how much those three conditions tripped me up when trying to implemente binary search. As I've kept practicing though, I've come to understand the intuition behind the problem.
"""


nums = [1, 2, 3, 4, 5, 6, 7, 8, 12, 122, 1222, 122222, 15555555, 5433221123455]

def binary_search(nums):

    target = 5433221123455
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

print(binary_search(nums))