# Problem

"""
Ok I have no idea what a key-value data structure is. Actually wait. I do. Key-value is literally a dictionary/hash map.

Ok so in this dictionary I want to store multiple values for the same key at different time stamps and retrieve the key's value at a certain time stamp.

Let me break that down more because that's confusing: inside one key, there's multiple timestamps, and each timestamp has a value. Then I want a function that is called with a key and timestamp, and using that key and timestamp I want the timestamp's value. 

Three functions: initialize data structure, set values in data structure, retrieve values from data structure. Much easier to understand. 

I could use the following variables: time_map which is a dictionary with a dictionary inside it, key which is a key in the time-map dictionary, timestamp which is a dictionary key in the time-map dictionary mapped to key as a value. and then timestamp which is the nested value of the nested timestamp dictionary.

Much easier to understand now.
"""
# Solution

"""
Initialize the data strcuture with self.time_map = defaultdict(dict) this code will initialize each new value of the dictionary with a dictionary, which is exactly what we want for each new key. Remember, each key is going to have a dictionary of timestamps with their own values.

Set values in the structure using self.time_map[key][timestamp] = value this code will initialize the values for key and timestamp since we are using a defaultdict and then set the respective value equal to the timestamp's value. 

Retrieve values that are less than or equal to the timestamp/key being called with. I can call on my data structure with key and timestamp. Then I can compare each value to the value I want in order of largest to smallest. If the value is <= to the expected value I return that value.

for i in range()
"""

# Intuition

Summarize the key challenges posed by the problem, and the main approach I will use to solve it. When I'm writing the more detailed sections below, make sure they follow the general plan explained in this section. If they don’t, either adjust the details or adjust the plan. I can also use the intuition section to remind myself how to solve the problem if I forget what approach I used in a future practice session. In this way, it’s a bit like the hints that LeetCode provides for some problems. But while LeetCode authors write hints cryptically, so they don’t give away too much, I should write my intuition section clearly.

# Algorithm ideas

In LeetCode discussion posts, authors often jump to the solution without explaining how they figured it out. The algorithm ideas section is for explaining how I got from the intuition to the final product, including any false starts that can help explain why I solved the problem in the way I did.

# Algorithm

LeetCode problems focus on algorithms and data structures. The algorithm section explains the final algorithm that I used to solve the problem. Usually, I'll want to explain the algorithm using pseudocode. There is no official pseudocode syntax like there is for a programming language, so I'll use whatever form of pseudocode is most understandable to me.

# Algorithm Notes

For some problems, it may not be clear why the algorithm works, even when the explanation is well written. Example cases or test data can help clarify how the algorithm handles different input. This model solution also uses diagrams, which make most model solutions more understandable.

# Code

Finally, I have the actual code, meaning code that LeetCode would accept if I submitted it. If I used code ideas from other sources, this is a good place to link to those in case I want to look them up later. Although LeetCode doesn’t care about code comments, it’s useful to add them to my model code to show where I implement each step of the solution. If there are any remaining questions about what each code block does and why it works, this is the place to clear them up.