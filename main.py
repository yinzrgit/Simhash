# main.py
import os
import sys


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from simhash.simhash import Simhash

def main():
    #假设有文本1和文本2，对其使用split分词，然后计算simhash值，最后计算海明距离
    text1 = "This is a test sentence for simhash."
    text2 = "This is another test sentence for simhash."
    
    tokens1 = text1.split()
    tokens2 = text2.split()
    
    #
    simhash1 = Simhash(tokens1)
    simhash2 = Simhash(tokens2)
    
    
    print(f"文本1的simhash值为(二进制数): {bin(simhash1.hash)}")
    print(f"文本2的simhash值为(二进制数): {bin(simhash2.hash)}")
    print(f"两者simhash值的海明距离为: {simhash1.hamming_distance(simhash2)}")

if __name__ == "__main__":
    main()