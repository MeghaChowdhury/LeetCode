class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        total = len(needle) 
        t2 = len(haystack) 
        k = 0 
        
        while t2 >= total: 
            for i in range(len(haystack)): 
                if haystack[i : total] == needle[:]: 
                    return k 
                else: 
                    k += 1 
                    total += 1 
        return -1
        