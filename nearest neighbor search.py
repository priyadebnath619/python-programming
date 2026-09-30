import math
def distance(p1,p2):
    return math.sqrt(sum((a-b) ** 2 for a,b in zip(p1,p2)))
n=int(input("enter number of points"))
points=[]
for i in range(n):
    coords=input(f"enter coordinates of point [i+1] (seperated by space ): ").split()
    points.append(tuple(float(x) for s in coords))
query=tuple(float(x) for x in input("enter coordinates of query point(seperated by spaces):").split())
min_distance=float('inf')
closest_point=None
for point in points:
    d=distance(point,query)
    if d < min_ditance:
        min_distance=d
        closest_point=point
print(f"\n closest point to {query} is {closest_point} with a distance of {min_distance:.4f}")            
'