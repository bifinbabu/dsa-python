class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
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

        itr.next = Node(data, None, itr)

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

    # Insert at specific index
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    # Get last node in the doubly linked list
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    # Print list forward
    def print_forward(self):
        if self.head is None:
            print("List is empty")
            return

        llstr = ""
        itr = self.head
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    # Print list backward
    def print_backward(self):
        if self.head is None:
            print("List is empty")

        llstr = ""
        last_node = self.get_last_node()
        itr = last_node

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.prev
        print("Linked list in reverse", llstr)


if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0, "jackfruit")
    ll.print_forward()
    ll.insert_at(6, "dates")
    ll.print_forward()
    ll.insert_at(2, "kiwi")
    ll.print_forward()
