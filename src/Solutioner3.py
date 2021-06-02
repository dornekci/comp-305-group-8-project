import Graph as g
import Node as n
import Edge as e
import MutualNode as mn
import random
import time


class Solutioner3:

    def __init__(self, graph):

        self.main_graph = graph
        self.graph = graph
        self.N = graph.N  # Node count
        self.M = graph.M  # Riot size
        self.E = graph.E  # Edge count
        self.K = graph.K  # Kingdom count

        self.neighbor_dict = self.graph.neighbor_dict
        self.kingdom_dict = self.graph.kingdom_dict

        self.included_cities_dict = {}
        self.included_cities_dict_sub = {}

        self.node = 0
        self.index = {}

    def solve_graph(self):

        self.compress_graph_first_time()
        print("Compression 1 completed\n")

        for i in range(0):
            self.compress_again()
            print("Compression ", i + 2, " completed.\n")

        nodes_dict = self.divide_nodes_by_included_city_count()

        kingdom = self.find_best_kingdom_in_graph()

        return 0

    def find_best_kingdom_in_graph(self):

        best_kingdom = None
        best_kingdom_distinct_count = None

        visited_cities = []
        for node in self.graph.nodes:

            if node.get_id not in visited_cities:

                path = self.get_best_path_from_node(node.get_id())
                distinct_count = self.get_distinct_neighbor_count_from_neighbors(self.get_neighbors_of_kingdom(path))
                visited_cities += path

                if best_kingdom is None or best_kingdom_distinct_count > distinct_count:
                    best_kingdom = path
                    best_kingdom_distinct_count = distinct_count

                print("Best path found from : ", node.get_id())

        included_cities = self.get_current_kingdom_real_cities(best_kingdom)
        print("\nBest kingdom : ", best_kingdom)
        print("Included cities : ", included_cities)
        print("Distinct neighbor count : ", best_kingdom_distinct_count)

        return included_cities

    # Function for finding kingdom with least amount of distinct neighbors
    def get_best_path_from_node(self, node_id):

        # Initializing our kingdom with starting node
        current_kingdom = [node_id]

        # Included cities
        included_cities = self.included_cities_dict[node_id]

        # Adding the best neighbor to the kingdom until size reached
        while len(included_cities) < self.M:

            best_neighbor = self.select_best_neighbor(current_kingdom)


            if best_neighbor is None:
                break

            current_kingdom.append(best_neighbor)
            cities_in_neighbor = self.included_cities_dict[best_neighbor]
            included_cities = included_cities + cities_in_neighbor

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

            if self.get_current_kingdom_real_size(potential_kingdom) <= self.M:

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

            neighbor_kingdoms = self.kingdom_dict[neighbor]
            for neighbor_kingdom in neighbor_kingdoms:

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

    def get_current_kingdom_real_size(self, current_kingdom):

        size = 0
        for node_id in current_kingdom:
            included_cities = self.included_cities_dict[node_id]
            size += len(included_cities)

        return size

    def get_current_kingdom_real_cities(self, current_kingdom):

        cities = []

        for node_id in current_kingdom:
            included_cities = self.included_cities_dict[node_id]
            cities += included_cities

        return cities

    def compress_graph_first_time(self):

        new_graph = g.Graph()

        pairs = self.pair_all_nodes()
        print("Pairing completed")

        i = 1
        for key in pairs:

            pair = pairs[key]

            id = key
            kingdoms = []
            neighbors = []

            for city_id in pair:

                self.index[city_id] = id

                kingdom_id = self.kingdom_dict[city_id]

                if kingdom_id not in kingdoms:
                    kingdoms.append(kingdom_id)

                neighbors_ids = self.neighbor_dict[city_id]

                for neighbor_id in neighbors_ids:

                    if neighbor_id not in neighbors and neighbor_id not in pair:
                        neighbors.append(neighbor_id)

            self.included_cities_dict[id] = pair
            new_node = mn.MutualNode(id, kingdoms, neighbors, pair)
            new_graph.add_node(new_node)
            print("Pair ", i, " finished")
            i += 1

        self.graph = new_graph
        self.update_neighbors()

        self.graph.kingdoms_as_dict()
        self.graph.neighbors_as_dict()

        self.neighbor_dict = self.graph.neighbor_dict
        self.kingdom_dict = self.graph.kingdom_dict

    def compress_again(self):

        self.index = {}
        new_graph = g.Graph()

        pairs = self.pair_all_nodes()
        print("Pairing completed")

        i = 1
        for key in pairs:

            pair = pairs[key]

            id = key
            kingdoms = []
            neighbors = []
            included_cities = []

            for city_id in pair:
                self.index[city_id] = id

                kingdom_ids = self.kingdom_dict[city_id]
                for kingdom_id in kingdom_ids:
                    if kingdom_id not in kingdoms:
                        kingdoms.append(kingdom_id)

                neighbors_ids = self.neighbor_dict[city_id]

                for neighbor_id in neighbors_ids:

                    if neighbor_id not in neighbors and neighbor_id not in pair:
                        neighbors.append(neighbor_id)

                cities_in_it = self.included_cities_dict[city_id]
                included_cities += cities_in_it

            self.included_cities_dict_sub[id] = included_cities
            new_node = mn.MutualNode(id, kingdoms, neighbors, included_cities)
            new_graph.add_node(new_node)

            print("Pair ", i, " finished")
            i += 1

        self.included_cities_dict = self.included_cities_dict_sub
        self.included_cities_dict_sub = {}

        self.graph = new_graph
        self.update_neighbors()

        self.graph.kingdoms_as_dict()
        self.graph.neighbors_as_dict()

        self.neighbor_dict = self.graph.neighbor_dict
        self.kingdom_dict = self.graph.kingdom_dict

    def update_neighbors(self):

        for node in self.graph.nodes:

            neighbors = []
            neighbors_main = node.get_neighbors()

            for neighbor_main in neighbors_main:

                new_neighbor = self.index[neighbor_main]

                if new_neighbor not in neighbors:
                    neighbors.append(new_neighbor)

            node.neighbors = neighbors
            node.update_neighbor_count()
            node.update_cities_included_count()

    def pair_all_nodes(self):

        self.sort_graph_by_neighbor_count()
        print("Graph sorted by neighbor count.")
        paired_nodes = []

        pairs = {}
        i = 0

        for node in self.graph.nodes:

            node_id = node.get_id()

            if node_id not in paired_nodes:

                neighbors = self.neighbor_dict[node_id]

                found = False
                found_neighbor = None
                for neighbor in neighbors:

                    if neighbor not in paired_nodes:
                        found = True
                        found_neighbor = neighbor
                        break

                if found:

                    pair = [node_id, found_neighbor]
                    pairs[i] = pair
                    i += 1

                    paired_nodes.append(node_id)
                    paired_nodes.append(found_neighbor)


                else:

                    pair = [node_id]
                    pairs[i] = pair
                    i += 1

                    paired_nodes.append(node_id)


        return pairs

    def sort_graph_by_neighbor_count(self):

        nodes = self.graph.nodes

        nodes.sort(key=lambda x: x.neighbor_count, reverse=False)

        self.graph.nodes = nodes

    def divide_nodes_by_included_city_count(self):

        nodes_dict = {}
        for node in self.graph.nodes:
            included_city_count = node.get_included_cities_count()

            if included_city_count not in nodes_dict.keys():
                nodes_dict[included_city_count] = [node]

            else:
                current_array = nodes_dict[included_city_count]
                current_array.append(node)
                nodes_dict[included_city_count] = current_array

        return nodes_dict

    # Function for printing an array
    def print_array(self, array):

        print([element for element in array])

    def check(self):

        print("Current real cities in node 0: ")
        node_0 = self.graph.nodes[0]
        self.print_array(node_0.get_included_cities())