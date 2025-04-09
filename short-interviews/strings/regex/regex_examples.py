""" Regex example  """
import re

class Solution :
    """ 5 letter word starting with a ad endong with s """
    def stoa(self,test_string:str) -> bool :
        pattern =  '^a...s$'
        result = re.match(pattern,test_string)
        if result :
            print('Search successful')
        else :
            print('Search unsuccessful')

    """ For range of characters  """

    def range1(self,pattern1:str):
        """ Here [a-e] means [a,b,c,d,e]  
            Here [1-5] means [1,2,3,4,5]
        """
        pattern = '[a-e]'
        result = re.match(pattern,pattern1)
        if result :
            print('Pattern1 matched')
        else :
            print('No patter matched')
    
    """ Invert character ^ means compliment of that set"""
    def invertstring(self,string1:str):
        pattern = '[^abc]'
        result = re.match(pattern,string1)
        if result:
            print('Patter matched')
        else :
            print('Pattern did not matched')
    

    """ check for any non digit character """
    def NonDigitCharacter(self,num1:str):
        pattern='[^1-9]'
        result=re.match(pattern,num1)
        if result :
            print('Pattern matched')
        else :
            print('pattern did not matched ')


        
sol=Solution()
test_string="aqwes"
pattern1 = 'bcd'
string1 ="a"
nums1 = "123345a"
# sol.stoa(test_string)
# sol.range1(pattern1)
# sol.invertstring(string1)
sol.NonDigitCharacter(nums1)