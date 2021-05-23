import Node as n
import Edge as e
import Graph as g
import numpy as np
import time

class Reader:

    def read_from_path(self, path):

        # For checking the runtime of the program
        start_time = time.time()

        # Opening the file and writing the content to lines array
        with open(path) as f:
            lines = f.readlines()

        # Removing \n's from the lines
        new_lines = []
        for line in lines:
            line = line.replace('\n', '')
            new_lines.append(line)

        lines = new_lines

        graph = g.Graph()

        # Getting the vertex count from the data
        line = lines[0]
        N = int(line)
        lines.remove(line)
        graph.N = N

        # Getting the edge count from the data
        line = lines[0]
        E = int(line)
        lines.remove(line)
        graph.E = E

        # Getting the kingdom size from the data
        line = lines[0]
        M = int(line)
        lines.remove(line)
        graph.M = M

        node_lines = lines[:N]
        edge_lines = lines[N:]

        max_kingdom = 0
        i = 0
        for line in node_lines:

            info = line.split()
            id = int(info[0])
            kingdom = int(info[1])

            node = n.Node(id, kingdom, [], False)

            graph.nodes.append(node)
            print("Node added :", i)
            i += 1
            if kingdom > max_kingdom:
                max_kingdom = kingdom

        graph.K = max_kingdom

        j = 0
        for line in edge_lines:

            info = line.split()
            src = int(info[0])
            dst = int(info[1])

            edge = e.Edge(src, dst)
            graph.edges.append(edge)
            print("Edge added :", j)

            j += 1

        graph.neighbors_from_edges()

        print()
        graph.info()
        print("\nInput reading finished in %.8s seconds" % (time.time() - start_time))

        return graph



