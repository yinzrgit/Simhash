# simhash/simhash.py
import hashlib

class Simhash:
    def __init__(self, tokens):
        self.tokens = tokens
        self.hashbits = 64
        self.hash = self.simhash()

    def _hashfunc(self, x):
        return int(hashlib.md5(x.encode('utf-8')).hexdigest(), 16)
    
    #simhash算法
    def simhash(self):

        v = [0] * self.hashbits
        for t in [self._hashfunc(x) for x in self.tokens]:
            bitmask = 1
            for i in range(self.hashbits):
                if t & bitmask:
                    v[i] += 1
                else:
                    v[i] -= 1
                bitmask = bitmask << 1
        fingerprint = 0
        for i in range(self.hashbits):
            if v[i] >= 0:
                fingerprint += 1 << i
        return fingerprint
    
    # 海明距离计算
    def hamming_distance(self, other):
        x = (self.hash ^ other.hash) & ((1 << self.hashbits) - 1)
        tot = 0
        while x:
            tot += 1
            x &= x - 1
        return tot