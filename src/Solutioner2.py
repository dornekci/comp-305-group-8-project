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

        self.neighbor_dict = self.graph.neighbor_dict
        self.kingdom_dict = self.graph.kingdom_dict

    # Function for solving the problem by finding the best path from every node
    # and getting the best one from them
    def solve_graph(self):

        best_kingdom = None
        best_kingdom_distinct_count = None

        visited_cities = []
        for node in self.graph.nodes:

            if node.get_id() not in visited_cities:

                path = self.get_best_path_from_node(node.get_id())
                distinct_count = self.get_distinct_neighbor_count_from_neighbors(self.get_neighbors_of_kingdom(path))
                visited_cities += path

                if best_kingdom is None or best_kingdom_distinct_count > distinct_count:

                    best_kingdom = path
                    best_kingdom_distinct_count = distinct_count

                print("Best path found from : ", node.get_id())

        print("\nBest kingdom : ", best_kingdom)
        print("Distinct neighbor count : ", best_kingdom_distinct_count)
        return best_kingdom

    # Function for finding kingdom with least amount of distinct neighbors
    def get_best_path_from_node(self, node_id):

        # Initializing our kingdom with starting node
        current_kingdom = [node_id]

        # Adding the best neighbor to the kingdom until size reached
        while len(current_kingdom) < self.M:

            best_neighbor = self.select_best_neighbor(current_kingdom)
            current_kingdom.append(best_neighbor)

        return current_kingdom

    # Function for selecting the best neighbor by their distinct neighbor count contribution
    def select_best_neighbor(self, current_kingdom):

        # Getting all neighbors from every city in the kingdom
        all_neighbors = self.get_neighbors_of_kingdom(current_kingdom)

        # Variables for storing best candidate for new city in kingdom
        best_neighbor = None
        best_neighbor_distinct_neighbor_count = None

        for neighbor in all_neighbors:

            # Potential new kingdom when this neighbor is added to the kingdom
            potential_kingdom = current_kingdom + [neighbor]

            # All neighbors of this new potential kingdom and distinct neighbor count
            new_neighbors = self.get_neighbors_of_kingdom(potential_kingdom)
            new_distinct_neighbor_count = self.get_distinct_neighbor_count_from_neighbors(new_neighbors)

            # If the new distinct neighbor count is better than the previously stored one's
            # replacing the best candidate with this new neighbor
            if best_neighbor is None or best_neighbor_distinct_neighbor_count > new_distinct_neighbor_count:
                best_neighbor = neighbor
                best_neighbor_distinct_neighbor_count = new_distinct_neighbor_count

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

        # We check the neighbors of all cities in the kingdom
        for city in current_kingdom:

            # Neighbors of the city
            neighbors = self.neighbor_dict[city]

            for neighbor in neighbors:

                # If the neighbor not in kingdom or already in all_neighbors list
                if neighbor not in all_neighbors and neighbor not in current_kingdom:
                    all_neighbors.append(neighbor)

        return all_neighbors

    # Function for printing an array
    def print_array(self, array):

        print([element for element in array])
