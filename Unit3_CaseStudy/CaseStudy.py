
# Case Study: Implementation of Stack and Queue Operations
# Using Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack implementation using Linked List
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed into Stack")

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return

        print("Popped from Stack:", self.top.data)
        self.top = self.top.next

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        temp = self.top
        print("Stack (top to bottom):", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Queue implementation using Linked List
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into Queue")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return

        print("Removed from Queue:", self.front.data)
        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        print("Queue (front to rear):", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Main program
if __name__ == "__main__":
    stack = Stack()
    queue = Queue()

    print("\n--- STACK OPERATIONS ---")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    stack.pop()
    stack.display()

    print("\n--- QUEUE OPERATIONS ---")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()
    queue.dequeue()
    queue.display()
