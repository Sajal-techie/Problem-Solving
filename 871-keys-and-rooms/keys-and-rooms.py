class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        queue = [0]
        while queue:
            vertex = queue.pop()
            for i in rooms[vertex]:
                if not seen[i]:
                    seen[i] = True
                    queue.append(i)
        return all(seen)

            