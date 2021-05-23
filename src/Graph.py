import networkx as nx
import matplotlib.pyplot as plt
import Edge as e


class Graph:

    def __init__(self):
        self.nodes = []
        self.edges = []

        self.N = 0
        self.E = 0
        self.M = 0
        self.K = 0

    def info(self):

        print("\nGraph Information:")
        print("------------------")
        print("Nodes : ", self.N, "\nEdges : ", self.E, "\nRiot Size : ", self.M, "\nKingdoms : ", self.K)

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

        if edge in self.edges:
            print("Edge is already in the edge list")

        else:
            self.edges.append(edge)

    def remove_edge(self, edge):

        if edge in self.edges:
            self.edges.remove(edge)

        else:
            print("Edge is not in edge list")

    def get_node(self, id):

        for node in self.nodes:

            if node.id == id:
                return node

        print("Node is not in graph")

    def get_edge(self, src, dst):

        for edge in self.edges:

            if edge.dst == dst & edge.src == src:
                return edge

        print("Edge is not in graph")

    def write_nodes(self):

        for node in self.nodes:
            print("ID : ", node.id, " - Kingdom : ", node.kingdom, " - Neighbors : ", node.neighbors)

    def write_edges(self):

        for edge in self.edges:
            print("Source : ", edge.src, " - Destination : ", edge.dst)

    def add_neighbor(self, id, neighbor):

        node = self.get_node(id)
        self.remove_node(node)

        node.add_neighbor(neighbor)
        self.add_node(node)

    def sort_nodes(self):

        self.nodes = sorted(self.nodes, key=lambda x: x.id)

    def sort_edges(self):

        self.edges = sorted(self.edges, key=lambda x: x.src)

    def neighbors_from_edges(self):

        adj_list = []
        i = 0
        for edge in self.edges:

            src = edge.src
            dst = edge.dst

            adj_list.append([src, dst])
            adj_list.append([dst, src])

            print("Edge addition completed : ", i)
            i += 1

        adj_list = sorted(adj_list, key = lambda x: x[0])

        neighbor_dict = {}

        index = 0
        for src in range(self.N):

            neighbor_list = []
            while adj_list[index][0] == src:

                neighbor_list.append(adj_list[index][1])
                index += 1

                if index > self.E * 2 - 1:
                    break

            print("Neighbor list found : ", src)
            neighbor_dict[src] = neighbor_list

        self.sort_nodes()

        for node in self.nodes:
            print("Completed neighboring", node.id)
            node.neighbors = neighbor_dict[node.id]


    def visualize(self):

        visedges = []
        for x in self.edges:
            visedges.append([x.src, x.dst])

        G = nx.Graph()
        G.add_edges_from(visedges)
        nx.draw_networkx(G)
        plt.show()
