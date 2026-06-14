class LRUCache:

    def __init__(self, capacity: int):
        print(f"init {capacity}")
        self.capacity = capacity
        self.hashMap = {}
        self.tail = None #Oldest
        self.head = None #Newest
        

    def get(self, key: int) -> int:
        print(f'Get {key}')
        print(self.hashMap.keys())
        if key in self.hashMap.keys():
            if self.head.key == key:
                # to get head node
                pass
            elif self.hashMap[key].prev == None:
                # to replace tail node
                print('replace tail')
                self.tail = self.hashMap[key].next
                self.tail.prev = None
                self.hashMap[key].prev = self.head
                self.head.next = self.hashMap[key]
                self.head = self.hashMap[key]
                self.head.next = None
            else:
                # for node in the middle
                print('replace mid')
                current_node = self.hashMap[key]
                current_node.next.prev = current_node.prev
                current_node.prev.next = current_node.next
                current_node.prev = self.head
                self.head.next = current_node
                self.head = self.hashMap[key]
                self.head.next = None
            print(self.tail)
            return self.hashMap[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        print(f'Put {key} {value}')
        print(self.hashMap)
        print(self.tail)
        if key not in self.hashMap:
            if len(self.hashMap) == 0:
                newNode = Node(key, value, None, None)
                self.tail = newNode
                self.head = newNode
                self.hashMap[key] = newNode
            elif len(self.hashMap) !=  self.capacity:
                newNode = Node(key, value, self.head, None)
                self.head.next = newNode
                self.head = newNode
                self.hashMap[key] = newNode
            else:
                del self.hashMap[self.tail.key]
                print(self.tail)
                self.tail = self.tail.next
                print(self.tail)
                if self.tail:
                    self.tail.prev = None
                newNode = Node(key, value, self.head, None)
                self.head.next = newNode
                self.head = newNode
                self.hashMap[key] = newNode
        else:
            if self.head.key == key:
                # to replace head node
                self.head.value = value
            elif self.hashMap[key].prev == None:
                # to replace tail node
                self.tail = self.hashMap[key].next
                self.tail.prev = None
                newNode = Node(key, value, self.head, None)
                self.head.next = newNode
                self.head = newNode
                self.hashMap[key] = newNode
            else:
                # for node in the middle
                current_node = self.hashMap[key]
                current_node.next.prev = current_node.prev
                current_node.prev.next = current_node.next
                newNode = Node(key, value, self.head, None)
                self.head.next = newNode
                self.head = newNode
                self.hashMap[key] = newNode
        print(self.hashMap)
        print(self.tail)


class Node:
    def __init__(self, key: int, value: int, prev, next):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return f"({self.key}, {self.value}) <-> {self.next}"