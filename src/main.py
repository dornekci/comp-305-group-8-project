import sys

import Node as n
import Edge as e
import Graph as g
import Reader as r
import numpy as np
import Solutioner as s


if __name__ == '__main__':

    path = "C:\\Users\\doruk\\Desktop\\comp-305-group-8-project\\test1_new.txt"

    reader = r.Reader()
    graph = reader.read_from_path(path)

    sys.setrecursionlimit(15000)

    solver = s.Solutioner(graph)
    solver.solve_graph()
    print("M = ", graph.M)
    print(solver.start_node.id)
    for comb in solver.all_combinations:
        print(comb)








