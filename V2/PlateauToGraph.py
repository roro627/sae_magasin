

graph = {
    (0, 0): {
        'adjacence': {(0, 1): 1, (1, 0): 1},
        'produit': []
    },
    (0, 1): {
        'adjacence': {(0, 0): 1, (1, 1): 1},
        'produit': ['orange']
    },
    (0, 2): {
        'adjacence': {(0, 1): 1, (1, 1): 1},
        'produit': ['pomme', 'banane']
    },
    (1, 0): {
        'adjacence': {(0, 0): 1, (1, 1): 1},
        'produit': ['champignon']
    },
    (1, 1): {
        'adjacence': {(0, 1): 1, (0, 2): 1, (1, 0): 1},
        'produit': ['pomme']
    },
    (1, 2): {
        'adjacence': {(0, 2): 1, (1, 1): 1},
        'produit': ['orange']
    },
    (2, 0): {
        'adjacence': {(1, 0): 1, (1, 1): 1},
        'produit': []
    },
    (2, 1): {
        'adjacence': {(1, 1): 1, (1, 2): 1},
        'produit': ['poire']
    },
    (2, 2): {
        'adjacence': {(1, 2): 1},
        'produit': ['melon']
    }
}

def dijkstra(graph, start, food_items):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = priority_queue[0]
        for i in range(len(priority_queue) - 1):
            priority_queue[i] = priority_queue[i + 1]
        priority_queue.pop()

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node]['adjacence'].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.append((distance, neighbor))
                priority_queue.sort()

    shortest_path = []
    current_node = start

    while current_node not in food_items:
        min_distance = float('inf')
        for neighbor, weight in graph[current_node]['adjacence'].items():
            distance = distances[neighbor] - weight

            if distance < min_distance and set(graph[neighbor]['produit']).intersection(food_items):
                min_distance = distance
                current_node = neighbor

        if min_distance == float('inf'):
            break

        shortest_path.append(current_node)
        current_node = current_node

    return shortest_path
# Utilisation de l'algorithme Dijkstra
start_node = (0, 0)
food_items = ['pomme', 'banane']
shortest_path = dijkstra(graph, start_node, food_items)
print(shortest_path)