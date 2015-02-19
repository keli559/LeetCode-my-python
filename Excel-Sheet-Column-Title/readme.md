## Coding Prompt

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
```
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
```
Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.

## Algorithm

1. figure out the last digit using ASCII code from the number: ex, number % 26 would give you the ASCII code of the letter;
2. calculate what is the rest aftering subtracting the last letter;
3. use nested function to figure out the rest; 

## Take Home Message:

1. ord(): symbol => integer
2. chr(): integer => symbol
3. list[::-1]: reverse the list
4. ''.join(): join list elements with '' symbol, ex: ''.join(['1', '2', '3']) gives '123'
