class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        # Function takes in a list of numbers, 'num'
        # and the sum value 'target'
        # Function returns the two indices in list 'num'
         # Index1 and Index2
         if num == []:
             return (-1, -1)
         dict = {}
         # dictionary /hash table is structured
         #  subtraction(can be negative):current index
         # target - num[ii]: ii
         #
         # Although there are negatives for (target -num[ii])
         # but pick only when the current num[ii] is in the dictionary.keys()
         # Therefore, the negative keys are automatically filtered! Excellent!
        m = len(num)
        for ii in range(m):
            if num[ii] in dict.keys():
                
                return (dict[num[ii]]+1, ii+1)
            else:
                tmp = target-num[ii]
                dict[tmp] = ii

num = [2, 7, 11, 13]
target = 9
print 'The list looks like:'
print num
print '\n'
print 'Target sum is:'
print target
print '\n'
print 'Index1 and Index2 are:'
print Solution().twoSum(num, target)
