import numpy as np

# --- STEP 1: Creating a Multidimensional Array ---
grid = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original 3x3 Matrix:")
print(grid)
print("-" * 40)

# --- STEP 2: Accessing Values and Performing Math ---
val_top_left = grid[0, 0]
val_center   = grid[1, 1]
val_bottom_r = grid[2, 2]

sum_val = val_top_left + val_center
product_val = val_center * val_bottom_r

print(f"Extracted values: {val_top_left}, {val_center}, and {val_bottom_r}")
print(f"Math Operation 1 (Addition): {val_top_left} + {val_center} = {sum_val}")
print(f"Math Operation 2 (Multiplication): {val_center} * {val_bottom_r} = {product_val}")
print("-" * 40)

# --- STEP 3: Applying 15 NumPy Methods ---
print("Running 15 different NumPy methods on the array:\n")

print("1. Add all numbers together:   ", np.sum(grid))
print("2. Average of all numbers:     ", np.mean(grid))
print("3. Highest number in the grid: ", np.max(grid))
print("4. Lowest number in the grid:  ", np.min(grid))
print("5. Total count of numbers:     ", np.size(grid))

print("6. Grid shape (rows, columns): ", grid.shape)
print("7. Type of data (e.g., integer):", grid.dtype)
print("8. Flattened into one long line:\n", grid.flatten())
print("9. Flipped sideways (rows become columns):\n", grid.T)
print("10. Middle value of the sorted data: ", np.median(grid))

print("11. How spread out the numbers are (Std Dev): ", np.std(grid))
print("12. Square root of every number:\n", np.sqrt(grid))
print("13. Every number multiplied by itself:\n", np.square(grid))
print("14. Adding 5 to every single number:\n", np.add(grid, 5))
print("15. Multiplying every single number by 2:\n", np.multiply(grid, 2))
