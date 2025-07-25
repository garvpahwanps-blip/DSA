# day_1_complexity.py

# Function 1: O(1) - Constant Time
def get_first_element(arr):
    """Returns the first element of a list. O(1) operation."""
    if not arr:
        return None
    return arr[0]

# Function 2: O(n) - Linear Time
def find_element_linear(arr, target):
    """Searches for a target in a list linearly. O(n) operation."""
    for element in arr:
        if element == target:
            return True
    return False

# Function 3: O(n^2) - Quadratic Time
def find_all_pairs_sum_n_squared(arr, target_sum):
    """Finds pairs that sum to target using nested loops. O(n^2) operation."""
    n = len(arr)
    found_pairs = []
    for i in range(n):
        for j in range(n):
            if arr[i] + arr[j] == target_sum:
                found_pairs.append((arr[i], arr[j]))
    return found_pairs

# --- Test Cases ---
my_list = [10, 20, 30, 40, 50]

print(f"First element: {get_first_element(my_list)}")
print(f"Found 30 (linear): {find_element_linear(my_list, 30)}")
print(f"Found 99 (linear): {find_element_linear(my_list, 99)}")
print(f"Pairs for sum 70 (n^2): {find_all_pairs_sum_n_squared(my_list, 70)}")
print(f"Pairs for sum 100 (n^2): {find_all_pairs_sum_n_squared(my_list, 100)}")

