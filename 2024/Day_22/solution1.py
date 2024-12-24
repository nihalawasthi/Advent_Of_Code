def read_input(file_path):
    """Reads the input file and returns a list of initial secret numbers."""
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def next_secret_number(secret):
    """Calculates the next secret number in the sequence."""
    # Step 1: Multiply by 64 and mix
    secret ^= (secret * 64)
    secret %= 16777216

    # Step 2: Divide by 32, floor, and mix
    secret ^= (secret // 32)
    secret %= 16777216

    # Step 3: Multiply by 2048 and mix
    secret ^= (secret * 2048)
    secret %= 16777216

    return secret

def calculate_2000th_secrets(initial_secrets):
    """Simulates 2000 steps for each initial secret number and returns the 2000th secret."""
    results = []
    for secret in initial_secrets:
        for _ in range(2000):
            secret = next_secret_number(secret)
        results.append(secret)
    return results

def main():
    file_path = "Day_22/input.txt"
    initial_secrets = read_input(file_path)

    # Calculate the 2000th secret number for each buyer
    final_secrets = calculate_2000th_secrets(initial_secrets)

    # Sum up the 2000th secret numbers
    result = sum(final_secrets)
    print(f"The sum of the 2000th secret numbers is: {result}")

if __name__ == "__main__":
    main()