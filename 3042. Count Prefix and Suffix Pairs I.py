class Solution(object):
    def countPrefixSuffixPairs(self, words):
        def isPrefixAndSufix(str1, str2):
            n = len(str1)
            return str2[:n] == str1 and str1 == str2[-n:] 

        count = 0
        length = len(words)
        for i in range(length):
            for j in range(i + 1, length):
                if isPrefixAndSufix(words[i], words[j]):
                    count += 1
        return count
