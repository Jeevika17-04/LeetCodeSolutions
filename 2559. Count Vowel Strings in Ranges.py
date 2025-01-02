class Solution(object):
    def vowelStrings(self, words, queries):
        n = len(words)
        prefix_sum = [0] * n
        result = []
        s = {'a', 'e', 'i', 'o', 'u'}

        prefix_sum[0] = 1 if words[0][0] in s and words[0][-1] in s else 0
        for i in range(1, n):
            if words[i][0] in s and words[i][-1] in s:
                prefix_sum[i] += 1
            prefix_sum[i] += prefix_sum[i - 1]
        
        for i, j in queries:
            if i == 0:
                result.append(prefix_sum[j])
                continue
            result.append(prefix_sum[j] - prefix_sum[i - 1])
        
        return result
