class Solution:
    def sumOfDivisors(self, N):

        s=0

        for i in range(1,N+1):

            s+=(N//i)*i

        return s
if __name__=='__main__':
    N= int(input("yess give input: "))
    a = Solution()
    c=a.sumOfDivisors(N)
    print(c)