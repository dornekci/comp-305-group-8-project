import Node as n
import Edge as e
import Graph as g
import Reader as r
import numpy as np
import time
import Solutioner as s1
import Solutioner2 as s2
import Solutioner3 as s3


class Ahmet:

    def operation(self):

        path1 = "C:\\Users\\doruk\\Desktop\\comp-305-group-8-project\\test1_new.txt"
        path2 = "C:\\Users\\doruk\\Desktop\\comp-305-group-8-project\\test2_new.txt"
        path3 = "C:\\Users\\doruk\\Desktop\\comp-305-group-8-project\\test3_new.txt"

        test_file_input = int(input("Write '1' for test1\nWrite '2' for test2\nWrite '3' for "
                                    "test3\nSelect the test input :"))
        algorithm_input = int(input("Write '1' for Algorithm 1\nWrite '2' for Algorithm 2\nWrite '3' for "
                                    "Algorithm 3\nSelect the algorithm :"))

        if algorithm_input == 2:
            version_input = int(input("Write '1' for version 1\nWrite '2' for version 2\nSelect version of algorithm 2 :"))

        path = None
        if test_file_input == 1:
            path = path1

        elif test_file_input == 2:
            path = path2

        elif test_file_input == 3:
            path = path3

        start_time = time.time()

        reader = r.Reader()

        graph = reader.read_from_path(path)

        input_reading_time = time.time() - start_time

        start_time_solver = time.time()

        solver = None
        if algorithm_input == 1:
            solver = s1.Solutioner(graph)

        elif algorithm_input == 2:
            solver = s2.Solutioner2(graph)

        elif algorithm_input == 3:
            solver = s3.Solutioner3(graph)

        if algorithm_input == 2:

            if version_input == 1:
                solver.solve_graph_1()

            elif version_input == 2:
                solver.solve_graph_2()

        else:
            solver.solve_graph()

        solving_time = time.time() - start_time_solver
        total_time = solving_time + input_reading_time

        print("\nInput reading finished in %.8s seconds" % input_reading_time)

        print("Solving the problem finished in %.8s seconds" % solving_time)

        print("Whole problem finished in %.8s seconds\n" % total_time)
