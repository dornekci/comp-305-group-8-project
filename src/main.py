class Edge:

    # The initialization function for the edge class
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst


class Node:

    # The initialization function for the node class
    def __init__(self, id, kingdom, neighbors, isInKingdom):
        self.id = id
        self.kingdom = kingdom
        self.neighbors = neighbors
        self.isInKingdom = isInKingdom

    # Function for adding a neighbor to neighbor list
    def add_neighbor(self, neighbor):

        if neighbor in self.neighbors:
            print("Neighbor is already in neighbor list")

        else:
            self.neighbors.append(neighbor)

    # Function for removing a neighbor from the neighbor list
    def remove_neighbor(self, neighbor):

        if neighbor in self.neighbors:
            self.neighbors.remove(neighbor)

        else:
            print("Neighbor is not in the neighbor list")


class Graph:
    nodes = []
    edges = []

    def add_node(self, node):

        if node in self.nodes:
            print("Node is already in the node list")

        else:
            self.nodes.append(node)

    def remove_node(self, node):

        if node in self.nodes:
            self.nodes.remove(node)

        else:
            print("Node is not in node list")

    def add_edge(self, edge):

        if edge in self.edge:
            print("Edge is already in the edge list")

        else:
            self.edges.append(edge)

    def remove_edge(self, edge):

        if edge in self.edges:
            self.edges.remove(edge)

        else:
            print("Edge is not in edge list")


def read_txt(path):
    return 0


if __name__ == '__main__':
    print(0)
