class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = ''
        indx = 0
        for i in range(len(arr)):
            val = arr.pop(i)
            if val in arr:
                arr.insert(i,val)
            else:
                arr.insert(i,val)
                indx += 1 
                if indx == k:
                    break
        return val if indx == k else ''