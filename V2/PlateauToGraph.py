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

# Exemple d'utilisation
plateau = [
    [0, 0, ["Objet 1", 'Objet 2']],
    [0, 0, ["Objet 3"]],
    [["Objet 3"], 0, 0]
]

graph_dict = create_graph_dict(plateau)
print(graph_dict)