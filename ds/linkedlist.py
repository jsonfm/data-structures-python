class ListNode:
    def __init__(self, data, link):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self._head = None
    
    def addfirst(self, item):
        self._head = ListNode(item, self._head)
    