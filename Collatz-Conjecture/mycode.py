class solution:
    def f(self, n):
        if n%2 == 1.0:
            n = int(3.0*n + 1)
        else:
            n = int(n/2.0)
        return n
    
    def maxline(self, n, hist):
        # input: a number,'n'
        #        a historic record hash table, 'hist'
        #              recording {integer: number of iterations to 1} 
        # Output: number of iterations to 1 , 'result'
        #         updated historic record has table, 'hist'
        if n < 1:
            return None
        if n == 1:
            hist[1] = 0
            return [0, hist]
        nInit = n
        num = 0
        nRec = [n]
        while(n != 1):
        # check if the integer is in the historic record
            # if so directly check out the number of iterations
            # to 1 and save it in 'num'
            # Otherwise,
            # calculate through Collatz function 'f'
            # 
            # nRec keeps all integers calculated through Collatz function 'f'
            # , excluding the integers that are looked up from historic records
            #
            if n in hist.keys():
                num = hist[n]
                break
            else:
                n = self.f(n)
                nRec.append(n)
        # write into historic dictionary 'hist'
        # for example:
        # integer is 10, n=10, hist is empty
        # nRec = [10, 5, 16, 8, 4, 2, 1]
        # We know that number of iteration to reach 1 from 1 is 0
        # hist[1] = 0
        # so,
        # number of iteration of 10 to reach 1, 
        # and updated historic record is:
        # [6, {1: 0, 2: 1, 4: 2, 5: 5, 8: 3, 10: 6, 16: 4}]
        if nRec[-1] == 1:
            hist[1] = 0
            num = hist[1]
        lenNRec = len(nRec)
        nRec = nRec[::-1]
        for ii in range(lenNRec):
            hist[nRec[ii]] = num + ii
        #print hist
        result = num+ii
        return [result, hist]
    def longest(self, nlist):
        # calculate maxline for a list of intergers and 
        # returns the integer that has the maximum 
        # number of iteration value to reach 1 through Collatz
        hist = {}
        numList = []
        if nlist == []:
            return None
        for item in nlist:
            [num, hist] = self.maxline(item, hist)
            print item, num
            numList.append(num)
        maxVal = max(numList)
        return numList.index(maxVal)
            
a=solution()
hist = {}
nlist = range(1,10)
b = a.longest(nlist)
print nlist[b]
