import math
class Solution(object):
    def pickGifts(self, gifts, k):
        index = 0
        n = len(gifts)
        gifts.sort(reverse = True)
        while k > 0:
            if n == index or gifts[index] < gifts[0]:
                gifts.sort(reverse = True)
                index = 0
            else:
                gifts[index] = int(math.sqrt(gifts[index]))
                index += 1
                k -= 1
        return sum(gifts)
