import Node as n
import Edge as e
import Graph as g
import numpy as np


class Reader:

    def read_from_path(self, path):

        graph = g.Graph()

        info = []
        lines = []

        with open(path) as input_file:

            for line in input_file:

                if ' ' in line:
                    line = line.rstrip("\n")
                    array = line.split()
                    lines.append([int(array[0]), int(array[1])])

                else:
                    info.append(int(line.rstrip("\n")))

        N, E, M = info
        graph.N, graph.E, graph.M = info

        node_lines = lines[:N]
        edge_lines = lines[N:]

        max_kingdom = 0
        i = 0
        for line in node_lines:

            node = n.Node(line[0], line[1], [], False)
            graph.nodes.append(node)

            print("Node added :", i)
            i += 1

            if line[1] > max_kingdom:
                max_kingdom = line[1]

        graph.K = max_kingdom

        j = 0
        for line in edge_lines:

            edge = e.Edge(line[0], line[1])
            graph.edges.append(edge)

            print("Edge added :", j)
            j += 1

        graph.neighbors_from_edges()
        graph.neighbors_as_dict()
        graph.kingdoms_as_dict()


        print()
        graph.info()

        return graph



