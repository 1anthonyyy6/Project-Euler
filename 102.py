"""
Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.
"""
C = 0

for line in open('p102_triangles.txt'):
    ax, ay, bx, by, cx, cy = map(int, line.split(','))
    a = ax*by - ay*bx > 0
    b = bx*cy - by*cx > 0
    c = cx*ay - cy*ax > 0

    C+= a==b==c

print ("Number of triangles that contain the origin:", C)