class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_box = sorted(boxTypes, key=lambda x:x[1],reverse=True)
        print(sorted_box)
        i = 0
        res = 0
        while truckSize > 0 and i < len(sorted_box):
            print(res,i,truckSize)
            if sorted_box[i][0] <= truckSize:
                truckSize -= sorted_box[i][0]
                res += sorted_box[i][1] * sorted_box[i][0]
                i+=1
            else:
                res = res + sorted_box[i][1] * truckSize
                i+=1
                truckSize = 0
        return res