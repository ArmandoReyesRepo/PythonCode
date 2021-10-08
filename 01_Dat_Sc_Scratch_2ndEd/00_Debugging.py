# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 23:05:19 2020

@author: arman
"""

def hello_world (firstname, lastname):
    var = 12
    print ("My name is {} {}".format(firstname,lastname))
    var = 24
    sum1 = var + 250
    print (sum1)
    

hello_world("Krish","Naik")



############   Use of assert


#   https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python


# Assertions can include an optional message, and you can disable them when running the interpreter.

# To print a message if the assertion fails:

assert False, "Oh no! This assertion failed!"