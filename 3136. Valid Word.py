class Solution(object):
    def isValid(self, word):
        if len(word) < 3:
            return False

        consonent = False
        vowel = False

        for ch in word:
            if ch.isdigit():
                continue

            elif ch.isalpha():
                if ch in {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}:
                    vowel = True
                else:
                    consonent = True
            
            else:
                return False
                
        return vowel and consonent
