# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:27:24 2021

@author: arman
"""

##  We import OS library to get the directory relevant
import os
path = os.getcwd()
print(path)

##  Changing path to root level where I can find the scratch directory
os.chdir('C:\\Users\\arman\\OneDrive\\Desktop\\2020\\08_DataScienceFromScratch\\data-science-from-scratch-master')
path = os.getcwd()
print(path)
os.listdir(path)


##  This is an example of a function to which we would like to obtain the maximum or minimum.
from scratch.linear_algebra import Vector, dot

def sum_of_squares(v: Vector) -> float:
    """Computes the sum of squared elements in v"""
    return dot(v, v)


##  We are getting the derivative.  
from typing import Callable

def difference_quotient(f: Callable[[float], float],
                        x: float,
                        h: float) -> float:
    return (f(x + h) - f(x)) / h

##  This is an example of simple derivative which we can do easily by hand
def square(x: float) -> float:
    return x * x

def derivative(x: float) -> float:
    return 2 * x

##  Making the estimation for this special case.
xs = range(-10, 11)
actuals = [derivative(x) for x in xs]
estimates = [difference_quotient(square, x, h=0.001) for x in xs]

# plot to show they're basically the same
import matplotlib.pyplot as plt
plt.title("Actual Derivatives vs. Estimates")
plt.plot(xs, actuals, 'rx', label='Actual')       # red  x
plt.plot(xs, estimates, 'b+', label='Estimate')   # blue +
plt.legend(loc=9)
# plt.show()


##  We obtain the derivative with respecto to a specific variable.
def partial_difference_quotient(f: Callable[[Vector], float],
                                 v: Vector,
                                 i: int,
                                 h: float) -> float:
     """Returns the i-th partial difference quotient of f at v"""
     w = [v_j + (h if j == i else 0)    # add h to just the ith element of v
          for j, v_j in enumerate(v)]
 
     return (f(w) - f(v)) / h
 

##  This is the simplification of the derivative
def estimate_gradient(f: Callable[[Vector], float],
                      v: Vector,
                      h: float = 0.0001):
    return [partial_difference_quotient(f, v, i, h)
            for i in range(len(v))]
 
    
 
 
import random
from scratch.linear_algebra import distance, add, scalar_multiply

## Explain how is the gradient step
def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    """Moves `step_size` in the `gradient` direction from `v`"""
    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)

def sum_of_squares_gradient(v: Vector) -> Vector:
    return [2 * v_i for v_i in v]

 # pick a random starting point
v = [random.uniform(-10, 10) for i in range(3)]




for epoch in range(1000):
        grad = sum_of_squares_gradient(v)    # compute the gradient at v
        v = gradient_step(v, grad, -0.01)    # take a negative gradient step
        print(epoch, v)
        
assert distance(v, [0, 0, 0]) < 0.001    # v should be close to 0


# x ranges from -50 to 49, y is always 20 * x + 5
inputs = [(x, 20 * x + 5) for x in range(-50, 50)]


def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    slope, intercept = theta
    predicted = slope * x + intercept    # The prediction of the model.
    error = (predicted - y)              # error is (predicted - actual)
    squared_error = error ** 2           # We'll minimize squared error
    grad = [2 * error * x, 2 * error]    # using its gradient.
    return grad

# First "Using Gradient Descent to Fit Models" example
    
from scratch.linear_algebra import vector_mean

# Start with random values for slope and intercept.
theta = [random.uniform(-1, 1), random.uniform(-1, 1)]

learning_rate = 0.001

for epoch in range(5000):
    # Compute the mean of the gradients
    grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
    # Take a step in that direction
    theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)

slope, intercept = theta
assert 19.9 < slope < 20.1,   "slope should be about 20"
assert 4.9 < intercept < 5.1, "intercept should be about 5"


####

from typing import TypeVar, List, Iterator

T = TypeVar('T')  # this allows us to type "generic" functions

def minibatches(dataset: List[T],
                batch_size: int,
                shuffle: bool = True) -> Iterator[List[T]]:
    """Generates `batch_size`-sized minibatches from the dataset"""
    # Start indexes 0, batch_size, 2 * batch_size, ...
    batch_starts = [start for start in range(0, len(dataset), batch_size)]

    if shuffle: random.shuffle(batch_starts)  # shuffle the batches

    for start in batch_starts:
        end = start + batch_size
        yield dataset[start:end] 

########  Application of minibatches

# Minibatch gradient descent example
    
theta = [random.uniform(-1, 1), random.uniform(-1, 1)]

for epoch in range(1000):
    for batch in minibatches(inputs, batch_size=20):
        grad = vector_mean([linear_gradient(x, y, theta) for x, y in batch])
        theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)

slope, intercept = theta
assert 19.9 < slope < 20.1,   "slope should be about 20"
assert 4.9 < intercept < 5.1, "intercept should be about 5"


# Stochastic gradient descent example
  
theta = [random.uniform(-1, 1), random.uniform(-1, 1)]

for epoch in range(100):
    for x, y in inputs:
        grad = linear_gradient(x, y, theta)
        theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)

slope, intercept = theta
assert 19.9 < slope < 20.1,   "slope should be about 20"
assert 4.9 < intercept < 5.1, "intercept should be about 5"


###  Please review this video to better understand the gradient 
### descent with Gradient descent, how neural networks learn | Deep learning, chapter 2
### 