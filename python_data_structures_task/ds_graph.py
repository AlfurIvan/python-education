"""Graph implementation"""

from ds_linked_list import SingleLinkedList


class Node:
    """Graph node"""
    def __init__(self, value):
        self.value = value
        self.neighbours = SingleLinkedList()


class Graph:
    """Graph class"""
    def __init__(self):
        self.vertices = SingleLinkedList()
        self.edges = SingleLinkedList()
        self.length = 0
        self.num = 0

    def insert(self, neighbours=None):
        """method to dd new node"""
        node = Node(self.num)
        self.vertices.append_item(node)
        if neighbours:
            self.add_neighbours(neighbours, node)
            self.add_edges(node)
        self.length += 1
        self.num += 1

    def add_neighbours(self, neighbours, node):
        """method to add node neighbours"""
        for i in range(neighbours.list_length()):
            for j in range(self.vertices.list_length()):
                if self.vertices[j].value == neighbours[i]:
                    node.neighbours.append_item(self.vertices[j])

    def add_edges(self, node):
        """method to add edges with node"""
        for k in range(node.neighbours.list_length()):
            edge = SingleLinkedList()
            edge.append_item(node)
            edge.append_item(node.neighbours[k])
            self.edges.append_item(edge)

    def lookup(self, value):
        """Search node by value"""
        for node in self.breadth_first():
            if node.value == value:
                return node

        return "No node with such value!"

    def delete(self, del_node):
        """Delete node by link"""
        for node in self.breadth_first():
            if node == del_node:
                ind = self.vertices.lookup(node)
                self.vertices.delete_item(ind)
                self.length -= 1
                self.delete_edges_neighbours(node)
                break

        else:
            print("No such node!")

    def delete_edges_neighbours(self, node):
        """Delete node neighbours and edges"""
        j = 0
        while j < self.edges.list_length():
            if self.edges[j][0] == node or self.edges[j][1] == node:
                self.edges.delete_item(j)
                j -= 1
            j += 1

        for p in range(self.vertices.list_length()):
            for i in self.vertices[p].neighbours:
                if i.value == node:
                    self.vertices[p].neighbours.delete(self.vertices[p].neighbours.lookup(i.value))

    def breadth_first(self):
        """
        breadth-first search algorithm takes
        the possibility of having no neighbors
        """
        visited = SingleLinkedList()
        find_queue = SingleLinkedList()
        index = 0
        visited.append_item(self.vertices[index])
        find_queue.append_item(self.vertices[index])

        while not find_queue.is_empty():
            node = find_queue[0]
            find_queue.delete_item(0)

            yield node

            for k in range(node.neighbours.length):
                if node.neighbours[k] not in visited:
                    visited.append_item(node.neighbours[k])
                    find_queue.append_item(node.neighbours[k])

            if find_queue.is_empty() and index < self.vertices.list_length() - 1:
                index += 1
                visited.append_item(self.vertices[index])
                find_queue.append_item(self.vertices[index])


gr_ex = Graph()
gr_ex.insert(None)
ex = SingleLinkedList()
ex.append_item(0)
gr_ex.insert(ex)
ex1 = SingleLinkedList()
ex1.append_item(0)
ex1.append_item(1)
gr_ex.insert(ex1)
ex2 = SingleLinkedList()
ex2.append_item(1)
ex2.append_item(2)
gr_ex.insert(ex2)
print("Graph vertices and their neighbours:")
for d in gr_ex.vertices:
    print(d.data.value, ": ", end="", sep='')
    for t in range(d.data.neighbours.length):
        print(d.data.neighbours[t].value, end=' ')
    print()
print("Graph edges:")
for d in gr_ex.edges:
    print(d.data[0].value, '-', d.data[1].value)
print("Lookup 2:")
print(gr_ex.lookup(2))
my_node = gr_ex.vertices[2]
gr_ex.delete(my_node)
print("Graph vertices and their neighbours after delete 2:")
for d in gr_ex.vertices:
    print(d.data.value, ": ", end="", sep='')
    for t in range(d.data.neighbours.length):
        print(d.data.neighbours[t].value, end=' ')
    print()
print("Graph edges after delete 2:")
for d in gr_ex.edges:
    print(d.data[0].value, '-', d.data[1].value)
print("Lookup 2:")
print(gr_ex.lookup(2))
