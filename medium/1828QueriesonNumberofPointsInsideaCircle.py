class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        def isInside( point:List[int], circle:List[int])-> bool:
            center_x = circle[0]
            center_y = circle[1]
            radius = circle[2]
            if math.sqrt((point[0]-center_x)*(point[0]-center_x) + (point[1]-center_y)*(point[1]-center_y))<= radius:
                return True
            return False


        output = []
        for circle in queries:
            inside = 0
            for point in points:
                if isInside(point,circle):
                    inside +=1
            output.append(inside)
        

        return output
