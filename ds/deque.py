class ListDeque:
    def __init__(self, L = []):
        self._L = L
    
    def __str__(self):
        return str(self._L)

    def addfirst(self, item):
        self._L.insert(0, item)
    
    def addlast(self, item):
        self._L.append(item)
    
    def removefirst(self):
        return self._L.pop(0)
    
    def removelast(self):
        return self._L.pop()
    

if __name__ == "__main__":
    deque = ListDeque([1, 2, 3, 4])
    deque.addlast(100)
    deque.addfirst(0)
    print("deque: ", deque)
    deque.removefirst()
    print("deque: ", deque)
