# Collatz Conjecture

The collatz function is described as:

n = 3n + 1, n%2 == 1; or
n = n/2,      n%2 = 0

## Question:

 For a list of integers, calculate the number that has the longest iteration with Collatz until it reaches to 1.

For example: 

1 has 0
2 has 1
3 has 7
4 has 2
5 has 5
6 has 8
7 has 16
8 has 3
9 has 19

## Comment:
Here is the catch:
10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1, 
however, when calculating 5, for example, 
the code doesn't have to recalculate 
5 -> 16 -> 8 -> 4 -> 2 -> 1 again
as it was calculated before. 



