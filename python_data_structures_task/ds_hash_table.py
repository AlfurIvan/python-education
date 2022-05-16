"""Hash Table module"""

from ds_linked_list import SingleLinkedList


class Node:
    """Hash Table node"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """Hash Table class"""
    def __init__(self):
        self.capacity = 30
        self.length = 0
        self.table = SingleLinkedList()
        for _ in range(30):
            self.table.append_item(None)

    @staticmethod
    def hash(key):
        """Returns hash for current key"""
        hash_sum = 0
        for i in key:
            hash_sum += ord(i)
        return hash_sum % 30

    def insert(self, key, value):
        """
        Add new key and value in table, if the cell is not
        empty - creates a linked list writes to it the
        key-value pair that was in the cell and the new pair
        """
        self.length += 1
        index = self.hash(key)
        node = self.table[index]
        if node is None:
            self.table[index] = Node(key, value)
        elif not isinstance(self.table[index], SingleLinkedList):
            self.table[index] = SingleLinkedList()
            self.table[index].append_item(node)
            self.table[index].append_item(Node(key, value))
        else:
            self.table[index].append_item(Node(key, value))

    def lookup(self, key):
        """Search value by key"""

        try:
            index = self.hash(key)
            node = self.table[index]
            if not isinstance(node, SingleLinkedList):
                return node.value
            for i in range(node.length):
                if node[i].key == key:
                    return node[i].value
            return None
        except AttributeError:
            print('Nein')

    def delete(self, key):
        """Delete key-value pair by key"""
        index = self.hash(key)
        node = self.table[index]
        if not isinstance(node, SingleLinkedList):
            self.table[index] = None
            self.length -= 1
            return

        for i in range(node.length):
            if node[i].key == key:
                self.table[index].delete(i)
                break

        else:
            print("No item!")


hash_t = HashTable()
hash_t.insert("some", 23)
hash_t.insert("some2", 34)
hash_t.insert("some3", 45)
print("Look for 45:")
print(hash_t.lookup("45"))

print("Look for some:")
print(hash_t.lookup("some"))
print("Delete some:")
hash_t.delete("some")
print("Look for some:")
print(hash_t.lookup("some"))

