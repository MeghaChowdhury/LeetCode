class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = str(n)
        
        check = set()
        total = 0

        while total not in check:
            check.add(total)
            total = 0
            for i in num:
                total += int(i)**2
            if total == 1:
                return True
            else:    
                num = str(total)
              
        return False


        