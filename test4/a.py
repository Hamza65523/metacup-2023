import sys

def can_reach_goal(N, A):
  """Returns True if Steve can reach his goal of eating two apples per day for the next N days with the same sum of apple weights each day, False otherwise."""

  # Calculate the total weight of all the apples Steve has already purchased.
  total_weight = sum(A)

  # If the total weight is not divisible by 2, then Steve cannot reach his goal.
  if total_weight % 2 != 0:
    return False

  # Calculate the desired weight of each apple that Steve eats each day.
  desired_weight = total_weight // 2 // N

  # If the desired weight is less than 1, then Steve cannot reach his goal.
  if desired_weight < 1:
    return False

  # Otherwise, Steve can reach his goal by buying an apple of the desired weight.
  return True


def find_smallest_apple_weight(N, A):
  """Returns the smallest possible apple weight that Steve can buy so that he can eat two apples for the next N days and have the sum of apple weights be the same every day, or -1 if doing so is impossible."""

  # Check if Steve can reach his goal.
  if not can_reach_goal(N, A):
    return -1

  # Calculate the desired weight of each apple that Steve eats each day.
  desired_weight = sum(A) // 2 // N

  # Return the desired weight.
  return desired_weight


def main():
  """Solves the Apple a Day problem."""

  # Open the input file for reading.
  with open("input.txt", "r") as input_file:
    # Read the number of test cases.
    num_test_cases = int(input_file.readline())

    # Open the output file for writing.
    with open("output.txt", "w") as output_file:
      # Iterate over the test cases.
      for i in range(num_test_cases):
        # Read the number of days.
        N = int(input_file.readline())

        # Read the weights of the apples that Steve has already purchased.
        A = list(map(int, input_file.readline().split()))

        # Find the smallest possible apple weight that Steve can buy to reach his goal.
        smallest_apple_weight = find_smallest_apple_weight(N, A)

        # Print the result to the output file.
        output_file.write("Case #%d: %d\n" % (i + 1, smallest_apple_weight))


if __name__ == "__main__":
  main()
