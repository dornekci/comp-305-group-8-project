import Graph as g
import Node as n
import Edge as e
import random
import time


class Solutioner2:

    def __init__(self, graph):

        self.graph = graph
        self.N = graph.N  # Node count
        self.M = graph.M  # Riot size
        self.E = graph.E  # Edge count
        self.K = graph.K  # Kingdom count
        self.all_combinations = []
        self.start_node = None

        self.neighbor_dict = self.graph.neighbor_dict
        self.kingdom_dict = self.graph.kingdom_dict

    def solve_graph(self):

        best_kingdom = None
        best_kingdom_distinct_count = None

        for node in self.graph.nodes:

            path = self.get_best_path_from_node(node.get_id())
            distinct_count = self.get_distinct_neighbor_count_from_neighbors(self.get_neighbors_of_kingdom(path))

            if best_kingdom is None or best_kingdom_distinct_count > distinct_count:

                best_kingdom = path
                best_kingdom_distinct_count = distinct_count

            print("Best path found from : ", node.get_id())
        print("Best kingdom : ", best_kingdom)
        print("Distinct neighbor count : ", best_kingdom_distinct_count)
        return best_kingdom

    # Function for finding kingdom with least amount of distinct neighbors
    def get_best_path_from_node(self, node_id):

        current_kingdom = []
        current_kingdom.append(node_id)

        while len(current_kingdom) < self.M:

            best_neighbor = self.select_best_neighbor(current_kingdom)
            current_kingdom.append(best_neighbor)

        return current_kingdom

    # Function for selecting the best neighbor by their distinct neighbor count contribution
    def select_best_neighbor(self, current_kingdom):

        base_kingdom = current_kingdom
        all_neighbors = self.get_neighbors_of_kingdom(current_kingdom)

        best_neighbor = None
        best_neighbor_distinct_neighbor_count = None
        for neighbor in all_neighbors:

            potential_kingdom = base_kingdom + [neighbor]

            new_neighbors = self.get_neighbors_of_kingdom(potential_kingdom)
            new_neighbors_score = self.get_distinct_neighbor_count_from_neighbors(new_neighbors)

            if best_neighbor is None or best_neighbor_distinct_neighbor_count > new_neighbors_score:
                best_neighbor = neighbor
                best_neighbor_distinct_neighbor_count = new_neighbors_score

        return best_neighbor

    # Function for getting distinct kingdom count from a set of cities
    def get_distinct_neighbor_count_from_neighbors(self, neighbors):

        kingdom_array = []

        for neighbor in neighbors:

            neighbor_kingdom = self.kingdom_dict[neighbor]

            if neighbor_kingdom not in kingdom_array:
                kingdom_array.append(neighbor_kingdom)

        return len(kingdom_array)

    # Function for getting all neighbors of the current state of kingdom
    # Does not include cities that already in kingdom
    def get_neighbors_of_kingdom(self, current_kingdom):

        all_neighbors = []

        for city in current_kingdom:

            neighbors = self.neighbor_dict[city]

            for neighbor in neighbors:

                if neighbor not in all_neighbors and neighbor not in current_kingdom:
                    all_neighbors.append(neighbor)

        return all_neighbors

    def print_array(self, array):

        print([element for element in array])
