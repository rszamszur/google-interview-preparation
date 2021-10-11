# Linked Lists

## Definition

A linked list is a linear data structure consisting of a group of nodes where each node points to the next node by means of a pointer.
Each node is composed of data and a reference to the next node in the sequence. The last node has a reference to null which indicates the end of the linked list.
Head node is the starting node of the linked list, and it contains the reference to the next node in the list. The head node will have a null reference when the list is empty.

![linked list](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/2560px-Singly-linked-list.svg.png)

## Time complexity

| Singly Linked List | no tail | with tail |
|-------------------:|:-------:|:---------:|
|    PushFront(data) |   O(1)  |           |
|         TopFront() |   O(1)  |           |
|         PopFront() |   O(1)  |           |
|     PushBack(data) |   O(n)  |    O(1)   |
|          TopBack() |   O(n)  |    O(1)   |
|          PopBack() |   O(n)  |           |
|        Find(value) |   O(n)  |           |
|       Erase(value) |   O(n)  |           |
|            Empty() |   O(1)  |           |

## Types

### Singly Linked List
![singly](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/2560px-Singly-linked-list.svg.png)

### Doubly Linked List
![Doubly](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/2560px-Doubly-linked-list.svg.png)

### Circular Linked List
![circular](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Circularly-linked-list.svg/2560px-Circularly-linked-list.svg.png)

## Visualisation

