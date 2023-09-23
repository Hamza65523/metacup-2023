def can_alice_win(R, C, A, B):
  """Returns True if Alice has a guaranteed winning strategy, False otherwise."""

  # If Alice can move down to the last row, she wins.
  if A >= R:
    return True

  # If Bob can move right to the last column, he wins.
  if B >= C:
    return False

  # If the number of rows and columns are equal, then the game is a draw.
  if R == C:
    return False

  # If the number of rows is greater than the number of columns, then Alice can win by moving down to the last row.
  if R > C:
    return True

  # If the number of columns is greater than the number of rows, then Bob can win by moving right to the last column.
  if C > R:
    return False

  # If the number of rows and columns are both odd, then Alice can win by moving down to the last row.
  if R % 2 == 1 and C % 2 == 1:
    return True

  # If the number of rows and columns are both even, then Bob can win by moving right to the last column.
  if R % 2 == 0 and C % 2 == 0:
    return False

  # If the number of rows is odd and the number of columns is even, then Alice can win by moving down to the last row.
  if R % 2 == 1 and C % 2 == 0:
    return True

  # If the number of rows is even and the number of columns is odd, then Bob can win by moving right to the last column.
  if R % 2 == 0 and C % 2 == 1:
    return False

  # If none of the above conditions are met, then the game is a draw.
  return False


results = []
def main():
  """Solves the Nim Sum Dim Sum problem."""

# Open the input file for reading
with open("input.txt", "r") as input_file:
    # Read the number of test cases
    num_test_cases = int(input_file.readline())

    # Iterate over the test cases.
    for i in range(num_test_cases):
        # Read the number of rows, the number of columns, the number of steps Alice can move down, and the number of steps Bob can move right.
        R, C, A, B = map(int, input_file.readline().split())

        # Check if Alice has a guaranteed winning strategy.
        if can_alice_win(R, C, A, B):
            print("Case #%d: YES" % (i + 1))
            results.append("Case #%d: YES" % (i + 1))
        else:
            results.append("Case #%d: NO" % (i + 1))
            print("Case #%d: NO" % (i + 1))
            
# Open the output file for writing
with open("output.txt", "w") as output_file:
    # Write the results to the output file
    for result in results:
        output_file.write(result + "\n")



if __name__ == "__main__":
  main()
