class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        store = ""
        
        for letter in s:
            if letter.isalnum():
                store += letter.lower()
        left = 0
        right = len(store) - 1
        while left < right:    
            if  store[left] == store[right]:
                left += 1
                right -= 1
            else:
                return False
                
        return True
