import networkx as nx
from trajecten import get_paths
from trajecten import station_data
from most_delayed import get_most_delayed



import matplotlib.pyplot as plt

def get_coords(node, table):
    coord = [[t[2], t[1]] for t in table if t[0] == node]
    if len(coord) != 0:
        return [float(coord[0][0]), float(coord[0][1])]
    else:
        return []

def get_coords2(node, coords, edges):
    connected_nodes = []
    for e in edges:
        if node == e[0]:
            if e[1] not in connected_nodes:
                connected_nodes.append(e[1])
        elif node == e[1]:
            if e[0] not in connected_nodes:
                connected_nodes.append(e[0])
    connected_coords = [get_coords(node, coords) for node in connected_nodes if get_coords(node, coords) != []]

    x = sum([c[0] for c in connected_coords]) / len(connected_coords)
    y = sum([c[1] for c in connected_coords]) / len(connected_coords)
    return [x, y]

# Create a graph given all possible train paths
def create_graph():
    # Execute get_paths once for the ns_paths file.
    f = open("data/ns_paths.txt")

    all_paths = []
    for line in f:
        split = line.split(',')
        all_paths.append([split[0].split(' '), split[1].replace('\n', '').split(' ')[1:]])
    paths = [p[0] for p in all_paths]

    stations = station_data()


    delays = get_most_delayed(False)
    most_delayed = delays[0:5]
    least_delayed = delays[len(delays) - 5: len(delays)]

    coords_node = [[s[1], s[2], s[3]] for s in stations]
    least_delayed_nodes = []
    for l in least_delayed:
        least_delayed_nodes.append(get_coords(l[3], coords_node))
    x_least = [l[0] for l in least_delayed_nodes]
    y_least = [l[1] for l in least_delayed_nodes]

    most_delayed_nodes = []
    for l in most_delayed:
        most_delayed_nodes.append(get_coords(l[3], coords_node))
    x_most = [l[0] for l in most_delayed_nodes]
    y_most = [l[1] for l in most_delayed_nodes]



    # Get all edges and nodes of the graph
    nodes = []
    edges = {}
    for p in paths:
        for i in range(len(p)):
            # Append to nodes
            current_node = p[i]
            if current_node not in nodes:
                nodes.append(current_node)
            # Append to edges
            if i != 0:
                previous_node = p[i - 1]
                if (previous_node, current_node) not in edges.keys():
                    edges[(previous_node, current_node)] = 1
                else:
                    edges[(previous_node, current_node)] = edges[(previous_node, current_node)] + 1

    # Get node coordinates
    node_coords = []
    for node in nodes:
        coords = [[s[1], s[2], s[3]] for s in stations]
        # get coordinates using the coords table
        coord = get_coords(node, coords)
        # if coordinates couldn't be found, get coordinates using the connected
        # nodes
        if coord == []:
            coord = get_coords2(node, coords, edges)
        x, y = coord
        node_coords.append([[x, y], node])

    G = nx.Graph()
    for i in range(len(nodes)):
        coord = tuple(node_coords[i][0])
        name = node_coords[i][1]
        G.add_node(name, pos=coord)
    pos=nx.get_node_attributes(G,'pos')

    weighted_edges = []
    for edge_key in edges.keys():
        #convert edge to tuple, (x, y, weight)
        weight = edges[edge_key]
        #took the squared weights for better visibility
        edge = edge_key + ({'weight': weight**2},)
        weighted_edges.append(edge)

    d = dict(G.degree)
    G.add_weighted_edges_from(weighted_edges)
    for i in range(len(nodes)):
        coord = tuple(node_coords[i][0])
        name = node_coords[i][1]
        G.add_node(name, pos=coord)
    pos=nx.get_node_attributes(G,'pos')

    img = plt.imread("NLmap.gif")
    fig, ax = plt.subplots()
    #trial and error for correct values imshow
    ax.imshow(img, extent=[3.35,7.15,50.7,53.5])

    nx.draw(G,pos,node_size=10, with_labels=False, font_size = 7)
    plt.scatter(x_least, y_least, c='green')
    plt.scatter(x_most, y_most, c='red')
    plt.show()

create_graph()
