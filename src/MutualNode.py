class MutualNode:

    # The initialization function for the node class
    def __init__(self, id, kingdoms, neighbors, citiesIncluded):
        self.id = id
        self.kingdoms = kingdoms
        self.neighbors = neighbors
        self.citiesIncluded = citiesIncluded
        self.neighbor_count = len(neighbors)

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
        return self.kingdoms

    def get_included_cities(self):
        return self.citiesIncluded
