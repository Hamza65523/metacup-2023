def can_build_k_decker_burger(A, B, C, K):
    total_buns = C // A + 2 * (C // B)
    total_cheese_slices = C // A + (C // B)
    total_patties = C // A + (C // B)
    return K <= total_buns and K <= total_cheese_slices and K <= total_patties

def find_largest_k_decker_burger(A, B, C):
    largest_k = 0
    for k in range(1, 101):
        if can_build_k_decker_burger(A, B, C, k):
            largest_k = k
        else:
            break
    return largest_k

def main():
    with open("input.txt", "r") as input_file:
        with open("output.txt", "w") as output_file:
            num_test_cases = int(input_file.readline())
            for i in range(num_test_cases):
                A, B, C = map(int, input_file.readline().split())
                largest_k = find_largest_k_decker_burger(A, B, C)
                output_file.write(f"Case #{i + 1}: {largest_k}\n")
    print("Output has been written to output.txt")

if __name__ == "__main__":
    main()
