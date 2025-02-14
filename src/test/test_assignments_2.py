import unittest
import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from assignment_2 import (  
  Nevilles_Method,
  Newton_Forward,
  Divided_Difference,
  Cubic_Spline
)

class TestAssignment2(unittest.TestCase):

  def test_W_Nevilles_Method(self):
    x = [3.6, 3.8, 3.9]
    y = [1.675, 1.436, 1.318]
    w = 3.7
    print(Nevilles_Method(x, y, w))
    print()

  def test_X_Newton_Forward(self):
    xi = [7.2, 7.4, 7.5, 7.6]
    fxi = [23.5492, 25.3913, 26.8224, 27.4589]
    w = 7.3
    arr1 = Newton_Forward(xi, fxi, w)
    print(arr1[0])
    print()
    print(arr1[1])
    print(arr1[2])
    print(arr1[3])
    print()

  def test_Y_Divided_Difference(self):
    x_values = [3.6, 3.6, 3.8, 3.8, 3.9, 3.9]
    f_values = [1.675, 1.675, 1.436, 1.436, 1.318, 1.318]
    f_derivatives = [-1.195, -1.195, -1.188, -1.188, -1.182, -1.182]
    arr = Divided_Difference(x_values, f_values, f_derivatives)
    
    array_str = np.array2string(arr, separator=', ')
    
    formatted_output = '\n'.join(line[1:-1] for line in array_str.splitlines()[0:])
    
    print(formatted_output)
 

    
  def test_Z_Cubic_Spline(self):
    x = [2, 5, 8, 10]
    y = [3, 5, 7, 9]
    arr2 = Cubic_Spline(x, y)
    print()
    
    col_width = max(len(str(num)) for num in arr2[0].flatten())
    
    for row in arr2[0]:
        print(f"[{', '.join(f'{num:{col_width}}' for num in row)}]")

    print(arr2[1])

    formatted_arr = [f"{num:.8g}" for num in arr2[2]]

    print(f"[{' '.join(formatted_arr)}]")
    
class NoDotsTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        pass 

class NoDotsTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return NoDotsTestResult(self.stream, self.descriptions, self.verbosity)

if __name__ == "__main__":
    unittest.main(testRunner=NoDotsTestRunner(), verbosity=0)
