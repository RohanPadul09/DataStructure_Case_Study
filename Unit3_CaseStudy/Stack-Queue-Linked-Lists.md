# Case Study: Implementation of Stack and Queue Operations Using Linked Lists

## 1. Introduction

A linked list is a linear data structure consisting of nodes. Each node contains two parts: data and a pointer to the next node.

Stack and Queue are linear data structures that can be implemented using linked lists. Unlike arrays, linked lists can grow and shrink dynamically during program execution.

- **Stack:** Follows LIFO (Last In, First Out).
- **Queue:** Follows FIFO (First In, First Out).

## 2. Problem Statement

To implement basic Stack and Queue operations using linked lists in Python, including insertion, deletion, and display operations, while handling empty data structures.

## 3. Objectives

- To understand linked list implementation.
- To implement Stack operations using a linked list.
- To implement Queue operations using a linked list.
- To handle underflow conditions when the structure is empty.
- To analyze the time and space complexity of operations.

## 4. Stack Using Linked List

A Stack follows the LIFO principle. The element inserted last is removed first. The `top` pointer indicates the first node of the linked list.

### Operations

1. **Push:** Inserts an element at the top of the Stack.
2. **Pop:** Removes the element from the top.
3. **Display:** Displays all elements from top to bottom.

### Algorithm: Push

1. Create a new node with the given data.
2. Set the new node's next pointer to the current top.
3. Update top to point to the new node.

### Algorithm: Pop

1. Check whether the Stack is empty.
2. If empty, display an appropriate message.
3. Otherwise, remove the top node by updating top to top.next.

## 5. Queue Using Linked List

A Queue follows the FIFO principle. The element inserted first is removed first. It uses two pointers: `front` and `rear`.

### Operations

1. **Enqueue:** Inserts an element at the rear.
2. **Dequeue:** Removes an element from the front.
3. **Display:** Displays elements from front to rear.

### Algorithm: Enqueue

1. Create a new node with the given data.
2. If the Queue is empty, set both front and rear to the new node.
3. Otherwise, link the current rear to the new node.
4. Update rear to the new node.

### Algorithm: Dequeue

1. Check whether the Queue is empty.
2. If empty, display an appropriate message.
3. Otherwise, remove the front node by updating front to front.next.
4. If the Queue becomes empty, set rear to None.

## 6. Python Implementation

The complete implementation is provided in the file `stack_queue_linked_list.py`. It defines a Node class, a Stack class, and a Queue class, with a main program to demonstrate the operations.

## 7. Sample Output

```text
--- STACK OPERATIONS ---
10 pushed into Stack
20 pushed into Stack
30 pushed into Stack
Stack (top to bottom): 30 20 10
Popped from Stack: 30
Stack (top to bottom): 20 10

--- QUEUE OPERATIONS ---
10 inserted into Queue
20 inserted into Queue
30 inserted into Queue
Queue (front to rear): 10 20 30
Removed from Queue: 10
Queue (front to rear): 20 30
```

## 8. Time and Space Complexity

| Operation | Time Complexity |
|---|---|
| Stack Push | O(1) |
| Stack Pop | O(1) |
| Stack Display | O(n) |
| Queue Enqueue | O(1) |
| Queue Dequeue | O(1) |
| Queue Display | O(n) |

**Space Complexity:** O(n), where n is the number of nodes stored in the linked list.

## 9. Applications

### Stack Applications
- Function calls and recursion.
- Undo and redo operations.
- Expression evaluation.
- Browser history navigation.

### Queue Applications
- CPU scheduling.
- Printer job scheduling.
- Customer service systems.
- Breadth-First Search (BFS).

## 10. Advantages

- Dynamic memory allocation.
- No fixed capacity like a basic array implementation.
- Efficient insertion and deletion at the required ends.
- Stack and Queue operations can be implemented without shifting elements.

## 11. Conclusion

This case study demonstrates the implementation of Stack and Queue operations using linked lists in Python. Stack follows the LIFO principle, while Queue follows the FIFO principle. Both structures support efficient insertion and deletion in O(1) time when implemented using appropriate pointers.
