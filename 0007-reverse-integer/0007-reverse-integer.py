class Solution(object):
    def reverse(self, x):

        s = str(x)
        if s[0] == '-':
            rev = '-' + s[:0:-1]
        else:
            rev = s[::-1]
        
        num = int(rev)
        
        if -2**31 <= num <= 2**31 - 1:
            return num
        return 0
        