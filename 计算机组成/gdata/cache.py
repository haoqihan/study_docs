from gdata.DoubleLinkList import DoubleLinkList, Node


class FIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.list = DoubleLinkList(self.capacity)

    def get(self, key):
        node = self.map.get(key, -1)
        if node != -1:
            return node.value
        return node

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.map:
            node = self.map.get(key)
            self.list.remove(node)
            node.value = value
            self.list.append(node)
        else:
            if self.size == self.capacity:
                node = self.list.pop()
                del self.map[node.key]
                self.size -= 1
            node = Node(key, value)
            self.list.append(node)
            self.map[key] = node
            self.size += 1

    def print(self):
        self.list.print()

if __name__ == '__main__':
    cache = FIFOCache(2)

    cache.put(1,1)
    cache.print()
    cache.put(2,2)
    cache.print()
    print(cache.get(1))
    cache.print()
    cache.put(3,3)
    cache.print()
    print(cache.get(3))
    cache.print()
    cache.put(4, 4)
    cache.print()
    print(cache.get(1))
