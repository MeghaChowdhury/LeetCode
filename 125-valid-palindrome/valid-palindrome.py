class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        k = 1
        store = ""
        if s == " ":
            return True
        else:
            for letter in s:
                if letter.isalnum():
                    store += letter.lower()
        for i in range (len(store)-1):
            if  store[i] == store[len(store)-k]:
                k += 1
            else:
                return False
        return True
