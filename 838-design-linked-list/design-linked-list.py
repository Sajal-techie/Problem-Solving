class MyLinkedList:

    def __init__(self):
        self.linked_list = []

    def get(self, index: int) -> int:
        if index >= len(self.linked_list):
            return -1
        return self.linked_list[index]

    def addAtHead(self, val: int) -> None:
        self.linked_list = [val] + self.linked_list
        # print(self.linked_list)

    def addAtTail(self, val: int) -> None:
        self.linked_list.append(val)
        # print(self.linked_list)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <  len(self.linked_list):
            self.linked_list.insert(index, val)
        elif index  == len(self.linked_list):
            self.linked_list.append(val)
        # print(self.linked_list)

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.linked_list):
            self.linked_list.pop(index)
        # print(self.linked_list)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)