class Solution(object):
    def getKthCharacter(self, k, operations):
        n = len(operations)
        lengths = [1] * (n + 1)

        for i in range(n):
            lengths[i + 1] = lengths[i] * 2

        shift = 0
        for i in range(n - 1, -1, -1):
            half = lengths[i]
            if k > half:
                k -= half
                if operations[i] == 1:
                    shift += 1

        return chr((ord('a') - ord('a') + shift) % 26 + ord('a'))
