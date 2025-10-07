class Solution(object):
    def findTheDifference(self, s, t):
        hashMap = [0] * 26

        for i in s:
            hashMap[ord(i) - 97] += 1
        
        for i in t:
            if hashMap[ord(i) - 97] <= 0:
                return i
            hashMap[ord(i) - 97] -= 1
