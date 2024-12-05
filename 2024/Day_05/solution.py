from collections import defaultdict, deque

def parse_input(file_path):
    with open(file_path, 'r') as f:
        content = f.read().strip()
    rules_section, updates_section = content.split("\n\n")
    
    rules = []
    for line in rules_section.strip().split("\n"):
        x, y = map(int, line.split('|'))
        rules.append((x, y))
    
    updates = []
    for line in updates_section.strip().split("\n"):
        update = list(map(int, line.split(',')))
        updates.append(update)
    
    return rules, updates

def is_update_valid(update, rules):
    index_map = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] >= index_map[y]:
                return False
    return True

def reorder_update(update, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for x, y in rules:
        graph[x].append(y)
        in_degree[y] += 1
        in_degree[x] += 0

    update_set = set(update)
    valid_graph = {node: [] for node in update_set}
    valid_in_degree = {node: 0 for node in update_set}
    
    for x, y in rules:
        if x in update_set and y in update_set:
            valid_graph[x].append(y)
            valid_in_degree[y] += 1
    
    queue = deque([node for node in valid_in_degree if valid_in_degree[node] == 0])
    ordered_update = []
    
    while queue:
        node = queue.popleft()
        ordered_update.append(node)
        for neighbor in valid_graph[node]:
            valid_in_degree[neighbor] -= 1
            if valid_in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return ordered_update

def find_middle_page(update):
    return update[len(update) // 2]

def solve_part_one(rules, updates):
    valid_middle_sum = 0
    for update in updates:
        if is_update_valid(update, rules):
            valid_middle_sum += find_middle_page(update)
    return valid_middle_sum

def solve_part_two(rules, updates):
    incorrect_updates = []
    corrected_middle_sum = 0
    
    for update in updates:
        if not is_update_valid(update, rules):
            incorrect_updates.append(update)
    
    for update in incorrect_updates:
        corrected_update = reorder_update(update, rules)
        corrected_middle_sum += find_middle_page(corrected_update)
    
    return corrected_middle_sum

def main(file_path):
    rules, updates = parse_input(file_path)
    part_one_result = solve_part_one(rules, updates)
    part_two_result = solve_part_two(rules, updates)
    
    print(f"Part One: Total sum of middle page numbers for valid updates: {part_one_result}")
    print(f"Part Two: Total sum of middle page numbers for corrected updates: {part_two_result}")

if __name__ == "__main__":
    file_path = "day_5.txt"
    main(file_path)