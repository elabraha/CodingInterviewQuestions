# CodingInterviewQuestions
A compilation of interview questions solved by me mostly in python.

1. k_closest_points.py
	- Question: Find the k closest points to the origin from a list of points.
	- I solved this problem by checking the euclidean distance between the point and the origin. Then I went through the list of points and checked each point against all k minimum distances (initialized with sys.maxint) and then if the distance was smaller than one of them on the list. I shifted the list of points and distances to the right by one. When the program has gone through the entire list of points I return the list of k closest points.
