class TreeNode :
    def __init__(self,val,start,end,left_child=None,right_child=None) :
        self.val=val
        self.start=start
        self.end=end
        self.left_child = left_child
        self.right_child = right_child

class SegmentTree :
    def __init__(self,nums):
        self.nums=nums
        self.root = self.build(0,len(nums)-1)
    
    def build(self,start,end):
        mid = (start+end)//2
        if start==end :
            return TreeNode(self.nums[start],start,end)
        left_child = self.build(start,mid)
        right_child = self.build(mid+1,end)
        return TreeNode(left_child.val,right_child.val,start,end,left_child,right_child)
    def update(self,root,index,value):
        if root.start==root.index and index==root.start : 
            root.val = value
            return value
        if root.start > index or root.end < index :
            return root.val
        
    def query(self,root,left,right):
        if root.start > right  or root.end<left :
            return 0
        if root.start >= left and root.end <= right :
            return root.val
        return self.query(root.left_child,left,right) + self.query(root.right,left,right)


class NumArray:
    def __init__(self,nums:list[int]):
        self.tree = SegmentTree(nums)
        self.root = self.tree.root 
    def update(self,index:int,val:int) -> int :
        self.tree.update(self.root,index,val)
    
    def sumRange(self,left:int,right:int) -> int : 
        return self.tree.query(self.root,left,right)
    
nums=[1,2,3,4,5]
obj = NumArray(nums)
ans = obj.sumRange(0,4)
print(ans)