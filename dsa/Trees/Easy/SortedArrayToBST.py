class Node :
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right


class Solution :
    def ArrayToBsthelper(self,nums:list[int],start,end):
        if start > end :
            return None
        mid = (start+end)//2
        root = Node(nums[mid])
        root.left = self.ArrayToBsthelper(nums,start,mid-1)
        root.right = self.ArrayToBsthelper(nums,mid+1,end)
        return root 
    def ArrayToBst(self,nums:list[int]):
        return self.ArrayToBsthelper(nums,0,len(nums)-1)
    def PreOrder(self,root):
        if root is None :
            return
        print(root.item,end=' ')
        self.PreOrder(root.left)
        self.PreOrder(root.right)
    def InOder(self,root):
        if root is None :
            return
        self.InOder(root.left)
        print(root.item,end=' ')
        self.InOder(root.right)


sol = Solution()
nums=[1,2,3]
ans = sol.ArrayToBst(nums)
sol.PreOrder(ans)
 
        