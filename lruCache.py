class LRUCache:

    def __init__(self, capacity: int):
        self._table = collections.OrderedDict()
        self._capacity = capacity

    def get(self, key: int) -> int:
        if key not in self._table:
            return -1
        v = self._table.pop(key)
        self._table[key] = v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self._table:
            v = self._table.pop(key)
        elif self._capacity <= len(self._table):
            self._table.popitem(last=False)
        self._table[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
