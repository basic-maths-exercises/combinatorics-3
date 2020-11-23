import unittest
import numpy as np
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_factorial(self) :
        for i in range(1,10) : 
            self.assertTrue( factorial(i)==np.math.factorial(i), "Your factorial function is not working correctly" )
            
    def test_recursion(self) :
        self.assertTrue( inspect.getsource(factorial).find("for")<0, "Your factorial function contains a for loop.  You are supposed to complete this exercise using recursion.  You thus do not need a for loop." )
