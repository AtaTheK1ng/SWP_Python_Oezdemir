import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def get_length(self):
        return self.length

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
            self.length -= 1
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next
            self.length -= 1


    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value


def main():
    linked_list = LinkedList()
    for _ in range(5):  # 5 Zufallszahlen hinzufügen
        linked_list.add(random.randint(1, 100))

    print("Liste nach dem Hinzufügen von Zufallszahlen:")
    linked_list.ausgeben()
    print(f"Länge der Liste: {linked_list.get_length()}")

    print("Iteriere über die Liste:")
    for value in linked_list:
        print(value, end=" -> ")
    print("None")

    linked_list.remove(linked_list.head.value)  # Erstes Element entfernen
    print("Liste nach dem Entfernen eines Elements:")
    linked_list.ausgeben()
    print(f"Länge der Liste: {linked_list.get_length()}")

if __name__ == "__main__":
    main()