class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'  # String containing all vowel characters
        num_v = 0  # Variable to count the number of vowels in the current window
        
        # Initialize the count of vowels in the first window of size k
        for l in s[:k]:
            if l in vowels:
                num_v += 1
        
        max_v = num_v  # Initialize max_v with the number of vowels in the first window
        
        # Slide the window across the string
        for i in range(k, len(s)):
            # If the character leaving the window is a vowel, decrement num_v
            if s[i - k] in vowels:
                num_v -= 1
            
            # If the new character entering the window is a vowel, increment num_v
            if s[i] in vowels:
                num_v += 1
            
            # Update max_v if the current count of vowels is greater
            max_v = max(max_v, num_v)
        
        return max_v  # Return the maximum number of vowels found in any window of length k