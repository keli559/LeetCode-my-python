class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        results = []
        if len(s) == 0 :
            return []
        #ipstack = list of (start, count, [what, what...](call it ipChuncks))
        # loop over ipstack elements
        ipstack = []
        ipstack.append((0,0,[]))
        while ipstack != []:
            start, count, ipChuncks = ipstack.pop(0)
            # at the end of the string
            strEnd = len(s)
            if (start == strEnd) and (count == 4): # the end of the string grouping
                results.append(ipChuncks)
                continue
            if count > 4: # if chuncks overflow to more than 4 
                continue
            # else would be not the end
            for upperBound in range(start + 1, strEnd + 1):
                if upperBound - start  > 3:
                    break
                aChunck = s[start: upperBound]
                if 0<=int(aChunck)<=255:
                    if not(len(aChunck)>1 and aChunck[0]=='0'): 
                        tempIpChuncks = ipChuncks[:]
                        tempIpChuncks.append(aChunck)
                        ipstack.append((start + len(aChunck), count+1, tempIpChuncks))
        # put the chosen results into format like xxx.xxx.xxx.xxx
        ipResults = []
        for ipIdress in results:
            ipResults.append('.'.join(ipIdress))
            
        return ipResults
