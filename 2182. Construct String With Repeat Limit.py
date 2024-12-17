class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        freq = [0] * 26
        for char in s:
            freq[ord(char) - 97] += 1
        
        result = []
        i = 25
        
        while i >= 0:
            if freq[i] == 0:
                i -= 1
                continue
            
            count = min(freq[i], repeatLimit)
            result.append(chr(i + 97) * count)
            freq[i] -= count
            
            if freq[i] > 0: 
                j = i - 1
                while j >= 0 and freq[j] == 0:
                    j -= 1
                
                if j < 0:  
                    break
                
                result.append(chr(j + 97))  
                freq[j] -= 1
            
            if freq[i] == 0:
                i -= 1

        return ''.join(result)
