class Solution:
    def minJumps(self, arr, n):
        #code here
        if n == 1: return 0
        if arr[0] == 0: return -1
        
        end, maxreach, jumps = 0, 0, 0
        
        for idx, val in enumerate(arr[:-1]):
            maxreach = max(maxreach, idx + val)
            
            if idx == end:
                jumps += 1
                end = maxreach
                
        return jumps if end >= n - 1 else -1


a=Solution()
b=a.minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9],11)
print(b)