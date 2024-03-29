# Pi Estimation with Monte Carlo Simulation

This project aims to estimate the mathematical constant π (pi) using the Monte Carlo method. It's a simple Python program that demonstrates how to use random points to approximate π.

## Project Purpose

The primary goal of this project is to provide a basic example of how you can estimate π using a Monte Carlo simulation. This technique involves generating random points within a square and calculating how many of them fall inside a unit circle. By doing this for a large number of iterations, we can obtain a reasonable estimate for π.

## Project Logic

The project follows these main steps:

1. Initialize an instance of the `Points` class, which will help with the calculations.

2. Inside the `Points` class:
   - Randomly generate coordinates (x, y) within the range [0, 1).
   - Calculate the distance from the origin to the point (x, y).
   - Keep track of the total number of generated points and the number of points that fall inside the unit circle.

3. Create a generator function `calculate_pi` within the `Points` class that iteratively:
   - Generates new random points.
   - Checks if the point falls inside the unit circle and updates the counts accordingly.
   - Calculates the estimate of π based on the counts.
   - Yields the current estimate of π.

4. Create an instance of the `Points` class to perform the calculations.

5. Specify the number of iterations to run the π estimation, e.g., 1,000,000.

6. Create a generator for estimating π and print the results at intervals.

The program calculates and prints the current estimate of π at every 1000 iterations, showing how the estimate approaches the true value of π as more iterations are performed.

Feel free to modify the number of iterations to achieve a more accurate estimate or adapt the code for educational purposes.

## Getting Started

To run the project, make sure you have Python installed on your system. Then, execute the Python script `pi_estimation.py`.

```bash
python pi_estimation.py
