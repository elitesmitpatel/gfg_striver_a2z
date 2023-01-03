class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        def hcf(A,B):
            if B==0:
                return(A)
            else:
                return hcf(B,A%B)
        def lcm(A,B):
            return(A*B)//hcf(A,B)
        return(lcm(A,B),hcf(A,B))
    
    
# import math
# if __name__ =='__main__':
#     t = int(input("the the num:"))
#     for _ in range(t):
#         A,B= map(int,input().split())
        
#         ob=Solution()
#         ptr = ob.lcmAndGcd(A,B)
a=Solution()
b=a.lcmAndGcd(16,5)
print(b)