""" Reverse  a number """

class Solution:
    def reverse_number(self,num):
        negative = num <0
        num = abs(num)
        reversed_num=0

        while num>0:
            reversed_num = reversed_num*10+ num%10
            num = num //10
        
        return -reversed_num if negative else reversed_num

    def direct_reverse_number(self,num:int):
        reverse_number = int(str(abs(num))[::-1])
        return -reverse_number if num < 0 else reverse_number

    
sol=Solution()
nums=123
nums1=234
ans=sol.reverse_number(nums)
ans1 = sol.direct_reverse_number(nums1)
print(ans1)