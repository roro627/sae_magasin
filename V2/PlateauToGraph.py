import heapq

def create_graph_dict(plateau):
    graph_dict = {}
    
    # Ajoute les noeuds au dictionnaire du graphe en fonction des coordonnées
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            graph_dict[(i, j)] = []
            if isinstance(plateau[i][j], list):
                graph_dict[(i, j)] = plateau[i][j]
            elif plateau[i][j] == 0:
                graph_dict[(i, j)].append(0)
    return graph_dict

def dijkstra(graph, start, aliment):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

        if aliment in graph[current_node]:
            path = []
            current_node = current_node
            while current_node != start:
                for neighbor, weight in graph[current_node].items():
                    if distances[neighbor] + weight == distances[current_node]:
                        path.insert(0, current_node)
                        current_node = neighbor
                        break
            return path

    return None
                
# Exemple d'utilisation
plateau = [
    [0, 0, ["Objet 1", 'Objet 2']],
    [0, 0, ["Objet 3"]],
    [["Objet 3"], 0, 0]
]

graph_dict = create_graph_dict(plateau)
print(graph_dict)

start = (0, 0)
item = "Objet 3"

path = dijkstra(graph_dict, start, item)
print(path)
