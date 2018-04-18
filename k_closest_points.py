import math
import sys
# Find k closest points to the origin

#points are a list of tuples

# let's say all points are closer to the origin than sys.maxint

def euclideanDistFromOrigin(x, y):
	return math.sqrt(x*x + y*y)

def kClosest(k, points):
	closest_distances = []
	closest_points = []
	for i in range(k):
		closest_distances.append(sys.maxint)
		closest_points.append((0, 0))
	for point in points:
		dist = euclideanDistFromOrigin(point[0], point[1])
		for i, d in enumerate(closest_distances):
			if (dist < d):
				#shift all the entries by one
				closest_distances.insert(i,closest_distances.pop())
				closest_points.insert(i,closest_points.pop())
				closest_distances[i] = dist
				closest_points[i] = point
				break
	return closest_points

def main():
	points = [(-2, 4), (0, -2), (-1, 0), (3, 5), (-2, -3), (3, 2)]
	k = 2
	#print(euclideanDistFromOrigin(points[0][0], points[0][1]))
	print("all points:", points)
	print(k)
	print("K closest:", kClosest(k, points))
	k = 5
	print(k)
	print(kClosest(k, points))
	points = [(1, 1), (0, 1), (2, 1), (2, 2), (1, 2), (1, 0)]
	k = 3
	print("all points:", points)
	print(k)
	print("K closest:", kClosest(k, points))

main()