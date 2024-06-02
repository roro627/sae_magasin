def create_graph_dict(plateau):
    """
    Crée un graphe à partir du plateau
    """
    graph_dict = {}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # droite, bas, gauche, haut

    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if plateau[i][j] == 0:
                graph_dict[(i, j)] = []
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < len(plateau) and 0 <= ny < len(plateau[i]) and plateau[nx][ny] == 0:
                        graph_dict[(i, j)].append((nx, ny))

    return graph_dict


def addProductToGraph(graph_dict, pointToAdd):
    """
    Ajoute un point au graphe 
    """
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # droite, bas, gauche, haut
    graph_dict[pointToAdd] = []
    for dx, dy in directions:
        nx, ny = pointToAdd[0] + dx, pointToAdd[1] + dy
        if (nx, ny) in graph_dict:
            graph_dict[pointToAdd].append((nx, ny))
            graph_dict[(nx, ny)].append(pointToAdd)

    if len(graph_dict[pointToAdd]) == 0:
        exit("Impossible d'ajouter le point au graphe car il n'y a pas de voisin")


def from_A_To_B(graphe: dict, depart: tuple, arrivee: tuple) -> list:
    """
    Trouve le chemin le plus court entre deux points dans un graphe
    """
    
    # Créez une copie du graphe pour ne pas modifier l'original
    graphe_copy = graphe.copy()

    # Si le départ ou l'arrivée sont des murs
    if depart not in graphe_copy:
        addProductToGraph(graphe_copy, depart)

    if arrivee not in graphe_copy:
        addProductToGraph(graphe_copy, arrivee)

    assert depart in graphe_copy and arrivee in graphe_copy, "Le départ ou l'arrivée n'existe pas dans le graphe"

    deja_visite = []  # Liste pour voir les cases déjà visitées
    file_attente = [[depart]]  # File d'attente pour le parcours en largeur

    while file_attente:
        chemin = file_attente.pop(0)
        noeud = chemin[-1]

        if noeud == arrivee:
            return chemin

        if noeud not in deja_visite:
            voisins = graphe_copy[noeud]
            for voisin in voisins:
                if voisin not in chemin:  # Vérifier si le voisin n'est pas déjà dans le chemin
                    nouveau_chemin = list(chemin)
                    nouveau_chemin.append(voisin)
                    file_attente.append(nouveau_chemin)

            deja_visite.append(noeud)

    return []  # Si aucun chemin n'est trouvé


def printPath(plateau, chemin, products=[], depart=(0, 0), arrivee=(30, 1)):
    """
    Affiche le chemin sur le plateau avec les produits et les points de départ et d'arrivée
    """
    for i in range(len(plateau)):
        if i < 10:
            print(i, end='  /|\  ')
        else:
            print(i, end=' /|\  ')

        for j in range(len(plateau[i])):
            if [(i, j)] == depart or [(i, j)] == arrivee:
                print("|", end='   ')
            elif (i, j) in chemin:
                print("@", end='   ')
            elif (i, j) not in products and type(plateau[i][j]) == list or plateau[i][j] == 0:
                print('O', end='   ')
            else:
                print('X', end='   ')
        print()


def findPostionsProducts(produits, plateau):
    """
    Trouve les coordonnées des produits sur le plateau
    """   

    positions = []
    for produit in produits:
        for i in range(len(plateau)):
            for j in range(len(plateau[i])):
                if type(plateau[i][j]) == list and produit in plateau[i][j]:
                    positions.append((i, j))
                    break

    return positions


def regroupProducts(coordoneesProducts):
    """
    regroupe les produits en créant plusieurs groupes de produits qui sont proches dans la même liste,
    de plus si les produits on les mêmes coordonnées, ils sont regroupés dans le même groupe
    """
    groupes = []
    for coordonee in coordoneesProducts:
        deja_present = False
        for groupe in groupes:
            # si les coordonnées sont déjà dans un groupe on ne les ajoute pas
            if coordonee in groupe:
                deja_present = True
                break
            for coord in groupe:
                # si les coordonnées sont voisins direct (haut, bas, droite, gauche)
                if (coord[0] == coordonee[0] and abs(coord[1] - coordonee[1]) == 1) or (coord[1] == coordonee[1] and abs(coord[0] - coordonee[0]) == 1):
                    groupe.append(coordonee)
                    deja_present = True
                    break
        # si les coordonnées ne sont pas dans un groupe on les ajoute dans un nouveau groupe
        if not deja_present:
            groupes.append([coordonee])
            
    return groupes

def manhattan_distance(point1, point2):
    """
    retourne la distance de Manhattan entre deux points
    """
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def min_distance(startingpoint, group):
    """
    retourne la distance minimale entre le point de départ et le premier et dernier point du groupe
    """
    return min(manhattan_distance(startingpoint, group[0]), manhattan_distance(startingpoint, group[-1]))

