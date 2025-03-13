class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def ausgeben(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def remove(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next


def main():
    linkedList = LinkedList()
    linkedList.add(1)
    linkedList.add(2)
    linkedList.add(3)
    linkedList.ausgeben()
    linkedList.remove(2)
    linkedList.ausgeben()

if __name__ == "__main__":
    main()