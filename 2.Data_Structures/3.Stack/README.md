# Stack

## Definition

A stack is a linear data structure that stores items in a **Last-In/First-Out** (**LIFO**) manner, with the restriction that inserts and deletes can be performed in only one position, namely the end of the list called the **top**.
The fundamental operations on a stack are **push**, which is equivalent to an insert, and **pop**, which deletes the most recently inserted element. The most recently inserted element can be examined prior to performing a pop by use of the **top** routine.

![stack](https://www.atnyla.com/library/images-tutorials/stack-data-structure-Slide1.PNG)

## Time complexity

Each stack operation is **O(1)**: Push, Pop, Top, Empty.

## Applications of stack:

* Stacks are used in the conversion of expression from infix notation to postfix and prefix notation.
* Stacks are used for evaluation of infix and postfix forms.
* Stacks are used in tree traversal techniques.
* Recursive functions are implemented using stacks. The copies of variables at each level of recursion are stored in stack.
* Compilers use stacks in syntax analysis phase to check whether a particular statement in a program is syntactically correct or not.
* Computers use stack during interrupts and function calls. The information regarding actual parameters return values, return addresses and machine status is stored in stack.
* Stacks are used in depth-first search of a graph.

## Visualization

1. [Stack using array](https://pythontutor.com/visualize.html#code=class%20ArrayStack%28object%29%3A%0A%20%20%20%20%22%22%22Stack%20implementation%20based%20on%20array%22%22%22%0A%0A%20%20%20%20def%20__init__%28self,%20size%3A%20int%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Initialize%20ArrayStack%20class%20object%20instance.%22%22%22%0A%20%20%20%20%20%20%20%20self._stack%20%3D%20%5B%5D%0A%20%20%20%20%20%20%20%20self._size%20%3D%20size%0A%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22ArrayStack%20class%20__str__%20method.%20Complexity%3A%20O%28n%29%22%22%22%0A%20%20%20%20%20%20%20%20stacks%20%3D%20%22%22%0A%0A%20%20%20%20%20%20%20%20for%20item%20in%20self._stack%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20stacks%20%2B%3D%20str%28item%29%0A%20%20%20%20%20%20%20%20%20%20%20%20stacks%20%2B%3D%20%22%5Cn%22%0A%0A%20%20%20%20%20%20%20%20stacks.strip%28%29%0A%20%20%20%20%20%20%20%20return%20%22Top-%3E%20%7Bstacks%7D%22.format%28stacks%3Dstacks%29%0A%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22ArrayStack%20class%20__repr__%20method.%22%22%22%0A%20%20%20%20%20%20%20%20return%20%22ArrayStack%28%7Bsize%7D%29%22.format%28size%3Dself._size%29%0A%0A%20%20%20%20def%20empty%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Return%20if%20the%20stack%20is%20empty.%20Complexity%3A%20O%281%29%22%22%22%0A%20%20%20%20%20%20%20%20return%20len%28self._stack%29%20%3D%3D%200%0A%0A%20%20%20%20def%20push%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Insert%20item%20at%20the%20top%20of%20the%20stack.%20Complexity%3A%20O%281%29%22%22%22%0A%20%20%20%20%20%20%20%20if%20len%28self._stack%29%20%3D%3D%20self._size%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20raise%20IndexError%28%22stack%20overflow%22%29%0A%0A%20%20%20%20%20%20%20%20self._stack.append%28value%29%0A%0A%20%20%20%20def%20pop%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Remove%20item%20at%20the%20top%20of%20the%20stack.%20Complexity%3A%20O%281%29%22%22%22%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20self._stack.pop%28%29%0A%20%20%20%20%20%20%20%20except%20IndexError%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20raise%20IndexError%28%22pop%20from%20empty%20stack%22%29%0A%0A%20%20%20%20def%20top%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Return%20last%20at%20the%20top%20of%20the%20stack.%20Complexity%3A%20O%281%29%22%22%22%0A%20%20%20%20%20%20%20%20if%20self.empty%28%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20raise%20IndexError%28%22top%20from%20empty%20stack%22%29%0A%0A%20%20%20%20%20%20%20%20return%20self._stack%5B-1%5D%0A%0A%0Astack%20%3D%20ArrayStack%283%29%0Astack.empty%28%29%0Astack.push%281%29%0Astack.top%28%29%0Astack.push%282%29%0Astack.push%283%29%0Atry%3A%0A%20%20%20%20stack.push%284%29%0Aexcept%20IndexError%3A%0A%20%20%20%20pass%0Astack.pop%28%29%0Astack.top%28%29%0Astack.empty%28%29%0A&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
2. [Stack using linked list](https://pythontutor.com/visualize.html#code=class%20Node%28object%29%3A%0A%20%20%20%20%22%22%22Node%20class%20implementation%20for%20linked%20list.%22%22%22%0A%0A%20%20%20%20def%20__init__%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Initialize%20Node%20class%20object%20instance.%22%22%22%0A%20%20%20%20%20%20%20%20self.value%20%3D%20value%0A%20%20%20%20%20%20%20%20self.next%20%3D%20None%0A%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Node%20class%20__str__%20method.%22%22%22%0A%20%20%20%20%20%20%20%20return%20str%28self.value%29%0A%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Node%20class%20__repr__%20method.%22%22%22%0A%20%20%20%20%20%20%20%20return%20%22Node%28%7Bvalue%7D%29%22.format%28value%3Dself.value%29%0A%0A%0Aclass%20LinkedListStack%28object%29%3A%0A%20%20%20%20%22%22%22Stack%20implementation%20based%20on%20linked%20list%22%22%22%0A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Initialize%20LinkedListStack%20class%20object%20instance.%22%22%22%0A%20%20%20%20%20%20%20%20self._top%20%3D%20None%0A%20%20%20%20%20%20%20%20self._iter%20%3D%20None%0A%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22LinkedListStack%20class%20__str__%20method.%20Complexity%3A%20O%28n%29%22%22%22%0A%20%20%20%20%20%20%20%20stacks%20%3D%20%22%22%0A%20%20%20%20%20%20%20%20node%20%3D%20self._top%0A%0A%20%20%20%20%20%20%20%20while%20node%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20stacks%20%2B%3D%20str%28node%29%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20node.next%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20stacks%20%2B%3D%20%22%5Cn%22%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%0A%20%20%20%20%20%20%20%20return%20%22Top-%3E%20%7Bstacks%7D%22.format%28stacks%3Dstacks%29%0A%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22LinkedListStack%20class%20__repr__%20method.%22%22%22%0A%20%20%20%20%20%20%20%20return%20%22LinkedListStack%28%29%22%0A%0A%20%20%20%20def%20empty%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Return%20if%20the%20stack%20is%20empty.%20Complexity%3A%20O%281%29%22%22%22%0A%20%20%20%20%20%20%20%20return%20not%20self._top%0A%0A%20%20%20%20def%20push%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Insert%20item%20at%20the%20top%20of%20the%20stack.%20Complexity%3A%20O%281%29%22%22%22%0A%20%20%20%20%20%20%20%20node%20%3D%20Node%28value%29%0A%20%20%20%20%20%20%20%20node.next%20%3D%20self._top%0A%20%20%20%20%20%20%20%20self._top%20%3D%20node%0A%0A%20%20%20%20def%20pop%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Remove%20item%20at%20the%20top%20of%20the%20stack.%20Complexity%3A%20O%281%29%22%22%22%0A%20%20%20%20%20%20%20%20if%20not%20self._top%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20raise%20IndexError%28%22pop%20from%20empty%20stack%22%29%0A%0A%20%20%20%20%20%20%20%20node%20%3D%20self._top.next%0A%20%20%20%20%20%20%20%20del%20self._top%0A%20%20%20%20%20%20%20%20self._top%20%3D%20node%0A%0A%20%20%20%20def%20top%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Return%20last%20at%20the%20top%20of%20the%20stack.%20Complexity%3A%20O%281%29%22%22%22%0A%20%20%20%20%20%20%20%20if%20not%20self._top%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20raise%20IndexError%28%22top%20from%20empty%20stack%22%29%0A%0A%20%20%20%20%20%20%20%20return%20self._top.value%0A%0A%0Astack%20%3D%20LinkedListStack%28%29%0Astack.empty%28%29%0Astack.push%281%29%0Astack.top%28%29%0Astack.push%282%29%0Astack.push%283%29%0Astack.pop%28%29%0Astack.top%28%29%0Astack.empty%28%29%0A&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## Implementation

### Python

1. [Stack using array](https://github.com/rszamszur/google-interview-preparation/blob/master/2.Data_Structures/3.Stack/Python/stack_array.py)
2. [Stack using linked list](https://github.com/rszamszur/google-interview-preparation/blob/master/2.Data_Structures/3.Stack/Python/stack_linked_list.py)

#### Tests

```shell
pytest ./Python
```

## Resources

- [stacks (video)](https://www.coursera.org/lecture/data-structures/stacks-UdKzQ)
- [Stack in Data Structure](https://www.atnyla.com/tutorial/stack-data-structure-introduction/3/315)