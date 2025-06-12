# Designing dynamic array

class DynamicArray:

    def __init__(self,capacity:int):
        self.capacity = capacity
        self.length=0
        self.arr = [0]*self.capacity
    
    # get value at i-index
    def get(self,i:int)->int:
        return self.arr[i]
    
    # set n at i index
    def set(self,i:int,n:int)-> None:
        self.arr[i]=n

    
    # resizing the array
    def resize(self)-> None:
        # create new array of double capacity
        self.capacity=2*self.capacity
        new_array=[0]*self.capacity


        # copying the elements into new array
        for i in range(self.length):
            new_array[i]=self.arr[i]
        self.arr = new_array

    # inserting n elements at the last position
    def pushback(self,n:int)->None:
        if self.length==self.capacity:
            self.resize()
        
        self.arr[self.length]=n
        self.length+=1
    
    # remove the last element from the array
    def popback(self) -> int:
        if self.length>0:
            self.length-=1
        return self.arr[self.length]
    
    def getSize(self)->int :
        return self.length
    
    def getCapacity(self)->int:
        return self.capacity


def main():
    # print("Creating a dynamic array with capacity 2...")
    dyn_arr = DynamicArray(4)
    dyn_arr.pushback(1)
    dyn_arr.pushback(2)
    dyn_arr.pushback(3)
    dyn_arr.pushback(4)

    for i in range(dyn_arr.getSize()):
        print(f'Index {i} : {dyn_arr.get(i)} ')

    # print("\nPushing values 10, 20, 30...")
    # dyn_arr.pushback(10)
    # dyn_arr.pushback(20)
    # dyn_arr.pushback(30)  # Should trigger resize

    # print(f"\nArray size: {dyn_arr.getSize()}")       # Should be 3
    # print(f"Array capacity: {dyn_arr.getCapacity()}")  # Should be 4 (doubled)

    # print("\nGetting values:")
    # for i in range(dyn_arr.getSize()):
    #     print(f"Index {i}: {dyn_arr.get(i)}")

    # print("\nSetting value at index 1 to 99...")
    # dyn_arr.set(1, 99)
    # print(f"Value at index 1: {dyn_arr.get(1)}")  # Should be 99

    # print("\nPopping last value...")
    # popped = dyn_arr.popback()
    # print(f"Popped value: {popped}")
    # print(f"New size: {dyn_arr.getSize()}")       # Should be 2

    # print("\nFinal array values:")
    # for i in range(dyn_arr.getSize()):
    #     print(f"Index {i}: {dyn_arr.get(i)}")


# Run the main method if this file is executed directly
if __name__ == "__main__":
    main()
