import networkx as nx
import matplotlib.pyplot as plt


def create_graph(plateau):
    graph = nx.Graph()

    # Ajoute des sommets au graphe en fonction des objets dans le plateau
    for row in plateau:
        for column in row:
            if isinstance(column, list):
                for objet in column:
                    graph.add_node(objet)
                    

    # Ajoute des arêtes au graphe en fonction des objets dans le plateau
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if isinstance(plateau[i][j], list):
                for objet in plateau[i][j]:
                    for other_objet in plateau[i][j]:
                        if objet != other_objet:
                            graph.add_edge(objet, other_objet, weight=1)  

    return graph

def display_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    plt.show()   


products = [
    [0, 0, 0, ["Objet 1", "Objet 2"]],
    [0, 0, 0, ["Objet 3"]],
    [0, 0, ["Objet 3"], 0]
]

graph = create_graph(products)

print("Nombre de sommets:", graph.number_of_nodes())
print("Nombre d'arêtes:", graph.number_of_edges())

# Affiche les informations sur les sommets et les arêtes du graphe


for node in graph.nodes():
    print("Sommet:", node)
    
    for neighbor in graph.neighbors(node):
        
        print("Arête:", node, "->", neighbor)
        print("Pondération:", graph.get_edge_data(node, neighbor)['weight'])
        
display_graph(graph)
