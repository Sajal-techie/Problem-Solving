class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []
        for i in range(len(nums)):
            if i % 3 == 0:
                res.extend([temp.copy()])
                temp.clear()
            temp.append(nums[i])
        else:
            res.extend([temp.copy()])
        print(nums)
        res.pop(0)
        print(temp, res)
        count = 0
        for i in res:
            for j in range(len(i)):
                if j > 0: 
                    continue
                if abs(i[j + 1] - i[j]) > k:
                    break
                if abs(i[j] - i[j+2]) > k:
                    break
                if abs(i[j-1] - i[j+2]) > k:
                    break
            else:
                count += 1
                
        if count == len(nums)/3:
            return res
        return []
