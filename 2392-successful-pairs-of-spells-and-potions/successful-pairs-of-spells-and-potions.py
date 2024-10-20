class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m, n = len(potions), len(spells)
        # print(potions,m)
        def binary_search(l, r, key):
            if key * potions[0] >= success:
                return m 
            while l < r:
                mid = (l + r)//2
                # print(key * potions[mid], 'vall', key, mid , potions[mid])
                if key * potions[mid] < success:
                    if mid + 1 < m :
                        if  key * potions[mid+1] >= success:
                            return m - (mid + 1)
                        else:
                            l = mid + 1
                    else:
                        return m - mid
                elif key * potions[mid] > success:
                    if mid - 1 >= 0 :
                        if  key * potions[mid-1] < success:
                            return m - mid
                        else:
                            r = mid - 1
                    else:
                        return m - mid
                else:
                    return m - mid
            return 0 
        res = []
        # print(res)
        for i in spells:
            res.append(binary_search(0, m-1, i))
        return res