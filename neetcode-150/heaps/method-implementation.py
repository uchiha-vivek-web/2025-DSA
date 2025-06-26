class MaxHeap:
    def __init__(self):
        self.heap = [None]  # 1-based indexing

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def parent(self, i):
        return i // 2

    def max_heapify(self, i):
        heap_size = len(self.heap)
        l = self.left(i)
        r = self.right(i)
        largest = i

        if l < heap_size and self.heap[l] > self.heap[largest]:
            largest = l
        if r < heap_size and self.heap[r] > self.heap[largest]:
            largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in range((len(self.heap) - 1) // 2, 0, -1):
            self.max_heapify(i)

    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_max(self):
        if len(self.heap) <= 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        max_val = self.heap[1]
        self.heap[1] = self.heap.pop()  # Move last to root
        self.max_heapify(1)
        return max_val

    def heap_sort(self):
        # Create a copy to preserve original heap
        original = self.heap[:]
        result = []
        while len(self.heap) > 1:
            result.append(self.extract_max())
        self.heap = original  # Restore
        return result


# Example usage
def main():
    heap = MaxHeap()
    
    # Initial bulk build
    initial_data = [0, 5, 20, 6, 12, 65, 1, 4, 9, 3, 89, 22, 25, 28, 10]
    heap.heap.extend(initial_data)  # Adding values starting from index 1
    heap.build_max_heap()
    
    print("✅ Built Max Heap:", heap.heap[1:])

    heap.insert(100)
    print("✅ After Insert 100:", heap.heap[1:])

    max_val = heap.extract_max()
    print("✅ Extracted Max:", max_val)
    print("✅ Heap After Extraction:", heap.heap[1:])

    sorted_list = heap.heap_sort()
    print("✅ Heap Sort Result:", sorted_list)


main()
