class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        n = len(v1)
        m = len(v2)
        i = j = 0

        while i < n and j < m:
            if v1[i] < v2[j]:
                return -1
            elif v1[i] > v2[j]:
                return 1
            else:
                i += 1
                j += 1
        
        while i < n:
            if v1[i] > 0:
                return 1
            else:
                i += 1

        while j < m:
            if v2[j] > 0:
                return -1
            else:
                j += 1

        return 0
    
