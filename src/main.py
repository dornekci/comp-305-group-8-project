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
    # solver.solve_graph()
    solver.findAllCombinations()

    for comb in solver.all_combinations:
        for cities in comb:
           print(cities.get_id())
        print("\n")
    # print("M = ", graph.M)
    # print(solver.start_node.id)
    print("0'DAN OLAN KOMBİNASYONLAR:\n")
    for comb in solver.findPaths(graph.get_node(0), 3):
        for elements in comb:
            print(elements.get_id())
        print("\n")


