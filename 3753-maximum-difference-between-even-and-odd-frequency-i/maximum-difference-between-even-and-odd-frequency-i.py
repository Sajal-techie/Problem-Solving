class Solution:
    def maxDifference(self, s: str) -> int:
        hash = Counter(s)
        oddmax = 0
        evenmax = 110
        for i in hash.values():
            if i % 2 == 0:
                evenmax = min(evenmax, i)
            else:
                oddmax = max(oddmax, i)
        return oddmax - evenmax