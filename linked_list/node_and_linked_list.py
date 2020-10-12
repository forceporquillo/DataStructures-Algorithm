class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    # method to add next node
    def set_next_node(self, next_node):
        self.next = next_node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def traverse_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def get_child_node(self):
        node = self.head
        return node


arr_titles = [
    Node("Wherever You Will Go"),
    Node("Tonight"),
    Node("Fall For You"),
    Node("Lips Of Angel"),
    Node("My Sacrifice")
]

arr_artist = [
    "The Calling",
    "FM Static",
    "Secondhand Serenade",
    "Hinder",
    "Creed"
]

arr_node_instance = [Node()] * 5
