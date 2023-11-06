import random
import math

# Define a class named "Points" to calculate an estimate of pi.


class Points:
    def __init__(self):
        # Initialize the object with random x and y coordinates within (0, 1).
        self.x = random.random()
        self.y = random.random()
        # Calculate the distance from the origin to the point (x, y).
        self.z = math.sqrt(self.x**2 + self.y**2)
        # Initialize counters for total points and points inside the unit circle.
        self.total_points = 0
        self.inner_points = 0

    # Define a generator function to continuously calculate the estimate of pi.
    def calculate_pi(self):
        while True:
            # Generate new random x and y coordinates.
            self.x = random.random()
            self.y = random.random()
            # Recalculate the distance from the origin.
            self.z = math.sqrt(self.x**2 + self.y**2)
            # Increment the total points count.
            self.total_points += 1
            # Check if the point is inside the unit circle and increment the inner points count accordingly.
            if self.z <= 1:
                self.inner_points += 1
            # Calculate the estimate of pi based on the current counts.
            pi_estimate = 4 * self.inner_points / self.total_points
            # Yield the current estimate of pi.
            yield pi_estimate


# Create an instance of the "Points" class to calculate pi.
pi_calculator = Points()

# Define the number of iterations to run the pi estimation.
iterations = 10000

# Create a generator to calculate pi estimates and print them at intervals.
pi_gen = pi_calculator.calculate_pi()
for i in range(iterations):
    pi_estimate = next(pi_gen)
    # Print the current estimate of pi at every 1000 iterations.
    if (i + 1) % 1000 == 0:
        print(f"Iteration {i + 1}: π ≈ {pi_estimate: .6f}")
