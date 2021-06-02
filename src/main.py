import sys

import Node as n
import Edge as e
import Graph as g
import Reader as r
import numpy as np
import time
import Solutioner as s1
import Solutioner2 as s2
import Solutioner3 as s3

if __name__ == '__main__':

    answer_1 = [3, 4, 5, 6]
    answer_2 = [38, 126, 74, 215, 183, 109, 137, 64, 91, 218, 146, 227, 47, 29, 224, 119, 167, 145, 73, 134]

    path = "C:\\Users\\doruk\\Desktop\\comp-305-group-8-project\\test1_new.txt"

    start_time = time.time()

    reader = r.Reader()
    graph = reader.read_from_path(path)

    print("\nInput reading finished in %.10s seconds\n" % (time.time() - start_time))

    start_time_solver = time.time()

    solver = s2.Solutioner2(graph)
    solver.solve_graph()

    print("\nSolving the problem finished in %.10s seconds" % (time.time() - start_time_solver))

    print("Whole problem finished in %.10s seconds\n" % (time.time() - start_time))

    solver3 = s3.Solutioner3(graph)

    solver3.solve_graph()

    for node in solver3.graph.nodes:
        print("Node : ", node.get_id(), " Kingdoms : ", node.get_kingdom(), "Neighbors : ", node.get_neighbors(),
              " Included Cities : ", node.get_included_cities(), " City count : ", node.get_included_cities_count())















