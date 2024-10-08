class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = i = 0
        j = 1
        temp = []
        while j <= len(arr):
            temp.append(arr[i:i+j])
            if i+j >= len(arr)  :
                i = 0
                j += 2
            else:
                i += 1
        res = [ sum(x) for x in temp ]
        return sum(res)
            

