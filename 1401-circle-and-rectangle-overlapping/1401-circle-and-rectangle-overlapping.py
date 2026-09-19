class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the point on the rectangle closest to the circle center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate distance components between circle center and closest point
        dist_x = xCenter - closest_x
        dist_y = yCenter - closest_y
        
        # Check if the squared distance is within radius^2
        return (dist_x ** 2 + dist_y ** 2) <= (radius ** 2)  