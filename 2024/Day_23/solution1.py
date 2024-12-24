from collections import defaultdict

# Load the input file
with open("Day_23/input.txt", 'r') as file:
    connections = [line.strip().split('-') for line in file.readlines()]

# Build the graph
graph = defaultdict(set)
for a, b in connections:
    graph[a].add(b)
    graph[b].add(a)

# Find all triads (sets of three interconnected nodes)
def find_triads(graph):
    triads = set()
    for node in graph:
        neighbors = graph[node]
        for neighbor1 in neighbors:
            for neighbor2 in neighbors:
                if neighbor1 != neighbor2 and neighbor2 in graph[neighbor1]:
                    triad = tuple(sorted([node, neighbor1, neighbor2]))
                    triads.add(triad)
    return triads

triads = find_triads(graph)

# Filter triads for those containing a node starting with 't'
triads_with_t = [triad for triad in triads if any(node.startswith('t') for node in triad)]

# Output the result
print(len(triads_with_t))