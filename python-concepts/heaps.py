

# import heapq
# heap=[]

# heapq.heappush(heap,10)
# heapq.heappush(heap,1)
# heapq.heappush(heap,15)

"""Heap pop -
    It will return the smallest value and also it will delete that from heap ,maintaining the heap property
    Root Node is getting deleted
 """

# heapq.heappop(heap)



"""
    Heapify
"""
# import heapq
# list1 :list[int] = [1,3,5,2,4,6]
# heapq.heapify(list1)
# print(list1)


"""
    Heap pushpop  --> First push and then pop
"""
# import heapq
# list1:list[int] = [1,3,5,2,4,6]
# heapq.heapify(list1)
# heapq.heappushpop(list1,76)
# print(list1)


"""
    Heap pushreplace --> First pop and then push
"""
# import heapq
# list1:list[int] = [1,3,5,2,4,6]
# heapq.heapify(list1)
# heapq.heapreplace(list1,100)
# print(list1)


"""
    nsmallest and nlargest
"""
import heapq
list1:list[int] = [1,20,5,4,6,8]
smallest,largest  =  heapq.nsmallest(2,list1),heapq.nlargest(2,list1)
print(smallest)
print('\n')
print(largest)