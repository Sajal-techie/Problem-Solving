class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = r = i = 0
        senate = list(senate)
        while "D" in senate and "R" in senate:
            if "D" == senate[i]:
                if r > 0:
                    r -= 1
                    senate.pop(i)
                else:
                    d += 1
                    i += 1
            elif "R" == senate[i]:
                if d > 0:
                    d -= 1
                    senate.pop(i)
                else:
                    r += 1
                    i += 1
            if i >= len(senate):
                i = 0
                
        return "Dire" if senate[0] == "D" else "Radiant" 