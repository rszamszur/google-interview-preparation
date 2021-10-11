# Arrays

## Definition

An array is a contiguous area of memory consisting of equal-size elements indexed by contiguous integers. In more plain words, it's a data structure that can store a fixed-size sequential collection of elements of the same type.

![array](https://github.com/rszamszur/google-interview-preparation/blob/master/assets/images/array.png?raw=true)

The key point about an array is constant time access to any particular element in an array. But how? Answer: simple arithmetics:

$first\_address + element\_size * (index - first\_index)$

NOTE! If array implementation is using $0$ based indexing $first\_index$ is irrelevant.

## Example

![array2](https://github.com/rszamszur/google-interview-preparation/blob/master/assets/images/array2.jpeg?raw=true)

If above array is storing 32bits integers, and its first addres is 200. Then address of element at index 3 would be:

$200 + ((32/8) * 3) = 212$

## Time complexity of common operations

|        | Access | Insertion | Deletion |
|--------|:------:|:---------:|:--------:|
|  Start |  O(1)  |    O(n)   |   O(n)   |
|    End |  O(1)  |    O(1)   |   O(1)   |
| Middle |  O(1)  |    O(n)   |   O(n)   |

## Space complexity

An array is fixed-size, therefore space complexity is $O(n)$ regardles whether all values are used.

## Multi-Dimensional arrays

![row-major](https://github.com/rszamszur/google-interview-preparation/blob/master/assets/images/row-major-order.png?raw=true)
![column-major](https://github.com/rszamszur/google-interview-preparation/blob/master/assets/images/column-major-order.png?raw=true)

## Resources

- [Arrays](https://www.coursera.org/lecture/data-structures/arrays-OsBSF)
- [Visualization](https://www.cs.usfca.edu/~galles/visualization/StackArray.html)
- [Multi-Dimensional](https://www.atnyla.com/tutorial/two-dimension-array-in-data-structure/3/301)
- [Dynamic arrays](https://www.coursera.org/lecture/data-structures/dynamic-arrays-EwbnV)
- [Jagged Arrays](https://youtu.be/1jtrQqYpt7g)
- [Data Structures: Arrays vs Linked Lists](https://youtu.be/lC-yYCOnN8Q)
