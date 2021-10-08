#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 01:07:26 2020

@author: armandoreyesmartinez
"""


##  Getting elements from Lists

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zero = x[0]          # equals 0, lists are 0-indexed
one = x[1]           # equals 1
nine = x[-1]         # equals 9, 'Pythonic' for last element
eight = x[-2]        # equals 8, 'Pythonic' for next-to-last element
x[0] = -1            # now x is [-1, 1, 2, 3, ..., 9]


assert x == [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

first_three = x[:3]                 # [-1, 1, 2]
three_to_end = x[3:]                # [3, 4, ..., 9]
one_to_four = x[1:5]                # [1, 2, 3, 4]
last_three = x[-3:]                 # [7, 8, 9]
without_first_and_last = x[1:-1]    # [1, 2, ..., 8]
copy_of_x = x[:]                    # [-1, 1, 2, ..., 9]

every_third = x[::3]                 # [-1, 3, 6, 9]
five_to_three = x[5:2:-1]            # [5, 4, 3]


assert every_third == [-1, 3, 6, 9]
assert five_to_three == [5, 4, 3]


##  Testing if elements are in list

1 in [1, 2, 3]    # True
0 in [1, 2, 3]    # False

##  Extending lists

x = [1, 2, 3]
x.extend([4, 5, 6])     # x is now [1, 2, 3, 4, 5, 6]
assert x == [1, 2, 3, 4, 5, 6]

##  Testing another example of lists

x = [1, 2, 3]
y = x + [4, 5, 6]       # y is [1, 2, 3, 4, 5, 6]; x is unchanged


assert x == [1, 2, 3]
assert y == [1, 2, 3, 4, 5, 6]


##  Another example of a list

x = [1, 2, 3]
x.append(0)      # x is now [1, 2, 3, 0]
y = x[-1]        # equals 0
z = len(x)       # equals 4


assert x == [1, 2, 3, 0]  ##  Nothing happens
assert y == 0
assert z == 4

x, y = [1, 2]    # now x is 1, y is 2


assert x == 1
assert y == 2

_, y = [1, 2]    # now y == 2, didn't care about the first element


##  Trying list and tuples

my_list = [1, 2]
my_tuple = (1, 2)  ##  This can not be modified
other_tuple = 3, 4
my_list[1] = 3      # my_list is now [1, 3]




try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")


##  Testing functions and assigning results to tuples

def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(2, 3)     # sp is (5, 6)
s, p = sum_and_product(5, 10)  # s is 15, p is 50

x, y = 1, 2     # now x is 1, y is 2
x, y = y, x     # Pythonic way to swap variables; now x is 2, y is 1


assert x == 2
assert y == 1


##  Dictioanries


empty_dict = {}                     # Pythonic
empty_dict2 = dict()                # less Pythonic
grades = {"Joel": 80, "Tim": 95}    # dictionary literal

joels_grade = grades["Joel"]        # equals 80


assert joels_grade == 80  ## Nothing will happen here

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

joel_has_grade = "Joel" in grades     # True
kate_has_grade = "Kate" in grades     # False


assert joel_has_grade
assert not kate_has_grade  ##  This is an example of assert being negative

joels_grade = grades.get("Joel", 0)   # equals 80
kates_grade = grades.get("Kate", 0)   # equals 0
no_ones_grade = grades.get("No One")  # default default is None


assert joels_grade == 80
assert kates_grade == 0
assert no_ones_grade is None

grades["Tim"] = 99                    # replaces the old value
grades["Kate"] = 100                  # adds a third entry
num_students = len(grades)            # equals 3


assert num_students == 3

##  An application of dictionaries

tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys   = tweet.keys()     # iterable for the keys
tweet_values = tweet.values()   # iterable for the values
tweet_items  = tweet.items()    # iterable for the (key, value) tuples

"user" in tweet_keys            # True, but not Pythonic
"user" in tweet                 # Pythonic way of checking for keys
"joelgrus" in tweet_values      # True (slow but the only way to check)


assert "user" in tweet_keys
assert "user" in tweet
assert "joelgrus" in tweet_values


##  An application of dictionaries for counting words in a list of words

document = ["data", "science", "from", "scratch", "data"]

word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
        
## Second approach

word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

##  Third approach

word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1
    
    
## Using default dictionaries  ( this is easier )

from collections import defaultdict

word_counts = defaultdict(int)          # int() produces 0
for word in document:
    word_counts[word] += 1
    
##  Using default dict with list, dict and functions

dd_list = defaultdict(list)             # list() produces an empty list
dd_list[2].append(1)                    # now dd_list contains {2: [1]}

dd_dict = defaultdict(dict)             # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle"     # {"Joel" : {"City": Seattle"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                       # now dd_pair contains {2: [0, 1]}



##  Counters


from collections import Counter
c = Counter([0, 1, 2, 0])          # c is (basically) {0: 2, 1: 1, 2: 1}


# recall, document is a list of words

document = ["data", "science", "from", "scratch", "data"]

word_counts = Counter(document)

# print the 10 most common words and their counts
for word, count in word_counts.most_common(10):
    print(word, count)
    
    
##  Sets   //  This is very good for use of in,  this is quite fast

primes_below_10 = {2, 3, 5, 7}

s = set()
s.add(1)       # s is now {1}
s.add(2)       # s is now {1, 2}
s.add(2)       # s is still {1, 2}
x = len(s)     # equals 2
y = 2 in s     # equals True
z = 3 in s     # equals False


hundreds_of_other_words = []  # required for the below code to run

stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]

"zip" in stopwords_list     # False, but have to check every element

stopwords_set = set(stopwords_list)
"zip" in stopwords_set      # very fast to check


item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)                # 6
item_set = set(item_list)                 # {1, 2, 3}
num_distinct_items = len(item_set)        # 3
distinct_item_list = list(item_set)       # [1, 2, 3]


assert num_items == 6
assert item_set == {1, 2, 3}
assert num_distinct_items == 3
assert distinct_item_list == [1, 2, 3]

##  me quedé en la línea 350,  mañana a trabajar fuerte en el currículum. Vamos a conseguir el trabajo bueno,
##  vamos a producir mis videos y vamos a comenzar el podcast


##  Control Flow


## IF

if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"
    
    
##  Compacted version of if then else

x=3

parity = "even" if x % 2 == 0 else "odd"



## Python while loop, using a variable inside

x = 0
while x < 10:
    print(f"{x} is less than 10")
    x += 1
    
# range(10) is the numbers 0, 1, ..., 9
for x in range(10):
    print(f"{x} is less than 10")


## printing with conditions
for x in range(10):
    if x == 3:
        continue  # go immediately to the next iteration
    if x == 5:
        break     # quit the loop entirely
    print(x)
    

##  Truthiness

one_is_less_than_two = 1 < 2          # equals True
true_equals_false = True == False     # equals False


assert one_is_less_than_two
assert not true_equals_false

x = None
assert x == None, "this is the not the Pythonic way to check for None"
assert x is None, "this is the Pythonic way to check for None"


# The following is false

# False
# None
# [] (an empty list)
# {} (an empty dict)
# ""
# set()
# 0
# 0.0


def some_function_that_returns_a_string():
    return ""

s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""

first_char = s and s[0]

safe_x = x or 0

safe_x = x if x is not None else 0


##  When all are truth,  is true,  when at least one is true (any)  it is true

all([True, 1, {3}])   # True, all are truthy
all([True, 1, {}])    # False, {} is falsy
any([True, 1, {}])    # True, True is truthy
all([])               # True, no falsy elements in the list
any([])               # False, no truthy elements in the list


##  Sorting elements

x = [4, 1, 2, 3]
y = sorted(x)     # y is [1, 2, 3, 4], x is unchanged
x.sort()          # now x is [1, 2, 3, 4]

# sort the list by absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)  # is [-4, 3, -2, 1]


# sort the words and counts from highest count to lowest  / a lambda function is inserted
wc = sorted(word_counts.items(),
            key=lambda word_and_count: word_and_count[1],
            reverse=True)


## List Comprehensions

even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
squares      = [x * x for x in range(5)]            # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers]        # [0, 4, 16]

assert even_numbers == [0, 2, 4]
assert squares == [0, 1, 4, 9, 16]
assert even_squares == [0, 4, 16]


## List in dictionaries

square_dict = {x: x * x for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
square_set  = {x * x for x in [1, -1]}      # {1}


assert square_dict == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
assert square_set == {1}

## If you don´t need the value from the list

zeros = [0 for _ in even_numbers]      # has the same length as even_numbers

assert zeros == [0, 0, 0]


## List comprehension with double for
pairs = [(x, y)
         for x in range(10)
         for y in range(10)]   # 100 pairs (0,0) (0,1) ... (9,8), (9,9)


assert len(pairs) == 100


## List comprehension with x<y using double for

increasing_pairs = [(x, y)                       # only pairs with x < y,
                    for x in range(10)           # range(lo, hi) equals
                    for y in range(x + 1, 10)]   # [lo, lo + 1, ..., hi - 1]

assert len(increasing_pairs) == 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1
assert all(x < y for x, y in increasing_pairs)


##  Automated Testing and Assert

assert 1 + 1 == 2
assert 1 + 1 == 2, "1 + 1 should equal 2 but didn't"

def smallest_item(xs):
    return min(xs)

assert smallest_item([10, 20, 5, 40]) == 5
assert smallest_item([1, 0, -1, 2]) == -1


##  Asserting input for functions
def smallest_item(xs):
    assert xs, "empty list has no smallest item"
    return min(xs)

smallest_item([])
smallest_item([5,4,3,2,1])


## Object Oriented Programming

class CountingClicker:
    """A class can/should have a docstring, just like a function"""

    def __init__(self, count = 0):
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    def click(self, num_times = 1):
        """Click the clicker some number of times."""
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0
        
        
clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"


# A subclass inherits all the behavior of its parent class.
class NoResetClicker(CountingClicker):
    # This class has all the same methods as CountingClicker

    # Except that it has a reset method that does nothing.
    def reset(self):
        pass

clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1, "reset shouldn't do anything"


##  Iterable and generators



##  Generator using Yield within functions  // They are evaluated on demand

def generate_range(n):
    i = 0
    while i < n:
        yield i   # every call to yield produces a value of the generator
        i += 1
        
        
for i in generate_range(10):
    print(f"i: {i}")


def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1
        
evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)
    
# None of these computations *does* anything until we iterate
data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)
# and so on

assert next(even_squares_ending_in_six) == 16
assert next(even_squares_ending_in_six) == 36
assert next(even_squares_ending_in_six) == 196


##  Enumerate  ( this is in order to get the index and value from data )


names = ["Alice", "Bob", "Charlie", "Debbie"]

# not Pythonic
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

# also not Pythonic
i = 0
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1

# Pythonic
for i, name in enumerate(names):
    print(f"name {i} is {name}")
    
    
## Randomness

import random
random.seed(10)  # this ensures we get the same results every time

four_uniform_randoms = [random.random() for _ in range(4)]  ## i don´t care about the variable in range

random.seed(10)         # set the seed to 10
print(random.random())  # 0.57140259469
random.seed(10)         # reset the seed to 10
print(random.random())  # 0.57140259469 again

random.randrange(10)    # choose randomly from range(10) = [0, 1, ..., 9]
random.randrange(3, 6)  # choose randomly from range(3, 6) = [3, 4, 5]

up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(up_to_ten)
# [7, 2, 6, 8, 9, 4, 10, 1, 3, 5]   (your results will probably be different)

my_best_friend = random.choice(["Alice", "Bob", "Charlie"])     # "Bob" for me
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)  # [16, 36, 10, 6, 25, 9]


four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)  # [9, 4, 4, 2]


##  Regular expressions

import re

re_examples = [                        # all of these are true, because
    not re.match("a", "cat"),              #  'cat' doesn't start with 'a'
    re.search("a", "cat"),                 #  'cat' has an 'a' in it
    not re.search("c", "dog"),             #  'dog' doesn't have a 'c' in it
    3 == len(re.split("[ab]", "carbs")),   #  split on a or b to ['c','r','s']
    "R-D-" == re.sub("[0-9]", "-", "R2D2") #  replace digits with dashes
    ]

assert all(re_examples), "all the regex examples should be True"


## Zip and Argument Unpacking


##  First example
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

# zip is lazy, so you have to do something like the following
[pair for pair in zip(list1, list2)]    # is [('a', 1), ('b', 2), ('c', 3)]


assert [pair for pair in zip(list1, list2)] == [('a', 1), ('b', 2), ('c', 3)]

## unpair a list from the zipping (*) argument unpacking

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

## the last unpacking is the same like this

letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))



## Unpacking within a function
def add(a, b): return a + b
add(1, 2)      # returns 3
try:
    add([1, 2])
except TypeError:
    print("add expects two inputs")
add(*[1, 2])   # returns 3

## args and kwargs

def doubler(f):
    # Here we define a new function that keeps a reference to f
    def g(x):
        return 2 * f(x)
    # And return that new function.
    return g

def f1(x):
    return x + 1

g = doubler(f1)
assert g(3) == 8,  "(3 + 1) * 2 should equal 8"
assert g(-1) == 0, "(-1 + 1) * 2 should equal 0"


##  here the function doesn´t work because g function only takes one argument
def f2(x, y):
    return x + y

g = doubler(f2)
try:
    g(1, 2)
except TypeError:
    print("as defined, g only takes one argument")
    
 ##  We need to define a function with arbitrary arguments

def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)

magic(1, 2, key="word", key2="word2")   

# prints
#  unnamed args: (1, 2)
#  keyword args: {'key': 'word', 'key2': 'word2'}

def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {"z": 3}
assert other_way_magic(*x_y_list, **z_dict) == 6, "1 + 2 + 3 should be 6"
other_way_magic(*x_y_list, **z_dict)


##  Fixing the function using args(*) and kwargs (**)
def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
assert g(1, 2) == 6, "doubler should work now"




##  Type annotations


## The type of inputs and function is not defined
def add(a, b):
    return a + b

assert add(10, 5) == 15,                  "+ is valid for numbers"
assert add([1, 2], [3]) == [1, 2, 3],     "+ is valid for lists"
assert add("hi ", "there") == "hi there", "+ is valid for strings"

try:
    add(10, "five")
except TypeError:
    print("cannot add an int to a string")
    
    
##  Defining the type of input and the type of the function

def add(a: int, b: int) -> int:
    return a + b

add(10, 5)           # you'd like this to be OK
add("hi ", "there")  # you'd like this to be not OK



## this is not very correct
def total(xs: list) -> float:
    return sum(xs)


total([1,2,3])

## this is better

from typing import List  # note capital L

def total(xs: List[float]) -> float:
    return sum(xs)

total([4.5,4.5,4.5])


## Defining several types

# This is how to type-annotate variables when you define them.
# But this is unnecessary; it's "obvious" x is an int.
x: int = 5

values = []         # what's my type?
best_so_far = None  # what's my type?

from typing import Optional

values: List[int] = []
best_so_far: Optional[float] = None  # allowed to be either a float or None

## More type definitions

lazy = True

# the type annotations in this snippet are all unnecessary
from typing import Dict, Iterable, Tuple

# keys are strings, values are ints
counts: Dict[str, int] = {'data': 1, 'science': 2}

# lists and generators are both iterable
if lazy:
    evens: Iterable[int] = (x for x in range(10) if x % 2 == 0)
else:
    evens = [0, 2, 4, 6, 8]

# tuples specify a type for each element
triple: Tuple[int, float, int] = (10, 2.3, 5)


##  Another example

from typing import Callable

# The type hint says that repeater is a function that takes
# two arguments, a string and an int, and returns a string.
def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)

assert twice(comma_repeater, "type hints") == "type hints, type hints"

Number = int
Numbers = List[Number]

def total(xs: Numbers) -> Number:
    return sum(xs)


total([1,2,3])
