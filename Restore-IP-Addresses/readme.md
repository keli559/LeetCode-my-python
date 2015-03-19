# LeetCode-my-python
Here accumulates all my python code to solve LeetCode problems

## Restore-IP-Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter) 

## Algorithm

I got the algorithm idea from 
https://oj.leetcode.com/discuss/23853/bfs-search-for-valid-ip-in-python
(really good job by the way!!)
I rewrote my code according to my interpretation.
Besides, I wrote the following just to blog out my takehome message of this algorithm. 

1. develop a list (ipstack) that contains the pointer variable, or records of where the pointer is as both in a string and in the number chuncks:
start: where is the pointer right now
count: how many chuncks have already been grouped (ex. '255' is called a chunck)
ipChuncks: so far, what have been the chuncks (in list, ex [255, 255, 11])

2. Use stack.pop(0) to take out the first element, and expand from there for the rest of the string. 'ipstack' starts from [(0,0,[])], will expand to [(3, 2, ['0', '10']), (4, 2, ['0', '100'])], as the first record of the list keeps taken out, and the end of the list keeps appending new expanded chuncks resulting from the first takenout record in ipstack. How brilliant!

3. '.'.join(['255', '255', '11', '135']): what a brilliant way to add dots between chuncks to form IP!

4. [1, 2, 3].pop(0) => [2, 3]. It deletes the first element from the list; 

[1, 2, 3].pop(1) => [1, 2]. It deletes the last element from the list;
