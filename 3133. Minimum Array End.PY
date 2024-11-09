class Solution(object):
    def minEnd(self, n, x):
        kMaxBit = n.bit_length() + x.bit_length()
        k = n - 1
        kBinaryIndex = 0

        for i in range(kMaxBit):
            if x >> i & 1 == 0:
                if k >> kBinaryIndex & 1:
                    x |= 1 << i
                kBinaryIndex += 1

        return x
