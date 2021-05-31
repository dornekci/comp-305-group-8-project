import sys

import Node as n
import Edge as e
import Graph as g
import Reader as r
import numpy as np
import time
import Solutioner as s
import Solutioner2 as s2

if __name__ == '__main__':

    path = "C:\\Users\\doruk\\Desktop\\comp-305-group-8-project\\test3_new.txt"

    start_time = time.time()

    reader = r.Reader()
    graph = reader.read_from_path(path)

    print("\nInput reading finished in %.10s seconds\n" % (time.time() - start_time))

    start_time_solver = time.time()

    solver = s2.Solutioner2(graph)
    solver.solve_graph()

    print("\nSolving the problem finished in %.10s seconds" % (time.time() - start_time_solver))

    print("Whole problem finished in %.10s seconds\n" % (time.time() - start_time))