1. [Singly Linked List](https://pythontutor.com/visualize.html#code=class%20Node%28object%29%3A%0A%20%20%20%20%0A%20%20%20%20def%20__init__%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20self.value%20%3D%20value%0A%20%20%20%20%20%20%20%20self.next%20%3D%20None%0A%20%20%20%20%20%20%0A%0Aclass%20SinglyLinkedList%28object%29%3A%0A%20%20%20%20%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20self.head%20%3D%20None%0A%0A%20%20%20%20def%20push_front%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20node%20%3D%20Node%28value%29%0A%20%20%20%20%20%20%20%20node.next%20%3D%20self.head%0A%20%20%20%20%20%20%20%20self.head%20%3D%20node%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20top_front%28self%29%3A%0A%20%20%20%20%20%20%20%20if%20self.head%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20self.head.value%0A%20%20%20%20%0A%20%20%20%20def%20pop_front%28self%29%3A%0A%20%20%20%20%20%20%20%20if%20self.head%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20self.head.next%0A%20%20%20%20%20%20%20%20%20%20%20%20del%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20node%0A%0A%20%20%20%20def%20push_back%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20if%20self.head%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20while%20node.next%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%20%20%20%20%20%20%20%20%20%20%20%20node.next%20%3D%20Node%28value%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20Node%28value%29%0A%20%20%20%20%0A%20%20%20%20def%20top_back%28self%29%3A%0A%20%20%20%20%20%20%20%20if%20self.head%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20while%20node.next%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20node.value%0A%0A%20%20%20%20def%20pop_back%28self%29%3A%0A%20%20%20%20%20%20%20%20if%20self.head%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20not%20self.head.next%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20del%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20None%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20while%20node.next.next%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20del%20node.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20node.next%20%3D%20None%0A%0A%20%20%20%20def%20find%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20node%20%3D%20self.head%0A%20%20%20%20%20%20%20%20while%20node%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20node.value%20%3D%3D%20value%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%0A%20%20%20%20def%20erase%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20node%20%3D%20self.head%0A%20%20%20%20%20%20%20%20prev%20%3D%20None%0A%20%20%20%20%20%20%20%20while%20node%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20node.value%20%3D%3D%20value%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20prev%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20prev.next%20%3D%20node.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20node.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20del%20node%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20break%0A%20%20%20%20%20%20%20%20%20%20%20%20prev%20%3D%20node%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%0A%20%20%20%20def%20length%28self%29%3A%0A%20%20%20%20%20%20%20%20node%20%3D%20self.head%0A%20%20%20%20%20%20%20%20count%20%3D%200%0A%20%20%20%20%20%20%20%20while%20node%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20count%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%20%20%20%20%20%20%20%20return%20count%0A%0A%20%20%20%20def%20empty%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20not%20self.head%0A%0A%23%20Comment%20and%20experiment%20with%20available%20operations%0Aobj%20%3D%20SinglyLinkedList%28%29%0Aobj.push_front%281%29%0Aobj.push_front%282%29%0Aobj.push_front%283%29%0Aobj.length%28%29%0Aobj.find%282%29%0Aobj.pop_front%28%29%0Aobj.pop_front%28%29%0Aobj.push_back%282%29%0Aobj.push_back%283%29%0Aobj.pop_back%28%29%0Aobj.pop_back%28%29%0A&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
2. [Doubly Linked List](https://pythontutor.com/visualize.html#code=class%20Node%28object%29%3A%0A%0A%20%20%20%20def%20__init__%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20self.value%20%3D%20value%0A%20%20%20%20%20%20%20%20self.prev%20%3D%20None%0A%20%20%20%20%20%20%20%20self.next%20%3D%20None%0A%0A%0Aclass%20DoublyLinkedList%28object%29%3A%0A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20self.head%20%3D%20None%0A%0A%20%20%20%20def%20push_front%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20node%20%3D%20Node%28value%29%0A%20%20%20%20%20%20%20%20if%20self.head%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20node.next%20%3D%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20self.head.prev%20%3D%20node%0A%20%20%20%20%20%20%20%20self.head%20%3D%20node%0A%0A%20%20%20%20def%20top_front%28self%29%3A%0A%20%20%20%20%20%20%20%20if%20self.head%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20self.head.value%0A%0A%20%20%20%20def%20pop_front%28self%29%3A%0A%20%20%20%20%20%20%20%20if%20self.head%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20self.head.next%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20node%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20node.prev%20%3D%20None%0A%20%20%20%20%20%20%20%20%20%20%20%20del%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20node%0A%0A%20%20%20%20def%20push_back%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20if%20self.head%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20while%20node.next%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%20%20%20%20%20%20%20%20%20%20%20%20node.next%20%3D%20Node%28value%29%0A%20%20%20%20%20%20%20%20%20%20%20%20node.next.prev%20%3D%20node%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20Node%28value%29%0A%0A%20%20%20%20def%20top_back%28self%29%3A%0A%20%20%20%20%20%20%20%20if%20self.head%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20while%20node.next%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20node.value%0A%0A%20%20%20%20def%20pop_back%28self%29%3A%0A%20%20%20%20%20%20%20%20if%20self.head%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20not%20self.head.next%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20del%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20None%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20while%20node.next.next%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20del%20node.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20node.next%20%3D%20None%0A%0A%20%20%20%20def%20find%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20node%20%3D%20self.head%0A%20%20%20%20%20%20%20%20while%20node%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20node.value%20%3D%3D%20value%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%0A%20%20%20%20%20%20%20%20return%20False%0A%0A%20%20%20%20def%20erase%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20node%20%3D%20self.head%0A%20%20%20%20%20%20%20%20while%20node%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20node.value%20%3D%3D%20value%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20node.prev%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20node.prev.next%20%3D%20None%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20node.next%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20node.prev.next%20%3D%20node.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20node.next.prev%20%3D%20node.prev%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20None%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20node.next%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20node.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.head.prev%20%3D%20None%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20del%20node%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20break%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%0A%20%20%20%20def%20length%28self%29%3A%0A%20%20%20%20%20%20%20%20node%20%3D%20self.head%0A%20%20%20%20%20%20%20%20count%20%3D%200%0A%20%20%20%20%20%20%20%20while%20node%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20count%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%20%20%20%20%20%20%20%20return%20count%0A%0A%20%20%20%20def%20empty%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20not%20self.head%0A%0Aobj%20%3D%20DoublyLinkedList%28%29%0Aobj.push_front%281%29%0Aobj.push_front%282%29%0Aobj.push_front%283%29%0Aobj.length%28%29%0Aobj.find%282%29%0Aobj.pop_front%28%29%0Aobj.pop_front%28%29%0Aobj.push_back%282%29%0Aobj.push_back%283%29%0Aobj.pop_back%28%29%0Aobj.pop_back%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## Implementation

### Python

1. [Singly Linked List](https://github.com/rszamszur/google-interview-preparation/blob/master/2.Data_Structures/2.Linked_Lists/Python/singly.py)
2. [Doubly Linked List](https://github.com/rszamszur/google-interview-preparation/blob/master/2.Data_Structures/2.Linked_Lists/Python/doubly.py)

#### Tests

```shell
pytest ./Python/
```

## Resources

- [Singly-Linked Lists (video)](https://www.coursera.org/lecture/data-structures/singly-linked-lists-kHhgK)
- [Linked list introduction](https://www.atnyla.com/tutorial/linked-list-introduction/3/307)
- [Linked List | Representation and Types of Linked List](https://dev.faceprep.in/data-structures/linked-list-introduction/)
- [Singly Linked Lists](https://www.atnyla.com/tutorial/singly-linked-list/3/309)
- [Doubly Linked Lists](https://www.atnyla.com/tutorial/doubly-linked-list/3/310)
- [In the Real World: Lists vs. Arrays (video)](https://www.coursera.org/lecture/data-structures-optimizing-performance/in-the-real-world-lists-vs-arrays-QUaUd)
- [Why you should avoid Linked Lists (video)](https://youtu.be/YQs6IC-vgmo)