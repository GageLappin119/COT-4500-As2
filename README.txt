# COT-4500-As2

Contains implementations of numerical algorithms from Chapter 3.
Also contains the assignment pdf with solutions written out by hand alongside program output

## Directory Structure

- **src/main/**: Contains the main implementation code.
- **src/test/**: Contains test cases for the algorithms.

## How to Use

### Install Dependencies

1. Ensure you have Python installed (3.6 or higher).
2. Install required dependencies by running the following command inside the root folder:
      pip3 install -r requirements.txt
 
   *(Use **`pip`** instead of **`pip3`** if the command does not work.)*

### Running Tests

To execute the test cases, navigate to the `test` folder and run:

   python3 test_assignments_2.py


(Default values are provided in the test cases.)

## Implemented Algorithms

### 1. Neville's Method

   - Approximates the value of a function at a given point using Neville’s interpolation.
   - **Test Case:** Approximates `f(3.7)` for given data points `x = [3.6, 3.8, 3.9]` and `y = [1.675, 1.436, 1.318]`.

### 2. Newton Forward Interpolation

   - Computes a polynomial approximation using Newton’s forward interpolation formula.
   - **Test Case:** Approximates `f(7.3)` using data points `xi = [7.2, 7.4, 7.5, 7.6]` with function values `fxi = [23.5492, 25.3913, 26.8224, 27.4589]`.
   - Outputs:
     - Approximate function value at `w = 7.3`
     - Coefficients of the interpolation polynomial

### 3. Hermite Interpolation (Divided Difference Method)

   - Constructs a Hermite interpolating polynomial using divided differences.
   - **Test Case:** Uses `x_values = [3.6, 3.6, 3.8, 3.8, 3.9, 3.9]` with corresponding function and derivative values to generate an approximation matrix.

### 4. Cubic Spline Interpolation

   - Computes cubic spline interpolation for a set of given points.
   - **Test Case:** Uses data points `x = [2, 5, 8, 10]` and `y = [3, 5, 7, 9]` to compute:
     - System matrix `A`
     - Solution set `B`
     - Vector `X` (solution of the system)

   ## Notes
   
   - The test cases output intermediate and final results to help in verification.
   - Ensure dependencies are installed before running the tests.


