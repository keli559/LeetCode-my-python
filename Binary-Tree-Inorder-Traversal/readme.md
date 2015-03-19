# Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
```
   1
    \
     2
    /
   3
```
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

## Comment
### 1. When the node hasn't checked its child(ren) yet, mark False;
if the node and its children checked and expanded,  mark the node True


step 1: [1] False
step 2: (1, True), (2, False)
step 3: (1, True), (3, True), (2, True)
step 4: (1, True), (3, True),  <==> [2]
step 5: (1, True),  <==> [2, 3]
step 6: ==> [2, 3, 1]

reverse: 1, 3, 2

When All True, 

return [1, 3, 2]
### 2. The algorithm uses stack.pop() to take stack records from its tail, 
and expanded from its tail until there is a 'True' node shows up. once the
'True' node shows up, it is taken out of the stack and append it to an accumulating list 'acc'. 

## Takehome Message

In a tree, stick with one end of the list would maintain its order. 


