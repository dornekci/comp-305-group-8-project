import Graph as g
import Node as n
import Edge as e
import random
import time


class Solutioner:

    def __init__(self, graph):

        self.graph = graph
        self.N = graph.N  # Node count
        self.M = graph.M  # Riot size
        self.E = graph.E  # Edge count
        self.K = graph.K  # Kingdom count
        self.all_combinations = []
        self.start_node = None

    def solve_graph(self):

        # For checking the runtime of the program
        start_time = time.time()

        graph = self.graph
        self.start_node = random.choice(graph.nodes)
        self.find_combination(self.start_node, [self.start_node.id])

        print("\nInput reading finished in %.8s seconds" % (time.time() - start_time))

    def find_combination(self, node, current_array):

        if len(current_array) == self.M:
            self.all_combinations.append(current_array)
            return 0

        else:

            neighbors = node.neighbors

            has_neighbor = False
            for neighbor in neighbors:

                if neighbor not in current_array:
                    has_neighbor = True

            if has_neighbor:
                for neighbor in neighbors:

                    if neighbor in current_array:
                        continue

                    new_node = self.graph.get_node(neighbor)

                    branch_array = current_array
                    branch_array.append(new_node)

                    self.find_combination(new_node, branch_array)



