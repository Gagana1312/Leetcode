class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        ch = chars[0]  
        s = "" 
        count = 0  
        
        for c in chars:
            if c == ch:
                count += 1  
            else:
                s += ch  
                if count > 1:
                    s += str(count)  
                ch = c  
                count = 1  
        
        
        s += ch
        if count > 1:
            s += str(count)
        
        
        chars[:len(s)] = list(s)
        return len(s)
            


        

        