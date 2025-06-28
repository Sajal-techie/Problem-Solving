class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        new=[(v,i) for i,v in enumerate(nums)]
        new.sort(reverse=True)
        if k>len(new):return []

        cur=new[:k]
        cur.sort(key=lambda x:(x[1]))
        return [i[0] for i in cur]