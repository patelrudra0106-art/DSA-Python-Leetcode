class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        j = 0
        l = len(s)
        num_started = False
        
        
        for idx in range(l):
            ascii_val = ord(s[idx])
            
            
            if ascii_val == 32:
                if num_started:
                    break
                
                
                continue
            if ascii_val == 45 or ascii_val == 43:
                if not num_started:
                    num_started = True
                    i = idx
                else:
                    break
            elif 48 <= ascii_val and ascii_val <= 57:
                if not num_started:
                    num_started = True
                    i = idx
                
                
                j = idx + 1
            else:
                break
        
        
        if i >= j:
            return 0
        
        
        num = int(s[i : j])
        maxx = 2147483647
        minn = -2147483648
        
        
        if minn >= num:
            return minn
        elif maxx <= num:
            return maxx
        
        
        return num