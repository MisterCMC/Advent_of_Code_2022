class Graph:

    def __init__(self, name):
        self.name = name
        self.neighbours = []
    
    def get_name(self):
        return self.name

    def add_neighbour(self, coords):
        self.neighbours.append(coords)
    
    def get_neighbours(self):
        return self.neighbours
