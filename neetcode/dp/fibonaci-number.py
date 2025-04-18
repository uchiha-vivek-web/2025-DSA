

class Fibonaci:
    def fibonacidp(self,n:int):
        """
        Time Complexity: O(N)
        Auxiliary Space: O(1)
        """
        f0=0
        f1 = 1
        if n<0:
            print('Error')
        elif n==0 :
            return 0
        elif n==1:
            return 1
        else :
            for i in range(2,n):
                c=f0+f1
                f0=f1
                f1=c
            return f1

    """ using dp and extra space"""
    def fibonaciwitharray(self,n:int):
        """
        Time complexity : O(N)
        Space complexity : O(N)
        """
        if n<=0:
            return 'incorrect output'
        data=[0,1]
        if n>2:
            for i in range(2,n):
                data.append(data[i-1]+data[i-2])
            return data[n-1]
    
    def fibonaccidfs(self,n:int):
        if n<=0 :
            return 'Error'
        else:
            def dfs(current:int):
                if current == 0 :
                    return 0
                elif current==1:
                    return 1
                else :
                    return dfs(current-1) + dfs(current-2)
            return dfs(n)




if __name__=="__main__":
    sol=Fibonaci()
    n:int=5
    ans=sol.fibonacidp(n)
    ans1=sol.fibonaciwitharray(n)
    ans2 = sol.fibonaccidfs(n)
    print(ans2)