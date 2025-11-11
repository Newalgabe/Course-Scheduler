"""
Graph Coloring Module for Course Scheduling
Implements greedy algorithm for graph coloring
"""


class Graph:
    """Represents a graph where vertices are courses and edges are conflicts"""
    
    def __init__(self):
        self.adjacency_list = {}
        self.vertices = []
    
    def add_vertex(self, vertex):
        """Add a vertex (course) to the graph"""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            self.vertices.append(vertex)
    
    def add_edge(self, vertex1, vertex2):
        """Add an edge (conflict) between two vertices"""
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)
        
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)
    
    def get_degree(self, vertex):
        """Get the degree (number of neighbors) of a vertex"""
        return len(self.adjacency_list.get(vertex, []))
    
    def get_vertices_sorted_by_degree(self):
        """Get vertices sorted by degree in descending order"""
        return sorted(self.vertices, key=self.get_degree, reverse=True)
    
    def get_neighbors(self, vertex):
        """Get all neighbors of a vertex"""
        return self.adjacency_list.get(vertex, [])


def greedy_coloring(graph):
    """
    Greedy algorithm for graph coloring
    Returns a dictionary mapping vertices to colors (time slots)
    """
    if not graph.vertices:
        return {}
    
    # Sort vertices by degree (largest first) for better coloring
    vertices_sorted = graph.get_vertices_sorted_by_degree()
    
    # Dictionary to store color assignment
    colors = {}
    
    # Assign colors to vertices
    for vertex in vertices_sorted:
        # Find used colors in neighbors
        used_colors = set()
        for neighbor in graph.get_neighbors(vertex):
            if neighbor in colors:
                used_colors.add(colors[neighbor])
        
        # Find the smallest available color
        color = 0
        while color in used_colors:
            color += 1
        
        colors[vertex] = color
    
    return colors


def get_color_count(coloring):
    """Get the number of colors used in the coloring"""
    if not coloring:
        return 0
    return max(coloring.values()) + 1


def validate_coloring(graph, coloring):
    """Validate that the coloring is correct (no adjacent vertices have same color)"""
    for vertex in graph.vertices:
        if vertex not in coloring:
            return False
        vertex_color = coloring[vertex]
        for neighbor in graph.get_neighbors(vertex):
            if neighbor in coloring and coloring[neighbor] == vertex_color:
                return False
    return True



