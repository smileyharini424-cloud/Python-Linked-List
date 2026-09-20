# Python Linked List

## Explanation

A Linked List is a linear data structure where elements are stored in separate nodes.

Each node contains:

* Data
* A reference to the next node

This program implements a **Singly Linked List** in Python.

## Problem Statement

Write a Python program to implement a singly linked list.

The program should support:

* Insertion at the beginning
* Insertion at the end
* Deletion of an element
* Displaying the linked list

## Features

* Implements a singly linked list
* Uses nodes and references
* Supports insertion at the beginning
* Supports insertion at the end
* Supports deletion
* Displays all elements

## How It Works

1. A `Node` class stores data and the reference to the next node.
2. A `LinkedList` class manages the nodes.
3. `insert_beginning()` adds a node at the beginning.
4. `insert_end()` adds a node at the end.
5. `delete()` removes a node containing the specified value.
6. `display()` traverses and prints the list.

## Technologies Used

* Python 3

## Data Structure Used

* Singly Linked List
* Nodes

## Methods Used

* `__init__()`
* `insert_beginning()`
* `insert_end()`
* `delete()`
* `display()`

## Program Flow

1. Create an empty linked list.
2. Display the menu.
3. Select an operation.
4. Insert, delete, or display elements.
5. Continue until Exit is selected.

## Sample Input

```text id="nq4w4a"
1. Insert at Beginning
2. Insert at End
3. Delete
4. Display
5. Exit

Enter your choice: 2
Enter element: 10

Enter your choice: 2
Enter element: 20

Enter your choice: 1
Enter element: 5

Enter your choice: 4
```

## Sample Output

```text id="2x2y9h"
Linked List: 5 -> 10 -> 20 -> None
```

## Time Complexity

* Insert at Beginning: O(1)
* Insert at End: O(n)
* Delete: O(n)
* Display: O(n)

## Space Complexity

* O(n)

## Key Learning

* Understanding linked lists
* Understanding nodes
* Understanding references
* Implementing insertion
* Implementing deletion
* Traversing a linked list

## File Location

```text id="7h8jpr"
Python-Linked-List/linked_list.py
```

## Repository Structure

```text id="s0p3qn"
Python-Linked-List/
│
├── linked_list.py
└── README.md
```

## Author

V.Harini