def sort_by_distance(groupe, coord1):
    """
    trier les coordonées du groupe en fonction de la distance entre les coordonées grâce à l'algorithme de Manhattan
    """
    for i in range(len(groupe)):
        min_index = i
        for j in range(i + 1, len(groupe)):
            if manhattan_distance(groupe[j], coord1) < manhattan_distance(groupe[min_index], coord1):
                min_index = j
        groupe[i], groupe[min_index] = groupe[min_index], groupe[i]
    return groupe


def find_min_group(groupes, startingpoint):
    """
    Trouver le groupe le plus proche du point de départ
    """
    
    min_group = groupes[0]
    min_dist = min_distance(startingpoint, min_group)

    for group in groupes[1:]:
        dist = min_distance(startingpoint, group)
        if dist < min_dist:
            min_dist = dist
            min_group = group

    return min_group


def sortGroupProduct(groupes):
    """
    trier les groupes de produits en fonction de la distance entre les coordonées grâce à l'algorithme de Manhattan
    """
    
    for groupe in groupes:
        if len(groupe) > 1:
            coord1 = groupe[0]
            groupe = sort_by_distance(groupe, coord1)


def sortGroup(groupes, startingpoint, endingpoint):
    """
    trier les groupes de produits en fonction de la distance entre les coordonées grâce à l'algorithme de Manhattan
    """
    
    # Trouver le premier groupe
    first_group = find_min_group(groupes, startingpoint)
    groupes.remove(first_group)

    # Trouver le dernier groupe
    last_group = find_min_group(groupes, endingpoint)
    groupes.remove(last_group)

    path = [[startingpoint], first_group]
    while groupes:
        next_group = find_min_group(groupes, path[-1][-1])
        groupes.remove(next_group)
        path.append(next_group)
    path.append(last_group)
    path.append([endingpoint])

    return path


# les produits disparraissent dans cette fonction
def makeFinalPath(plateau, path,coordonneProducts):
    """
    Crée le chemin final en passant par tous les groupes de produits
    """
    listPath = []
    
    for i in path:
        for j in i:
            listPath.append(j)

    finalPath = []
    for i in range(len(listPath)-1):
        segment = from_A_To_B(create_graph_dict(plateau), listPath[i], listPath[i+1])
        finalPath += segment
    return finalPath

def detectTurn(path):
    """
    Détecte les virages dans le chemin
    """
    turnList = []


    for i in range(1,len(path)-1):
        if path[i-1][0] != path[i][0] and path[i][0] != path[i+1][0]:
            if len(turnList) == 0:
                turnList.append([path[0],path[i]])
            else:
                turnList.append([turnList[-1][1],path[i]])

        if path[i-1][1] != path[i][1] and path[i][1] != path[i+1][1]:
            if len(turnList) == 0:
                turnList.append([path[0],path[i]])
            else:
                turnList.append([turnList[-1][1],path[i]])
            
    print(turnList)
    return turnList

