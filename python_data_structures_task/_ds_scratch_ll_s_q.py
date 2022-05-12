"""
modulo to contain implementation of ll, queue, stack Node
contain List class, which realises
_append_item(data) -- add in the end
_prepend_item(data) -- add before head
_list_length() -- length
_lookup_by_val(data) -- search by val
_lookup_by_index(index) -- search by index
_insert_item(data, index) -- add by index
_delete_item(index) -- delete by index
-- basic methods to these structures
each method from this tests in module test_ll.py
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def has_value(self, value):
        """method to compare the value with the node data"""
        if self.data == value:
            return True
        return False


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def _append_item(self, item):
        """add an item at the end of the list"""

        new_node = Node(item)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node

    def _prepend_item(self, item):
        """add an item at the end of the list"""

        new_node = Node(item)
        if self.head is None:
            self._append_item(item)
        else:

            new_node.next = self.head
            self.head = new_node

    def _list_length(self):
        """returns the number of list items"""

        count = 0
        current_node = self.head
        while current_node is not None:
            # increase counter by one
            count = count + 1

            # jump to the linked node
            current_node = current_node.next

        return int(count)

    def _lookup_by_val(self, value):
        """search the linked list for the node that has this value"""

        # define current_node
        current_node = self.head

        # define position
        node_index = 1

        while current_node is not None:
            if current_node.has_value(value):
                return node_index

            # jump to the linked node
            current_node = current_node.next
            node_index += 1
        else:
            return False

    def _lookup_by_index(self, index):

        floating_index = 1
        current_node = self.head
        if self._list_length() >= index >= 0:

            while floating_index <= index:
                current_node = current_node.next
                floating_index += 1
            return current_node

    def _insert_item(self, data, index):
        new_node = Node(data)
        current_node = self.head
        floating_index = 1

        while floating_index < index - 1:
            floating_index += 1
            current_node = current_node.next

        temp_ref = current_node.next
        current_node.next = new_node
        new_node.next = temp_ref

    def _delete_item(self, index):
        """remove the list item with the item id"""
        current_index = 1
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_index == index:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    # we don't have to look any further
                    return

            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
            current_index = current_index + 1


# node1 = 15
# node2 = 8.2
# item3 = "Berlin"
# node4 = 118
#
# track = List()
# print("track length: %i" % track._list_length())
#
# for current_item in [node1, node2, item3, node4]:
#     track._append_item(current_item)
#     track._prepend_item(str(current_item) + ' head')
#
# print(track._lookup_by_index(2).data)
#     print("track length: %i" % track.list_length())

# #
# # print(track.lookup(118))
# # print(track.lookup(119))
# # track.delete_item(3)
# # track.delete_item(1)
# track.insert_item(56, 3)
# track.output_list()
