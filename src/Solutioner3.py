import Graph as g
import Node as n
import Edge as e
import MutualNode as mn
import random
import time


class Solutioner3:

    def __init__(self, graph):

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

        self.graph.kingdoms_as_dict()
        self.graph.neighbors_as_dict()

        self.neighbor_dict = self.graph.neighbor_dict
        self.kingdom_dict = self.graph.kingdom_dict

        self.compress_again()

        self.graph.kingdoms_as_dict()
        self.graph.neighbors_as_dict()

        self.neighbor_dict = self.graph.neighbor_dict
        self.kingdom_dict = self.graph.kingdom_dict

        return 0

    def compress_graph_first_time(self):

        new_graph = g.Graph()

        pairs = self.pair_all_nodes()

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

        self.graph = new_graph
        self.update_neighbors()

    def compress_again(self):

        self.index = {}
        new_graph = g.Graph()

        pairs = self.pair_all_nodes()

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

        self.included_cities_dict = self.included_cities_dict_sub
        self.included_cities_dict_sub = {}

        self.graph = new_graph
        self.update_neighbors()

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