if __name__ == '__main__':
    plateau2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, ["C\u00e9leri"], ["Champignons"], ["Chou", "Chou de Bruxelles"], 0, 0, ["Chou-rouge", "Ciboulette"], ["Citrouille", "Coeur de palmier", "Courge"], 0, 0, ["\u00c9chalote"], ["Courgette"], 0, 0, ["Fenouil", "Cresson"], 0, 0, 0, 0, 0, 0, 0, 0, ["Figues s\u00e8ches"], 0, 0, ["Bi\u00e8re", "Eau min\u00e9rale", "Alcools fort"], ["Bougies"], 0, 0, ["Cure dents"], 0], [0, 0, ["Asperges"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["D\u00e9tachant", "Gants de m\u00e9nage", "Mouchoirs"]], [0, 0, 0, 0, 0, ["M\u00e2che"], ["Mac\u00e9doine"], 0, ["Germe de soja", "Gingembre"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, ["Lentilles"], ["Haricot"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Gingembre confit"], 0, 0, 0, 0, 0, 0, 0, 0, ["Compote", "Gaspacho", "Haricots vert", "Ma\u00efs", "Chips"]], [0, 0, ["Ma\u00efs"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, ["Menthe", "Navet", "Oignons"], ["Pois gourmand"], 0, 0, ["Pois mangetout", "Pomme de terre", "Potimarron"], 0, 0, 0, 0, 0, 0, ["Oyster sauce"], 0, 0, 0, 0, 0, 0, ["Cannelle"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, ["Pousses de bambou"], ["Salsifis", "Poissons pan\u00e9s", "Moules", "Maquereaux"], 0, ["Crabe"], 0, 0, 0, 0, ["Paprika"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Encornet", "\u00c9crevisses", "Andouille"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Bl\u00e9 dur", "Riz", "Pois chiches"], 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Cacao"], 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Andouillette", "Bavette (boeuf)"], ["Canard"], 0, ["Chair \u00e0 saucisse", "Origan"], 0, 0, 0, 0, ["Boulgour"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Hareng fum\u00e9", "Gambas"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Groseille"], 0, 0, 0], [0, ["Amandes"], 0, 0, 0, ["Quinoa"], 0, 0, 0, 0, 0, 0, 0, ["Cervelas"], 0, 0, ["Cro\u00fbton"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, ["Beurre de cacahu\u00e8te"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Encre Imprimante", "Crayons de couleur", "Colle", "Ciseau \u00e0 papier"], 0, 0, 0, 0, 0, 0, 0, ["Brioche"], 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, ["Dattes"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Couches b\u00e9b\u00e9", "Cr\u00e8me main"]], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Cr\u00e8me dessert"], 0, 0, 0, 0], [0, ["Brugnon"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Quenelles"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Caf\u00e9 en grains"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, ["Biscuite"], 0, 0, 0, 0, ["Margarine"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Foins", "Papier \u00e0 lettre"]], [0, ["Framboise"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["D\u00e9maquillant", "Dentifrice", "Fil dentaire", "Gel douche", "Gel spray", "Calculatrice"]], [["Pi\u00e9montaise"], 0, 0, ["P\u00e2tes \u00e0 tarte"], ["Foie gras", "Galettes", "Fromage blanc"], 0, 0, 0, 0, 0, 0, 0, 0, ["Fruits secs"], 0, 0, ["Pizzas"], 0, 0, 0, 0, 0, 0, ["Cassis", "Cl\u00e9mentine"], 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ["Abricots secs"], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    plateau2_produit = ["Asperges", "C\u00e9leri", "Champignons", "Chou", "Chou de Bruxelles", "Chou-rouge", "Ciboulette", "Citrouille", "Coeur de palmier", "Courge", "Courgette", "Cresson", "\u00c9chalote", "Fenouil", "Germe de soja", "Gingembre", "Haricot", "Lentilles", "Mac\u00e9doine", "M\u00e2che", "Ma\u00efs", "Menthe", "Navet", "Oignons", "Pois gourmand", "Pois mangetout", "Pomme de terre", "Potimarron", "Pousses de bambou", "Salsifis", "Poissons pan\u00e9s", "Moules", "Maquereaux", "Hareng fum\u00e9", "Gambas", "Encornet", "crevisses", "Crabe", "Andouille", "Andouillette", "Bavette (boeuf)", "Canard", "Cervelas", "Chair \u00e0 saucisse", "Paprika", "Oyster sauce", "Origan", "Cro\u00fbton", "Cannelle", "Boulgour", "Bl\u00e9 dur", "Riz", "Quinoa", "Pois chiches", "Abricots secs", "Amandes", "Beurre de cacahu\u00e8te", "Dattes", "Figues s\u00e8ches", "Gingembre confit", "Brugnon", "Cassis", "Cl\u00e9mentine", "Framboise", "Groseille", "Biscuite", "Brioche", "Cacao", "Caf\u00e9 en grains", "Quenelles", "Pizzas", "Pi\u00e9montaise", "P\u00e2tes \u00e0 tarte", "Galettes", "Foie gras", "Cr\u00e8me dessert", "Fromage blanc", "Margarine", "Compote", "Gaspacho", "Haricots vert", "Ma\u00efs", "Fruits secs", "Chips", "Bi\u00e8re", "Alcools fort", "Eau min\u00e9rale", "Bougies", "Cure dents", "D\u00e9tachant", "Gants de m\u00e9nage", "Mouchoirs", "Couches b\u00e9b\u00e9", "Cr\u00e8me main", "D\u00e9maquillant", "Dentifrice", "Fil dentaire", "Gel douche", "Gel spray", "Calculatrice", "Ciseau \u00e0 papier", "Colle", "Crayons de couleur", "Encre Imprimante", "Papier \u00e0 lettre", "Foins"]
    
    coordonneProducts = findPostionsProducts(plateau2_produit, plateau2)
    
    produit_regrouper = regroupProducts(coordonneProducts)
    
    sortGroupProduct(produit_regrouper)
    
    optimizedPath = sortGroup(produit_regrouper, (0, 0), (30, 1))
    
    finalPath = makeFinalPath(plateau2, optimizedPath,coordonneProducts)

    
    graphe = create_graph_dict(plateau2)
    printPath(plateau2, finalPath, coordonneProducts, optimizedPath[0], optimizedPath[-1])
    detectTurn(finalPath)