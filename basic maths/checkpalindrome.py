
class Solution:
	def is_palindrome(self, n):
		n= str(n)
		if n == n[::-1]:
		    return "Yes"
		else:
		    return "No"
if __name__=='__main__':
    t= int(input("number you eant to write"))
    for i in range(t):
        n = int(input())
        ob = Solution()
        ans=ob.is_palindrome(n)
        print(ans)