class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        
        cur_wlist  = []
        cur_ch_cnt = 0   # for the space consideration
     
        for w in words: 
            if cur_ch_cnt + len(cur_wlist) + len(w) > maxWidth:
                for i in range(maxWidth - cur_ch_cnt):  # insert space
                    cur_wlist[i%(len(cur_wlist) - 1 or 1)] += ' '
               
                res.append(''.join(cur_wlist)) # insert a this row 
                cur_wlist, cur_ch_cnt = [], 0 # prepare a new row, resetting
                
            cur_wlist += [w]
            cur_ch_cnt += len(w)
            
        return res + [' '.join(cur_wlist).ljust(maxWidth)]