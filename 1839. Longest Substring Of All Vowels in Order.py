class Solution(object):
    def longestBeautifulSubstring(self, word):
        vowels = ['a', 'e', 'i', 'o', 'u']

        maxCount = 0
        curr = 0
        index = 0
        prev = ''

        for char in word:
            if char == vowels[index]:
                curr += 1

                if char == 'u':
                    prev = ''
                    maxCount = max(maxCount, curr)
                    continue

                prev = vowels[index]
                index += 1

            elif char == prev:
                curr += 1

            elif char == 'a':
                curr = 1
                index = 1
                prev = 'a'

            else:
                curr = 0
                index = 0
                prev = ''
                
        return maxCount
