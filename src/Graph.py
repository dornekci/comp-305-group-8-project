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
