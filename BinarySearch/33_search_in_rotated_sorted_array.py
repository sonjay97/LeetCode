"""
# Problem

I need to search for target inside a rotated sorted array.
The algorithm I use has to search for target in O(log n) time.

# Solution

I can use a modified binary search to look for target in O(log n) runtime complexity, even if the array is rotated.

I can use binary search on each sorted subarray, therefore ensuring I have an efficient runtime.

# Intuition

The key challenge with this problem is modifying binary search to work with sub arrays that contain the target. The main approach first requires understanding that I'll have to verify which subarray I'm looking at. Then, it's required to do classic binary search within the subarray.

# Algorithm ideas

I need to modify the if conditions in a binary search to account that I might be in the right or wrong subarray.

This means I need to check if the middle value is greater than the left value. Then I need to check if the target is greater than the middle value or if the target is less than the left value. 


In LeetCode discussion posts, authors often jump to the solution without explaining how they figured it out. The algorithm ideas section is for explaining how I got from the intuition to the final product, including any false starts that can help explain why I solved the problem in the way I did.

# Algorithm

LeetCode problems focus on algorithms and data structures. The algorithm section explains the final algorithm that I used to solve the problem. Usually, I'll want to explain the algorithm using pseudocode. There is no official pseudocode syntax like there is for a programming language, so I'll use whatever form of pseudocode is most understandable to me.

# Algorithm Notes

For some problems, it may not be clear why the algorithm works, even when the explanation is well written. Example cases or test data can help clarify how the algorithm handles different input. This model solution also uses diagrams, which make most model solutions more understandable.

# Code

Finally, I have the actual code, meaning code that LeetCode would accept if I submitted it. If I used code ideas from other sources, this is a good place to link to those in case I want to look them up later. Although LeetCode doesn’t care about code comments, it’s useful to add them to my model code to show where I implement each step of the solution. If there are any remaining questions about what each code block does and why it works, this is the place to clear them up.
"""