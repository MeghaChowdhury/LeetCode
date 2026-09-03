class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        k = 1
        store = ""
        truth = True
        if s == " ":
            return True
        for letter in s:
            if letter.isalnum():
                store += letter.lower()
        for i in range (len(store)-1):
            if  store[i] == store[len(store)-k]:
                k += 1
            else:
                return False
                break
        return truth
