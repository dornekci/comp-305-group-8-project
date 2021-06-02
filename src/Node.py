class Node:

    # The initialization function for the node class
    def __init__(self, id, kingdom, neighbors, isInKingdom):
        self.id = id
        self.kingdom = kingdom
        self.neighbors = neighbors
        self.isInKingdom = isInKingdom
        self.neighbor_count = len(neighbors)

    # Function for adding a neighbor to neighbor list
    def add_neighbor(self, neighbor):

        if neighbor in self.neighbors:
            print("Neighbor is already in neighbor list")

        else:
            self.neighbors.append(neighbor)

    # Function for removing a neighbor from the neighbor list
    def remove_neighbor(self, neighbor):

        if neighbor in self.neighbors:
            self.neighbors.remove(neighbor)

        else:
            print("Neighbor is not in the neighbor list")

    def get_neighbor_count(self):

        return self.neighbor_count

    def update_neighbor_count(self):

        self.neighbor_count = len(self.neighbors)

    def sort_neighbors(self):

        self.neighbors.sort()

    def get_neighbors(self):

        return self.neighbors

    def get_id(self):
        return self.id

    def get_kingdom(self):
        return self.kingdom