import numpy as np

# 2D vectors
v1 = np.array([2, 4])
v2 = np.array([5, 3])
v3 = np.array([7, 12])
v4 = np.array([3, 8])

# 3D lines (direction vectors)
l1 = np.array([-2, 1, 1])
l2 = np.array([2, 3, 1])

#  3D points
p1 = np.array([10, 6, 2])
p2 = np.array([2, 8, 1])
p3 = np.array([5, 3, 1])
p4 = np.array([7, 9, 1])

#1.1    Vector addition
print(np.add(v1, v2))  # or print(v1 + v2)

#1.2    Vector subtraction
print(np.subtract(v3, v2))  # or print(v3 - v2)

#1.3    scalar multiplication
print(np.multiply(5, v4))  # or print(5 * v4)

#1.4    dot product
print(np.dot(p2, l1))  # or print(p2 @ l1)

#1.5    cross product
print(np.cross(p2, l1))


#1.6    equivalence of points
def are_equivalent(t1, t2): # comparing if one is a scalar multiple of the other
    return all(t1[i] / t2[i] == t1[0] / t2[0] if t2[i] != 0 else t1[i] == 0 for i in range(len(t1)))


points = [p1, p2, p3, p4]

for i, point1 in enumerate(points):
    for j, point2 in enumerate(points[i + 1:], i + 1):
        if np.array_equal(point1, point2) or are_equivalent(point1, point2):
            print(f"point{i + 1} and point{j + 1} are equivalent.")

########################

p1 = np.array([500, 900, 1])  # blue point at the bottom
p2 = np.array([1700, 1300, 1])  # blue point at the top
l2 = np.array([900, 1050, -2287500])  # green line
p4 = np.array([1046, 1082, 1])  # white car marked with red x
p5 = np.array([1310, 1220, 1])  # black car marked with red x

#2.1    equivalence of points
if are_equivalent(p1, p2):
    print("p1 and p2 are equivalent.")
else:
    print("p1 and p2 are not equivalent.")

#2.2    line through two points
l1 = np.cross(p1, p2)
print(l1)


#2.3    convert to cartesian line equation
# Helper method to correctly format terms with proper signs (+/-).
# This method does not affect the core task; it's just for formatting the output properly.
def format_term(coef, variable):
    if coef > 0:
        return f"+ {coef}{variable}"
    elif coef < 0:
        return f"- {-coef}{variable}"
    else:
        return ""


a, b, c = l1  # (a,b,c)
print(f"{format_term(a, 'x')} {format_term(b, 'y')} {format_term(c, '')} = 0".strip())

#2.4   find slope and y-intercept
#impossible if b = 0; means line is vertical -> slope and y-intercept are undefined
print("slope :", -(a / b))
print("y-intercept :", -(c / b))

#2.5    intersection point
p_homogeneous = np.cross(l1, l2)
# Normalize the result by dividing both the first and second components by the third component (homogeneous coordinate)
p_cartesian = p_homogeneous[:2] / p_homogeneous[2]
print(p_cartesian)


#2.6    point-on-line check
# Function to check if a point lies on the line
def is_point_on_line(point, line, threshold=1e-5):
    # Extract the line coefficients (a, b, c)
    a, b, c = line
    # Get the x and y coordinates of the point
    x, y = point

    # Calculate the result of the line equation: ax + by + c
    result = a * x + b * y + c

    # Check if the result is close to 0 within the given threshold
    return abs(result) < threshold


print("p4 on line l1:", is_point_on_line([(p4[0]/p4[2]),(p4[1]/p4[2])], l1))   # normalize?
print("p5 on line l1:", is_point_on_line([p5[0],p5[1]], l1))                    # normalize?
