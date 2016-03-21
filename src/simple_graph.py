# coding=utf-8


class SimpleGraph(object):
    """Create a simple graph."""

    def __init__(self):
        """Initialize a simple graph."""
        self.graph = {}

    def add_node(self, n):
        """Add a new node to the graph."""
        self.graph[n] = []

    def nodes(self):
        """Return a list of nodes."""
        return list(self.graph.keys())

    def add_edge(self, n1, n2):
        """Add an edge to the graph pointing from n1 to n2."""
        node_list = list(self.graph.keys())
        if n1 not in node_list:
            self.add_node(n1)
        elif n2 not in node_list:
            self.add_node(n2)
        self.graph[n1].append(n2)

    def edges(self):
        """Return a list of all edges in the graph."""
        node_list = list(self.graph.keys())
        edge_list = []
        for node in node_list:
            edges = self.graph[node]
            for edge in edges:
                edge_val = (node, edge)
                edge_list.append(edge_val)
        return edge_list

    def del_node(self, n):
        """Delete a node from the graph."""
        try:
            self.graph.pop(n)
            node_list = list(self.graph.keys())
            for node in node_list:
                if n in self.graph[node]:
                    self.graph[node].remove(n)
        except KeyError:
            raise KeyError

    def del_edge(self, n1, n2):
        """Delete the edge from n1 to n2."""
        try:
            if n2 in self.graph[n1]:
                self.graph[n1].remove(n2)
            else:
                raise ValueError
        except KeyError:
            raise KeyError

    def has_node(self, n):
        """Check if the graph has node n."""
        node_list = list(self.graph.keys())
        if n in node_list:
            return True
        else:
            return False

    def neighbors(self, n):
        """Return the neighbors of node n."""
        try:
            return self.graph[n]
        except KeyError:
            raise KeyError

    def adjacent(self, n1, n2):
        """Check if n1 is connected to n2"""
        try:
            self.graph[n2]
            if n2 in self.graph[n1]:
                return True
            else:
                return False
        except KeyError:
            raise KeyError

    def dft(self, start):
        """Return a list of visited nodes for depth first traversal."""
        to_visit = [start]
        visited = []
        while to_visit:
            next_val = to_visit.pop()
            if next_val not in visited:
                visited.append(next_val)
                to_visit = to_visit + self.graph[next_val]
        return visited

    def bft(self, start):
        """Return a list of visited nodes for breadth first traversal."""
        to_visit = [start]
        visited = []
        while to_visit:
            next_val = to_visit.pop()
            if next_val not in visited:
                visited.append(next_val)
                to_visit = self.graph[next_val] + to_visit
        return visited


if __name__ == '__main__':
    new_graph = SimpleGraph()
    new_graph.graph = {'A': ['B', 'C'],
                       'B': ['D', 'E'],
                       'D': [],
                       'E': ['F'],
                       'C': ['F'],
                       'F': [],
                       }
    dft = new_graph.dft('A')
    bft = new_graph.bft('A')
    print("Depth first traversal:" + str(dft))
    print("Breadth first traversal:" + str(bft))
    new_graph.add_edge('F', 'C')
    dft = new_graph.dft('A')
    bft = new_graph.bft('A')
    print("Depth first traversal(cyclic):" + str(dft))
    print("Breadth first traversal(cyclic):" + str(bft))
