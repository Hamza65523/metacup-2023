def can_build_k_decker_burger(A, B, C, K):
  """Returns True if a K-decker cheeseburger can be built with the given budget and prices, False otherwise."""

  # Calculate the total number of buns, cheese slices, and patties that can be bought with the given budget.
  total_buns = C // A + 2 * (C // B)
  total_cheese_slices = C // A + (C // B)
  total_patties = C // A + (C // B)

  # Check if there are enough buns, cheese slices, and patties to build the K-decker cheeseburger.
  return K <= total_buns and K <= total_cheese_slices and K <= total_patties


def find_largest_k_decker_burger(A, B, C):
  """Returns the largest K for which a K-decker cheeseburger can be built with the given budget and prices, or 0 if you cannot build even a 1-decker cheeseburger."""

  # Initialize the largest possible K to 0.
  largest_k = 0

  # Iterate over possible values of K, starting from 1.
  for k in range(1, 101):
    # If a K-decker cheeseburger can be built with the given budget and prices, update the largest possible K.
    if can_build_k_decker_burger(A, B, C, k):
      largest_k = k

    # Otherwise, stop iterating.
    else:
      break

  # Return the largest possible K.
  return largest_k


def main():
  """Solves the Cheeseburger Corollary 2 problem."""
  # Open the input file for reading
  with open("input.txt", "r") as input_file:
    # Open the output file for writing
    with open("output.txt", "w") as output_file:
      # Read the number of test cases
      num_test_cases = int(input_file.readline())
  
      # Iterate over the test cases
      for i in range(num_test_cases):
        # Read the price of a single cheeseburger, the price of a double cheeseburger, and the budget
        A, B, C = map(int, input_file.readline().split())
  
        # Find the largest K for which a K-decker cheeseburger can be built with the given budget and prices
        largest_k = find_largest_k_decker_burger(A, B, C)
  
        # Print the result to the output file
        output_file.write(f"Case #{i + 1}: {largest_k}\n")
  
  # Close the input and output files
  input_file.close()
  output_file.close()
 


if __name__ == "__main__":
  main()
