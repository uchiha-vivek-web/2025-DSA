# https://leetcode.com/problems/make-the-string-great/submissions/1652253969/



class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1]!=ch and stack[-1].lower()==ch.lower():
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
        

# lot of follow ups can be made 