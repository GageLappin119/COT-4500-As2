# COT-4500-Pro1

Contains implementations of algorithms from Chapter 2

## Directory Structure
- **src/main/**: Contains the main implementation code.
- **src/test/**: Contains test cases for the algorithms.

## How to Use
### Install Dependencies
1. Ensure you have Python installed (3.6 or higher).
2. Install required dependencies (from within the src folder):
   pip install -r requirements.txt
3. Change the values of the required variables in each function (within test_assignments_1.py) to ensure desired output.
      The variables that need to be given for the function to work as intended are the 
      parameters for each function provided below.
4. By default, each function will be turned on, change the boolean value (located at the top of each function in the test file) to true to see the output for the desired algorithm
5. In order to run program, go inside test folder and run python3 test_assignments_1.py, default values have been provided.

1.1 Approximation Algorithm

      Purpose: Approximates a value to a given exponent using an iterative approach.
      
      Parameters:
      
         value_to_approximate (float): The value to approximate.
         
         exponent (int): The exponent for the approximation.
         
         tol (float): The tolerance for stopping the iterations.
      
      Returns: The number of iterations needed to reach the desired tolerance.

1.2 Bisection Method

      Purpose: Finds the root of a function within a specified interval using the bisection method.
      
      Parameters:
      
         error (float): The tolerance for the root.
         
         a (float): The starting point of the interval.
         
         b (float): The endpoint of the interval.
         
         f (sympy expression): The function for which the root is to be found.
      
      Returns: A tuple containing the root and the number of iterations.

1.3 Fixed-Point Iteration

      Purpose: Approximates a root of a function by rewriting it as a fixed-point equation.
      
      Parameters:
      
         error (float): The tolerance for convergence.
         
         f (sympy expression): The fixed-point function .

         f_0 (sympy expression): The function before fixed point transformation
      
      Returns: The number of iterations required to converge.

1.4 Newton-Raphson Method

      Purpose: Approximates a root of a function using its derivative.
      
      Parameters:
      
         f (sympy expression): The function.
         
         f_prime (sympy expression): The derivative of the function.
         
         initial_guess (float): The initial guess for the root.
         
         tolerance (float): The stopping tolerance.
      
      max_iterations (int, optional): The maximum number of iterations (default: 100).
      
      Returns: The number of iterations required to converge.

NOTE:
   Precision: The methods use a fixed tolerance to determine convergence.

   Divergence: Fixed-point iteration and Newton-Raphson may fail for certain functions or initial guesses.

   Error Handling: Ensure that inputs (e.g., interval for bisection) meet the method's requirements to avoid runtime errors.
