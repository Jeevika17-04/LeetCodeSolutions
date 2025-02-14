class ProductOfNumbers(object):

    def __init__(self):
        self.a = [1]

    def add(self, num):
        if num == 0:
            self.a = [1]
        else:
            self.a.append(self.a[-1] * num) 

    def getProduct(self, k):
        if k >= len(self.a):
            return 0

        return self.a[-1] // self.a[-k - 1]
