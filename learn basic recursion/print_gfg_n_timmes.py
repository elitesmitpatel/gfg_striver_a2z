class Solution:
    def printGfg(self, n):
        # Code here
        if n > 1:
            self.printGfg(n-1)
        print("GFG", end = " ")
        
a=Solution()
a.printGfg(5)