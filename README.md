# Runge-Kutta Integration for Systems of Differential Equations

This project provides an implementation of the Runge-Kutta method of order 4 for numerical integration of systems of differential equations. The Runge-Kutta method is a widely used numerical technique for solving initial value problems in systems of ordinary differential equations (ODEs).

## Features
- Performs numerical integration using the Runge-Kutta method of order 4.
- Supports systems of n differential equations.
- Allows customization of initial conditions, step size, and number of iterations.
- Provides the computed t and y values at each step.

## Getting Started
To use the Runge-Kutta integration code in your project, follow these steps:
1. Clone the repository or download the source code files.
2. Make sure you have Python and NumPy installed on your system.
3. Import the runge_kutta_system_integration function from the source code file.
4. Define your system of differential equations as a Python function that takes t and y as parameters and returns a list of dy/dt values.
5. Set the initial conditions (t0 and y0), step size (h), and number of iterations (n) according to your problem.
6. Call the runge_kutta_system_integration function with your system of equations function and the specified parameters.
7. The function will return two lists: one containing the computed t values and another containing the corresponding y values at each step.

## Example
Here's an example of how to use the Runge-Kutta integration code:

```python
import numpy as np
from runge_kutta_system_integration import runge_kutta_system_integration

def equations(t, y):
    dydt = [
        y[1],
        -y[0] + y[2],
        np.sin(y[0]) - np.cos(y[1])
    ]
    return dydt

t0 = 0  # Initial value of t
y0 = [1, 0, np.pi/4]  # Initial values of the variables
h = 0.1  # Step size
n = 10  # Number of iterations

t_values, y_values = runge_kutta_system_integration(equations, t0, y0, h, n)

for t, y in zip(t_values, y_values):
    print(f"t = {t}, y = {y}")

```
In this example, we define a system of 3 differential equations and set the initial conditions, step size, and number of iterations. The runge_kutta_system_integration function is called with these parameters, and the computed t and y values at each step are printed.

## Dependencies
> NumPy: A library for numerical computing in Python.

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License
This project is licensed under the MIT License.
## Acknowledgments
The Runge-Kutta method is a fundamental numerical integration technique, and this implementation is based on the mathematical principles described in various numerical analysis textbooks and resources.

## References
- Atkinson, Kendall E. "An Introduction to Numerical Analysis." John Wiley & Sons, 2008.
- Burden, Richard L., and J. Douglas Faires. "Numerical Analysis." Brooks/Cole, Cengage Learning, 2011.

Feel free to customize and expand upon this README file based on your specific project requirements and additional details you want to include.
