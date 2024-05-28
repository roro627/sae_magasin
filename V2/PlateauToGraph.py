graph = {
    (0, 0): {
        'adjacence': {(0, 1): 1, (1, 0): 1},
        'produit': ['pomme', 'banane']
    },
    (0, 1): {
        'adjacence': {(0, 0): 1, (1, 1): 1},
        'produit': ['orange']
    },
    (1, 0): {
        'adjacence': {(0, 0): 1, (1, 1): 1},
        'produit': ['champignon']
    },
    (1, 1): {
        'adjacence': {(0, 1): 1, (1, 0): 1},
        'produit': ['pomme']
    }
}

def dijkstra(graph, start, food_list):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while visited != set(graph):
        current_node = min((node for node in graph if node not in visited), key=lambda node: distances[node])
        visited.add(current_node)

        for neighbor, weight in graph[current_node]['adjacence'].items():
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    # Find the shortest path to collect all the food
    shortest_path = []
    current_node = start
    while food_list:
        neighbors = graph[current_node]['adjacence']
        closest_neighbors = [neighbor for neighbor in neighbors if graph[neighbor]['produit']]
        if closest_neighbors:
            closest_neighbor = min(closest_neighbors, key=lambda neighbor: distances[neighbor])
            shortest_path.append(closest_neighbor)
            current_node = closest_neighbor
            food_list = [food for food in food_list if food not in graph[closest_neighbor]['produit']]
            if len(food_list) == 0:
                break
        else:
            shortest_path.append(current_node)
            current_node = min(neighbors, key=lambda neighbor: distances[neighbor])

    # Remove two food items from the list
    if len(food_list) >= 2:
        food_list = food_list[:2]

    return shortest_path

# Utilisation de l'algorithme Dijkstra
food_list = ['pomme', 'banane', 'orange', 'champignon']
shortest_path = dijkstra(graph, (0, 0), food_list)
print(shortest_path)