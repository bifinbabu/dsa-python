class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, head):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    # Insert at end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr = Node(data, None, itr)

    # Insert a list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    # Get list length
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    # Remove at specific index
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            if self.head:  # Check if the new head is not None
                self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:  # If not removing the last node
                    itr.next.prev = itr.prev
                else:  # If removing the last node
                    itr.prev.next = None  # Update the previous node's next to None
                break

            itr = itr.next
            count += 1
