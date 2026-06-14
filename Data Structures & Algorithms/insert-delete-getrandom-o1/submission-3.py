class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.list = []

    def insert(self, val: int) -> bool:
        print(self.hashMap, self.list, 'insert')
        if val not in self.hashMap:
            self.hashMap[val] = len(self.list)
            self.list.append(val)
            return True
        else:
            return False
        
    def remove(self, val: int) -> bool:
        print(self.hashMap, self.list, val, 'delete')
        if val in self.hashMap:
            deleted_item_index = self.hashMap[val]
            self.list[deleted_item_index] = self.list[-1]
            self.hashMap[self.list[-1]] = deleted_item_index
            self.list.pop()
            self.hashMap.pop(val)
            return True
        else:
            return False


    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()