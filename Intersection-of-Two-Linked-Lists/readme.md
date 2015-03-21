# Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

```
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
```

begin to intersect at node c1.

Notes:

    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.

Credits:
Special thanks to @stellari for adding this problem and creating all test cases.

## Comment

1. Both pointers a-> and b-> start at a1 and b1. 
Due to the length difference between A and B, 
a would reach end first.
Turn a to link Node B, and iterate until b reaches end of B
Turn b to link Node A. Now the a-> and b-> should be pointing at same pace. 

2. iterate as a-> and b-> are traversing, The first one the both a-> and b-> are recorded. 
