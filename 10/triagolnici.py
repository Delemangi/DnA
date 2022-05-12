import queue


class Triagolnici:
    def mnoguagolnici(self, XY):
        graph = HashGraph(len(XY) * 3)
        not_visited = set()

        for triangle in XY:
            x1, y1, x2, y2, x3, y3 = map(int, triangle.split(' '))
            a, b, c = (x1, y1), (x2, y2), (x3, y3)

            not_visited.add(a)
            not_visited.add(b)
            not_visited.add(c)

            graph.add_edge(a, b)
            graph.add_edge(b, a)
            graph.add_edge(a, c)
            graph.add_edge(c, a)
            graph.add_edge(b, c)
            graph.add_edge(c, b)

        for triangle1 in XY:
            for triangle2 in XY:
                if triangle1 != triangle2:
                    x1, y1, x2, y2, x3, y3 = map(int, triangle1.split(' '))
                    a, b, c = Point(x1, y1), Point(x2, y2), Point(x3, y3)
                    x1, y1, x2, y2, x3, y3 = map(int, triangle2.split(' '))
                    d, e, f = Point(x1, y1), Point(x2, y2), Point(x3, y3)

                    if any(do_intersect(i, j, k, l) for i, j in ((a, b), (b, c), (a, c)) for k, l in ((d, e), (e, f), (d, f))):
                        graph.add_edge((a.x, a.y), (d.x, d.y))
                        graph.add_edge((d.x, d.y), (a.x, a.y))

        visited = set()
        convex_hulls = []

        for node in not_visited:
            if node not in visited:
                connected = graph.connected(node)

                for n in connected:
                    visited.add(n)

                convex = convex_hull(connected)
                convex_hulls.append(convex)

        return ' '.join(str(len(coords)) + ' ' + ' '.join(str(x) + ' ' + str(y) for x, y in sorted(coords)) for coords in sorted(convex_hulls, key=min))


class AbstractGraph:
    def __init__(self, num_vertices: int):
        self.inf = float('inf')
        self.num_vertices = num_vertices
        self.graph = None

    def add_edge(self, fr, to, weight: float = 0):
        raise NotImplementedError

    def connected(self, src) -> set:
        connections_set = {src}
        q = queue.Queue()
        q.put(src)
        while not q.empty():
            vertex = q.get()
            for neighbour in self.graph[vertex]:
                if neighbour not in connections_set:
                    connections_set.add(neighbour)
                    q.put(neighbour)
        return connections_set


class HashGraph(AbstractGraph):
    def __init__(self, num_vertices: int):
        super().__init__(num_vertices)
        self.graph = {}

    def add_edge(self, fr, to, weight: float = 0):
        if fr not in self.graph:
            self.graph[fr] = {}
        self.graph[fr][to] = weight


def convex_hull(points):
    """Computes the convex hull of a set of 2D points.
    Input: an iterable sequence of (x, y) pairs representing the points.
    Output: a list of vertices of the convex hull in counter-clockwise order,
      starting from the vertex with the lexicographically smallest coordinates.
    Implements Andrew's monotone chain algorithm. O(n log n) complexity.
    """

    # Sort the points lexicographically (tuples are compared lexicographically).
    # Remove duplicates to detect the case we have just one unique point.
    points = sorted(set(points))

    # Boring case: no points or a single point, possibly repeated multiple times.
    if len(points) <= 1:
        return points

    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list.
    return lower[:-1] + upper[:-1]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def on_segment(p, q, r):
    if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
            (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False


def orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Colinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise

    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/
    # for details of below formula.

    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):

        # Clockwise orientation
        return 1
    elif (val < 0):

        # Counterclockwise orientation
        return 2
    else:

        # Colinear orientation
        return 0


# The main function that returns true if
# the line segment 'p1q1' and 'p2q2' intersect.
def do_intersect(p1, q1, p2, q2):
    # Find the 4 orientations required for
    # the general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True

    # Special Cases

    # p1 , q1 and p2 are colinear and p2 lies on segment p1q1
    if (o1 == 0) and on_segment(p1, p2, q1):
        return True

    # p1 , q1 and q2 are colinear and q2 lies on segment p1q1
    if (o2 == 0) and on_segment(p1, q2, q1):
        return True

    # p2 , q2 and p1 are colinear and p1 lies on segment p2q2
    if (o3 == 0) and on_segment(p2, p1, q2):
        return True

    # p2 , q2 and q1 are colinear and q1 lies on segment p2q2
    if (o4 == 0) and on_segment(p2, q1, q2):
        return True

    # If none of the cases
    return False
