class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]
        if len(arr) <= 1:
            return res
        # res = [arr[-1], -1]
        # if len(arr) == 2:
        #     return res
        # print(res)
        for i in range(len(arr)-1, 0, -1):
            # print(arr, res, i)
            val =[ max(arr[i], res[0])]
            val.extend(res)
            res = val
        return res
