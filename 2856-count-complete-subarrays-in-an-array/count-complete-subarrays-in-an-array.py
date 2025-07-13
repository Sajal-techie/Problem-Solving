class Solution:
    def countCompleteSubarrays(self, nums):
        # Count the number of unique elements in nums
        unique_count = len(set(nums))
        # Initialize a counter to keep track of the frequency of elements
        elem_freq = Counter()
        # Initialize the answer and get the length of the nums array
        total_subarrays, length = 0, len(nums)
        # Start pointer for the sliding window
        start_index = 0
      
        # Iterate over nums with an end pointer for the sliding window
        for end_index, value in enumerate(nums):
            # Update the frequency count of the current element
            elem_freq[value] += 1
            # Shrink the window from the left if all unique elements are included
            while len(elem_freq) == unique_count:
                # Current number of complete subarrays is (length-end_index)
                total_subarrays += length - end_index
                # Decrease the freq count of the element at the start of the window
                elem_freq[nums[start_index]] -= 1
                # Remove the element from the counter if its count drops to zero
                if elem_freq[nums[start_index]] == 0:
                    elem_freq.pop(nums[start_index])
                # Move the start pointer to the right
                start_index += 1
      
        # Return the total number of complete subarrays
        return total_subarrays
