import numpy as np

# Create a 5x5 array of random integers from 0 to 100
array = np.random.randint(0, 100, size=(5, 5))

# Print the array
print("5x5 Array:")
print(array)

#value at 2nd row, 3rd column
value = array[1, 2]
print("Value at 2nd row, 3rd column:", value)

#total sum of all elements
total_sum = np.sum(array)
print("Sum of all elements:", total_sum)

#mean of each row
means = np.mean(array, axis=1)
print("Mean of each row:", means)

#max value in each column
max = np.max(array, axis=0)
print("Maximum value in each column:", max)

input("Press Enter to exit...")