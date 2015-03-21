# Two Sum

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2 

# Comment

Dictionary is built to store 
```
(target - num[ii]): ii

```
Note that (target - num[ii]) can be negative,
but "dict[num[ii]], ii" shows the indices. 

For example, for num = [2, 7, 11, 15]
The first element 2, the subtraction is 9 -2 = 7.
Since 2 isn't in the dictionary, save 7:0 to the dictionary.

When it iterates to element 7 (index = 1), 
dict[7] = 0, and current index 1 are stored as the location of 
2 and 7. Therefore, 

```
index1 = 1, index2 = 2
```  