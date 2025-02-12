import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.main.assignment_2 import (  
  Nevilles_Method,
  Newton_Forward,
  Divided_Difference,
  Cubic_Spline
)

class TestAssignment2(unittest.TestCase):

  def test_Nevilles_Method(self):
    x = [3.6, 3.8, 3.9]
    y = [1.675, 1.436, 1.318]
    w = 3.7
    #print(Nevilles_Method(x, y, w))

  def test_Newton_Forward(self):
    xi = [7.2, 7.4, 7.5, 7.6]
    fxi = [23.5492, 25.3913, 26.8224, 27.4589]
    w = 7.3
    #print(Newton_Forward(xi, fxi, w))

  def test_Divided_Difference(self):
    # Given data points
    x_values = [3.6, 3.6, 3.8, 3.8, 3.9, 3.9]
    f_values = [1.675, 1.675, 1.436, 1.436, 1.318, 1.318]
    f_derivatives = [-1.195, -1.195, -1.188, -1.188, -1.182, -1.182]
    #print(Divided_Difference(x_values, f_values, f_derivatives))

  def test_Cubic_Spline(self):
    x = [2, 5, 8, 10]
    y = [3, 5, 7, 9]
    spline = Cubic_Spline(x, y)
    print(spline)
    
if __name__ == "__main__":
  unittest.main()
