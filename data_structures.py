"""
Types of data structures: 

Ordered collections: 
    - Mutable - Lists
    - Not mutable - Tuples
    - Mutable, allow generation - Ranges

Unordered collections:
    - Sets
    - Dictionaries
"""

# Lists
list1 = [1, 3, 4, 5, 6]
list1.append(7)
list1.remove(1)
print(list1)
list1[0] = 5
print(list1[0])

# Tuples
x = (3, 4)
print(x[1])
# tuples do not allow us to assign item assignment or edit.

def foo(a, b):
    return a+b, a-b

foo(1, 2)

# Ranges
x = list(range(0, 10))
print(x)
for i in range(10):
    print(i)

# Sets
# store unique values in no particular order
y = {1, 1, 1, 1, 4, 4, 6, 7, 8, 9, 10}

# Dictionary
# a set with more powers. Unique key an value.
z = {"num_cakes":10, "num_cookies":5}

def value_counts(nums):
    """
    :param nums: Input list of numbers
    :return: Dict of each unique number and its frequency
    """
    counts = {}
    if nums is not None:
        for num in nums:
            counts[num] = 1 if num not in counts else counts[num] + 1
    return counts

print(value_counts([6, 7, 0, 8, 0, 8, 0, 1, 2, 3, 2]))