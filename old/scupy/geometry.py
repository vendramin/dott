def Rect2Polygon(rect):
    return Polygon((rect.x, rect.y), (rect.x+rect.w, rect.y), (rect.x+rect.w, rect.y+rect.h), (rect.x, rect.y+rect.h))

class Polygon(object):

    def __init__(self, *points):
        self.points = points
    
    def collidepoint(self, x, y):
        """
        This method checks is a point is inside a polygon
    
        See:
        http://local.wasp.uwa.edu.au/~pbourke/geometry/insidepoly/
        """
        n = len(self.points)
        inside = False
        p1x, p1y = self.points[0]
        for i in range(n+1):
            p2x, p2y = self.points[i%n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x,p1y = p2x,p2y
        return inside

class Point2D(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

class Point3D(object):
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z


if __name__ == '__main__':
    poly = Polygon((0,0), (0, 2), (1,2), (1,0))
    print poly.collidepoint(1, 1)
    print poly.collidepoint(3, 0)
