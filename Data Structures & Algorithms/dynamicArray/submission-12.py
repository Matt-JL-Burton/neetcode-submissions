class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.array = [None] * capacity
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if self.array[i] == None:
            self.size = self.size + 1
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.array = self.array + [None] * self.capacity
            self.capacity = self.capacity * 2
        self.array[self.size] = n
        self.size = self.size + 1 

    def popback(self) -> int:
        temp = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size = self.size - 1 
        return temp

    def resize(self) -> None:
        self.array = self.array + ([] * self.capacity)
        self.capacity = self.capacity * 2
 
    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
