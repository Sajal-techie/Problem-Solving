class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = {
            "area": 0,
            "diagonal":0,
            "length":0,
            "width":0,
        }
        n, m = len(dimensions), len(dimensions[0])
        for i in range(n):
            l, w = dimensions[i][0], dimensions[i][1]
            d = (l*l)+ (w*w)
            if d > res.get("diagonal"):
                res['diagonal'] = d
                res["area"] = l * w
                res["length"] = l
                res['width'] = w
            elif d == res.get("diagonal"):
                if l * w > res.get("area"):
                    res['area'] = l * w
                    res['width'] = w
                    res['length'] = l
        return res.get("area")