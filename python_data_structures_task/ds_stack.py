from _ds_scratch_ll_s_q import List


class Stack(List):

    def __init__(self):
        """constructor to initiate this object"""
        super().__init__()

    def push_item(self, item):
        """add item"""
        self._prepend_item(item)

    def peek_item(self):
        """search the stack for the last added node """
        res = self._lookup_by_index(0)
        if res is not None:
            return res.data
        return None

    def pop_item(self):
        """remove the last stack`s item"""
        self._delete_item(1)


if __name__ == '__main__':
    node1 = 15
    node2 = 8.2
    item3 = "Berlin"
    node4 = 118

    stack_1 = Stack()

    for current_item in [node1, node2, item3, node4]:
        stack_1.push_item(current_item)
        print(stack_1.peek_item())

    for current_item in [node1, node2, item3, node4]:
        print(stack_1.peek_item())
        stack_1.pop_item()
