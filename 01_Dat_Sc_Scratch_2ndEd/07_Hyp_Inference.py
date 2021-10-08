# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 01:53:57 2021

@author: arman
"""

from typing import Tuple
import math

def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """Returns mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

normal_approximation_to_binomial(10,0.5)


##  We import OS library to get the directory relevant
import os
path = os.getcwd()
print(path)

##  Changing path to root level where I can find the scratch directory
os.chdir('C:\\Users\\arman\\OneDrive\\Desktop\\2020\\08_DataScienceFromScratch\\data-science-from-scratch-master')
path = os.getcwd()
print(path)


## Finding probabilities above and below some number

from scratch.probability import normal_cdf

# The normal cdf _is_ the probability the variable is below a threshold
normal_probability_below = normal_cdf



# It's above the threshold if it's not below the threshold
def normal_probability_above(lo: float,
                             mu: float = 0,
                             sigma: float = 1) -> float:
    """The probability that a N(mu, sigma) is greater than lo."""
    return 1 - normal_cdf(lo, mu, sigma)


normal_probability_above(-.5)

# It's between if it's less than hi, but not less than lo.
def normal_probability_between(lo: float,
                               hi: float,
                               mu: float = 0,
                               sigma: float = 1) -> float:
    """The probability that a N(mu, sigma) is between lo and hi."""
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

normal_probability_between(-.5,.5)

# It's outside if it's not between
def normal_probability_outside(lo: float,
                               hi: float,
                               mu: float = 0,
                               sigma: float = 1) -> float:
    """The probability that a N(mu, sigma) is not between lo and hi."""
    return 1 - normal_probability_between(lo, hi, mu, sigma)

normal_probability_outside(-.5,.5)


###  Finding the number giving probabilities

from scratch.probability import inverse_normal_cdf

def normal_upper_bound(probability: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """Returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)


normal_upper_bound(0.3)

def normal_lower_bound(probability: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """Returns the z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)

normal_lower_bound(0.3)

def normal_two_sided_bounds(probability: float,
                            mu: float = 0,
                            sigma: float = 1) -> Tuple[float, float]:
    """
    Returns the symmetric (about the mean) bounds
    that contain the specified probability
    """
    tail_probability = (1 - probability) / 2

    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

normal_two_sided_bounds(0.3)

# In particular, let’s say that we choose to flip the coin n = 1,000 times. 
# If our hypothesis of fairness is true, X should be distributed approximately 
# normally with mean 500 and standard deviation 15.8:
    
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)


assert mu_0 == 500
assert 15.8 < sigma_0 < 15.9   


# (469, 531)
lower_bound, upper_bound = normal_two_sided_bounds(0.95, mu_0, sigma_0)

lower_bound
upper_bound

assert 468.5 < lower_bound < 469.5
assert 530.5 < upper_bound < 531.5

# 95% bounds based on assumption p is 0.5
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)


# actual mu and sigma based on p = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# a type 2 error means we fail to reject the null hypothesis
# which will happen when X is still in our original interval
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability      # 0.887


assert 0.886 < power < 0.888

hi = normal_upper_bound(0.95, mu_0, sigma_0)
# is 526 (< 531, since we need more probability in the upper tail)

type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability      # 0.936


assert 526 < hi < 526.1
assert 0.9363 < power < 0.9364

##  P - Values

def two_sided_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:
    """
    How likely are we to see a value at least as extreme as x (in either
    direction) if our values are from a N(mu, sigma)?
    """
    if x >= mu:
        # x is greater than the mean, so the tail is everything greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # x is less than the mean, so the tail is everything less than x
        return 2 * normal_probability_below(x, mu, sigma)

two_sided_p_value(529.5, mu_0, sigma_0)   # 0.062


import random

extreme_value_count = 0
for _ in range(1000):
    num_heads = sum(1 if random.random() < 0.5 else 0    # Count # of heads
                    for _ in range(1000))                # in 1000 flips,
    if num_heads >= 530 or num_heads <= 470:             # and count how often
        extreme_value_count += 1    
        
# p-value was 0.062 => ~62 extreme values out of 1000
assert 59 < extreme_value_count < 65, f"{extreme_value_count}"

two_sided_p_value(531.5, mu_0, sigma_0)   # 0.0463

tspv = two_sided_p_value(531.5, mu_0, sigma_0)
assert 0.0463 < tspv < 0.0464



upper_p_value = normal_probability_above
lower_p_value = normal_probability_below

upper_p_value
lower_p_value

upper_p_value(524.5, mu_0, sigma_0) # 0.061
##  We reject the null hypotehis

upper_p_value(526.5, mu_0, sigma_0) # 0.047
##  We do not reject the null hypothesis


##  Condifendence Interval using a Bernoulli Experiment
# 525 heads of 1000 trials.

p_hat = 525 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)   # 0.0158
normal_two_sided_bounds(0.95, mu, sigma)        # [0.4940, 0.5560]


p_hat = 540 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000) # 0.0158
normal_two_sided_bounds(0.95, mu, sigma) # [0.5091, 0.5709]


## p-Hacking

from typing import List

def run_experiment() -> List[bool]:
    """Flips a fair coin 1000 times, True = heads, False = tails"""
    return [random.random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment: List[bool]) -> bool:
    """Using the 5% significance levels"""
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531

random.seed(0)
experiments = [run_experiment() for _ in range(1000)]
num_rejections = len([experiment
                      for experiment in experiments
                      if reject_fairness(experiment)])


experiment=run_experiment()
reject_fairness(experiment)

assert num_rejections == 46


#######  example of exporting a list to excel file #####
import xlwt
from tempfile import TemporaryFile
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

supersecretdata = [34,123,4,1234,12,34,12,41,234,123,4,123,1,45123,5,43,61,3,56]

for i,e in enumerate(supersecretdata):
    sheet1.write(i,1,e)

name = "random.xls"
book.save(name)
book.save(TemporaryFile())

#######  example of exporting a list to excel file #####

#### using the same for my bool list ####

import xlwt
from tempfile import TemporaryFile
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

##experimento = experiment

for i,e in enumerate(experimento):
    ##print(e)
    sheet1.write(i,1,e)

name = "experimento.xls"
book.save(name)
book.save(TemporaryFile())


#### using the same for my bool list ####



##  Running A/B Test

def estimated_parameters(N: int, n: int) -> Tuple[float, float]:
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma

def a_b_test_statistic(N_A: int, n_A: int, N_B: int, n_B: int) -> float:
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

z = a_b_test_statistic(1000, 200, 1000, 180)    # -1.14


assert -1.15 < z < -1.13

two_sided_p_value(z)                            # 0.254


assert 0.253 < two_sided_p_value(z) < 0.255

z = a_b_test_statistic(1000, 200, 1000, 150)    # -2.94
two_sided_p_value(z)                            # 0.003



## Bayesian Inference

def B(alpha: float, beta: float) -> float:
    """A normalizing constant so that the total probability is 1"""
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

def beta_pdf(x: float, alpha: float, beta: float) -> float:
    if x <= 0 or x >= 1:          # no weight outside of [0, 1]
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)
