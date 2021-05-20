import Node as n
import Edge as e
import Graph as g


def read_txt(path):
    return 0

def main():


if __name__ == '__main__':
    testGraph = g.Graph()

    node0 = n.Node(0, 0, [0, 1, 1, 0], False)
    testGraph.add_node(node0)

    node1 = n.Node(1, 1, [1, 0, 0, 0], False)
    testGraph.add_node(node1)

    node2 = n.Node(2, 2, [1, 0, 0, 1], False)
    testGraph.add_node(node0)

    node3 = n.Node(3, 0, [0, 1, 1, 0], False)
    testGraph.add_node(node3)

    node4 = n.Node(4, 1, [1,1,0,0], False)
    testGraph.add_node(node4)

    edge01 = e.Edge(0,1)
    testGraph.add_edge(edge01)

    edge02 = e.Edge(0,2)
    testGraph.add_edge(edge02)

    edge05 = e.Edge(0,5)
    testGraph.add_edge(edge05)

    edge27 = e.Edge(2,7)
    testGraph.add_edge(edge27)