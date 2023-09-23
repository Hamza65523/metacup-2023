def can_build_k_decker_burger(S, D, K):
  """Returns True if a K-decker cheeseburger can be built with the ingredients from S single and D double cheeseburgers, False otherwise."""

  # Calculate the total number of buns, cheese slices, and patties
  total_buns = S * 2 + D * 4
  total_cheese_slices = S + D * 2
  total_patties = S + D * 2

  # Check if there are enough buns to build the K-decker cheeseburger, even without the buns for the top and bottom
  if K <= total_buns - 2:
    # Check if there are enough cheese slices and patties to build the K-decker cheeseburger
    if K <= total_cheese_slices and K <= total_patties:
      return "YES"
    else:
      return "NO"
  else:
    return "NO"

# Open the input file for reading
with open("input.txt", "r") as input_file:
  # Read the number of test cases
  T = int(input_file.readline())

  # Initialize an empty list to store the results
  results = []

  # Iterate through each test case
  for i in range(1, T + 1):
    # Read S, D, and K for the current test case
    S, D, K = map(int, input_file.readline().split())

    # Call the function to check if you can build the K-decker cheeseburger
    result = can_build_k_decker_burger(S, D, K)

    # Append the result to the list of results
    results.append(f"Case #{i}: {result}")

# Open the output file for writing
with open("output.txt", "w") as output_file:
  # Write the results to the output file
  for result in results:
    output_file.write(result + "\n")
