def process_stones(stones):
    """
    Process the list of stones according to the rules.
    """
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            half = len(str(stone)) // 2
            left = int(str(stone)[:half])
            right = int(str(stone)[half:])
            new_stones.append(left)
            new_stones.append(right)
        else:
            new_stones.append(stone * 2024)
    return new_stones


def simulate_blinks(file_path, blinks):
    """
    Simulates the blinking process for the given number of blinks.

    Parameters:
        file_path (str): Path to the input file containing initial stone numbers.
        blinks (int): Number of times to blink.

    Returns:
        int: Total number of stones after all blinks.
    """
    with open(file_path, 'r') as file:
        stones = list(map(int, file.read().strip().split()))

    for _ in range(blinks):
        stones = process_stones(stones)

    return len(stones)



def simulate_blinks_count(stones, num_blinks):
    """
    Simulate the evolution of stones by counting their behavior.
    """
    from collections import Counter
    stone_counts = Counter(stones)  # {stone_value: count}

    for _ in range(num_blinks):
        new_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:  # Even number of digits
                stone_str = str(stone)
                mid = len(stone_str) // 2
                left = int(stone_str[:mid])
                right = int(stone_str[mid:])
                new_counts[left] += count
                new_counts[right] += count
            else:
                new_counts[stone * 2024] += count
        stone_counts = new_counts
    return sum(stone_counts.values())


def main():
    file_path = "Day_11/input.txt"
    with open(file_path, 'r') as file:
        content = file.read().strip()

    blinks = 25
    total_stones = simulate_blinks(file_path, blinks)
    print(f"Total stones after {blinks} blinks: {total_stones}")
    initial_stones = list(map(int, content.split()))
    num_blinks = 75
    total_stones = simulate_blinks_count(initial_stones, num_blinks)
    print("Number of stones after 75 blinks:", total_stones)


if __name__ == "__main__":
    main()