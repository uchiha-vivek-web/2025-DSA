def longest_subarray_with_sum_less_than_k(arr, k):
    left = 0
    current_sum = 0
    max_length = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum >= k and left <= right:
            current_sum -= arr[left]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example usage
arr = [1, 2, 3, 4, 5]
k = 8
print(longest_subarray_with_sum_less_than_k(arr, k))  # Output: 3
