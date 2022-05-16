from _ds_scratch_ll_s_q import List


class Queue(List):

    def __init__(self):
        """constructor to initiate this object"""
        super().__init__()

    def enqueue_item(self, item):
        """add item"""
        self._prepend_item(item)

    def peek_item(self):
        """search the queue for the first added node"""
        res = self._lookup_by_index(self._list_length()-1)
        if res is not None:
            return res.data
        return None

    def dequeue_item(self):
        """remove the first queue item"""
        self._delete_item(self._list_length())


if __name__ == '__main__':
    node1 = 15
    node2 = 8.2
    node3 = "Berlin"
    node4 = 118

    track = Queue()

    for current_item in [node1, node2, node3, node4]:
        track.enqueue_item(current_item)
        print(track._list_length())
        print(track.peek_item())
    print('\ndeq&peek\n')
    for current_item in [node1, node2, node3, node4]:
        track.dequeue_item()
        print(track.peek_item())
