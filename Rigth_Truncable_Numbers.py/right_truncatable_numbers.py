# Right-Truncatable Primes: Filters numbers from a file that remain prime
# when digits are removed from the right, within a user-defined range.
import os

def is_prime(number):
    number = int(number)
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def read_file(numbers_path):
    try:
        with open(numbers_path, "r") as file:
            content = file.read()
            return content.strip().split()
    except FileNotFoundError:
        print("Input file not found.")
        return []

def filter_numbers(numbers_lst, lower_limit, upper_limit):
    filtered_numbers = []

    for number_str in numbers_lst:
        num_val = int(number_str)
        # Check if within range (inclusive of lower, exclusive of upper)
        if lower_limit <= num_val <= upper_limit:
            # Check if it is Right-Truncatable
            is_right_truncatable = True
            for i in range(len(number_str)):
                truncated_part = number_str[:len(number_str) - i]
                if not is_prime(truncated_part):
                    is_right_truncatable = False
                    break
            
            if is_right_truncatable:
                filtered_numbers.append(number_str)
                
    return filtered_numbers

def main():
    # Uses files relative to this script's directory so running from
    # a different working directory still finds them.
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, "numbers.txt")
    output_path = os.path.join(base_dir, "filtered_numbers.txt")
    
    numbers_lst = read_file(input_path)
    if not numbers_lst:
        return

    try:
        limits = input("Enter the limits of the range (e.g., 13 200): ").split()
        lower_limit = int(limits[0])
        upper_limit = int(limits[1])
    except (ValueError, IndexError):
        print("Invalid input. Please enter two numbers separated by a space.")
        return

    filtered = filter_numbers(numbers_lst, lower_limit, upper_limit)

    if not filtered:
        print("No Number Found")
    else:
        # Write to file
        with open(output_path, "w") as file:
            for n in filtered:
                file.write(f"{n}\n")
        
        print(f"The file contains {len(filtered)} right-truncatable prime numbers between {lower_limit} and {upper_limit}")

if __name__ == "__main__":
    main()