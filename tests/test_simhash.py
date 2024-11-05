# tests/test_simhash.py
import unittest
from simhash import Simhash

class TestSimhash(unittest.TestCase):
    def test_simhash(self):
        s1 = Simhash(['this', 'is', 'a', 'test'])
        s2 = Simhash(['this', 'is', 'a', 'test'])
        s3 = Simhash(['this', 'is', 'another', 'test'])
        
        self.assertEqual(s1.hash, s2.hash)
        self.assertNotEqual(s1.hash, s3.hash)

        #如果两个simhash值相差在10以内，说明两个文本相似
        self.assertLess(s1.hamming_distance(s3), 10)

if __name__ == '__main__':
    unittest.main()