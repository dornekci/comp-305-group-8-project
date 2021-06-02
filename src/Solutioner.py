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

        self.neighbor_dict = self.graph.neighbor_dict
        self.kingdom_dict = self.graph.kingdom_dict

    def solve_graph(self):

        self.findAllCombinations()

        solution_path = []
        solution_neighbors = []
        solution_neighbor_count = 99999999

        i = 1
        total = len(self.all_combinations)
        for comb in self.all_combinations:

            comb_array = [cities.get_id() for cities in comb]
            neighbors = self.getDistinctNeighbors(comb_array)
            distinct_neighbor_count = self.get_distinct_neighbor_count_from_neighbors(neighbors)

            print("This is ", i, "'th comb done from total ", total, " nodes")
            i += 1
            if len(solution_path) == 0 or solution_neighbor_count > distinct_neighbor_count:
                solution_path = comb_array
                solution_neighbors = neighbors
                solution_neighbor_count = distinct_neighbor_count

        self.print_array(solution_path)
        print("Distinct neighbor count : ", solution_neighbor_count)


    def findAllCombinations(self):

        i = 1
        total = len(self.graph.nodes)
        for node in self.graph.nodes:
            print("This is ", i, "'th node done from total ", total, " nodes")
            i += 1

            self.all_combinations.extend(self.findPaths2(node, self.M - 1))

    def findPaths(self, node, length):

        if length == 0:
            return [[node]]

        paths = [[node] + path for neighbor in self.graph.get_node(node.get_id()).get_neighbors() for path in
                 self.findPaths(self.graph.get_node(neighbor), length - 1) if node not in path]
        return paths

    def findPaths2(self, node, length):

        if length == 0:
            return [[node]]

        paths = []
        for neighbor in self.graph.get_node(node.get_id()).get_neighbors():
            for path in self.findPaths2(self.graph.get_node(neighbor), length - 1):
                if node not in path:
                    paths.append([node] + path)

        return paths

    # Function for getting distinct kingdom count from a set of cities
    def get_distinct_neighbor_count_from_neighbors(self, neighbors):

        kingdom_array = []

        for neighbor in neighbors:

            neighbor_kingdom = self.kingdom_dict[neighbor]

            if neighbor_kingdom not in kingdom_array:
                kingdom_array.append(neighbor_kingdom)

        return len(kingdom_array)

    def getDistinctNeighbors(self, array):

        allNeighbors = []

        for city_id in array:
            city_node = self.graph.get_node(city_id)
            neighbors = city_node.get_neighbors()

            for neighbor in neighbors:

                if (neighbor not in allNeighbors) & (neighbor not in array):
                    allNeighbors.append(neighbor)

        return allNeighbors

    def print_array(self, array):

        print([element for element in array])
