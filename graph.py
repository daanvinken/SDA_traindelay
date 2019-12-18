from trajecten import get_paths
from trajecten import station_data

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

def create_graph():
    # Execute get_paths once for the ns_paths file. If ns_data exists, you
    # can turn off the line below.
    paths = [p[0] for p in get_paths("data/ns.csv")]
    all_paths = []
    f = open("data/ns_paths.txt")
    for line in f:
        split = line.split(',')
        all_paths.append([split[0].split(' '), split[1].replace('\n', '').split(' ')[1:]])
    paths = [p[0] for p in all_paths]

    stations = station_data()

    # Get all edges and nodes of the graph
    nodes = []
    edges = []
    for p in paths:
        for i in range(len(p)):
            # Append to nodes
            current_node = p[i]
            if current_node not in nodes:
                nodes.append(current_node)
            # Append to edges
            if i != 0:
                previous_node = p[i - 1]
                if [previous_node, current_node] not in edges:
                    edges.append([previous_node, current_node])

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

    # Plot nodes
    x_values = [c[0][0] for c in node_coords]
    y_values = [c[0][1] for c in node_coords]
    texts = [c[1] for c in node_coords]

    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values)

    for i, txt in enumerate(texts):
        ax.annotate(txt, (x_values[i], y_values[i]), size=10)

    # Plot edges
    for edge in edges:
        n1_coords = [[coord[0][0], coord[0][1]] for coord in node_coords if coord[1] == edge[0]][0]
        n2_coords = [[coord[0][0], coord[0][1]] for coord in node_coords if coord[1] == edge[1]][0]
        x_values = [n1_coords[0], n2_coords[0]]
        y_values = [n1_coords[1], n2_coords[1]]

        plt.plot(x_values, y_values, color='grey', linewidth=0.5)

    plt.show()
create_graph()
