from _ds_scratch_ll_s_q import List


class SingleLinkedList(List):

    def __init__(self):
        """constructor to initiate this object"""
        super().__init__()
        self.length = self._list_length()

    def __getitem__(self, index):
        """to get element by index"""
        if index < 0:
            index += self._list_length()

        loc_head = self.head
        for _ in range(index):
            loc_head = loc_head.next
        return loc_head.data

    def __setitem__(self, index, data):
        """to set element by index"""
        if index < 0:
            index = self.length + index

        loc_head = self.head
        for _ in range(index):
            loc_head = loc_head.next
        loc_head.data = data

    def __iter__(self):
        """simplest iterator"""
        node = self.head
        while node:
            yield node
            node = node.next

    def append_item(self, item):
        """add an item at the end of the list"""
        self._append_item(item)

    def prepend_item(self, item):
        self._prepend_item(item)

    def output_list(self):
        """outputs the linked list"""

        current_node = self.head

        while current_node is not None:
            print(current_node.data)

            # jump to the linked node
            current_node = current_node.next

    def lookup(self, data):
        """search the linked list for the node that has this value"""
        return self._lookup_by_val(data)

    def list_length(self):
        return self._list_length()

    def lookup_by_index(self, index):
        return self._lookup_by_index(index)

    def insert_item(self, data, index):
        self._insert_item(data, index)

    def delete_item(self, index):
        """remove the list item with the item id"""
        self._delete_item(index)

    def is_empty(self):
        """to know if ll is empty"""
        if self.list_length() == 0:
            return True
        return False


if __name__ == '__main__':
    node1 = 15
    node2 = 8.2
    item3 = "Berlin"
    node4 = 118

    track = SingleLinkedList()
    print(f"track length: {track.list_length()}")

    for current_item in [node1, node2, item3, node4]:
        track.append_item(current_item)
        track.prepend_item(str(current_item) + ' head')
        print("track length: %i" % track.list_length())
    track.output_list()

    print(track.lookup(118))
    print(track.lookup(119))
    track.delete_item(3)
    track.delete_item(1)
    track.insert_item(56, 3)
    track.output_list()
