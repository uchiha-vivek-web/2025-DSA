class Solution :
    def ValidParantheses(self,character:str)  :
        st=[]
        for i in range(len(character)) :
            if character[i] =='(' or character[i] =='{' or character[i] =='[' :
                st.append(character[i])
            else :
                if st and (( st[-1] =='(' and character[i]==')') or
                           (st[-1] =='[' and character[i]==']') or
                           (st[-1] =='{' and character[i]=='}')) :
                    st.pop()
                else :
                    return False
        return not st
sol=Solution()
character = '[()]'
ans = sol.ValidParantheses(character)
print(ans)
                           
                             
                    