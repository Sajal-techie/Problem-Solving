class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            print(i[11:13])
            if i[11:13] > '60':
                count += 1
        return count