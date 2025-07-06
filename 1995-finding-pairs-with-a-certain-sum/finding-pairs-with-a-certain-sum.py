class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.num1 = nums1
        self.counter = Counter(nums2)
        self.num2 = nums2

    def add(self, index: int, val: int) -> None:
        v = self.num2[index]
        newv = v + val
        self.counter[v] -= 1
        if newv in self.counter:
            self.counter[newv] += 1
        else:
            self.counter[newv] = 1 
        self.num2[index] = newv

    def count(self, tot: int) -> int:
        ct = 0
        counter = self.counter
        for i in self.num1:
            if tot - i in counter:
                ct = ct + counter.get(tot-i)
        return ct


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)