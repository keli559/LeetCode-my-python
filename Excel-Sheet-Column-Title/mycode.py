class Solution:
    # @return a string
    def convertToTitle(self, num):
        # 1. find out the ASCII code for the first letter 'A', 
        # any other letters can be calculated
        startA = ord('A')
        # 2. number cannot below or equal to zero
        if num <= 0:
            return ''
        # 3. 
        If number is just one digit
        if 1<=num<=26:
            return chr(startA + num -1)
        # otherwise, set up a list of letters in the reverse order ex. ['A', 'B', 'C'] for 'CBA'
        list = []
        # 3.1 focuse on current letter to list
        # if num is multiple of 26, the target digit should be 'Z', 
        # ex. 52 = 1 x 26 + 26 -> 'ZZ'
        # otherwise it is a calculated letter according to ASCII code
        # ex. 51 = 1 x 26 + 25 -> 'ZY'
        if num%26 == 0:
            list.append('Z')
        else:
            lastLetter = chr(startA + int(num)%26 -1)
            list.append(lastLetter)
        # 3.2 focuse on the next letter/letters
        # if number doesn't have multiple of  26 any more, skip this step
        # otherwise, iterate the number value to the "leftover" number 
        # after dealing withcurrent letter, 
        # ex, 51, after recognizing ['Y'], now the "leftover" number is 51-25 = 26
        # use 26 as the new number, and use nested function to figure out the rest of the letters
        if int(num)/26 != 0:
            if int(num)%26 == 0:
                num = int(num)/26 -1
            else:
                num = int(num)/26
            list.append(Solution().convertToTitle(num))
          # 4. reverse the list, ex: ['A', 'B', 'C'] -> ['C', 'B', 'A'] 
          # and join them together ex:['C', 'B', 'A'] -> 'CBA'
          # return answer
          list = list[::-1]
          return ''.join(list)
