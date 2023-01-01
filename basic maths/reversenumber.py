class Solution:
    def reversedBits(self, X):
        return int('0b'+format(X,'032b')[::-1],2)
    
    
    
if __name__=='__main__':
    t= int(input())
    for _ in range(t):
        x = int(input())
        ob = Solution()
        print(ob.reversedBits(x))