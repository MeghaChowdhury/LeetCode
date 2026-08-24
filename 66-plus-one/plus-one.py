class Solution(object):
    def plusOne(self, digits):
                
        num = int("".join(map(str,digits))) + 1

        digits = [int(x) for x in str(num)]

        return digits
        


        