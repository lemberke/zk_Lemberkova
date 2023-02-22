# Zkouška z úvodu do programování
# Úloha 67: Test, jestli se bod nachází uvnitř, vně nebo na hraně konvexního mnohoúhelníku
# Eva Lemberková, MOBIBO, 2. ročník

import turtle

#class "Point", where each object is characterised by coordinates x and y
class Point:
    def __init__(self, coordinate_x, coordinate_y):
        self.__coordinate_x = coordinate_x 
        self.__coordinate_y = coordinate_y

    #method "getx()" gets x coordinate from an object of class "Point"  
    def getx(self):
        return self.__coordinate_x

    #method "gety()" gets y coordinate from an object of class "Point" 
    def gety(self):
        return self.__coordinate_y

#class "Line" which is characterised by two points
class Line:
    def __init__(self, point_A, point_B):
        self.__point_A = point_A
        self.__point_B = point_B
    
    def location(self, analyzed_point):
        # vector of the line containting the edge of polygon
        u = [self.__point_B.getx() - self.__point_A.getx(), self.__point_B.gety() - self.__point_A.gety()]
        # vector from the beginning point of the vector "u" to a point "analyzed_point"
        v = [analyzed_point.getx() - self.__point_A.getx(), analyzed_point.gety() - self.__point_A.gety()]
        # t = u_x*v_y - u_y*v_x
        t = u[0]*v[1] - u[1]*v[0]
        if t > 0:
            return "left"
        # checks if the analyzed point lies on the edge of polygon not only on the line
        elif t == 0 \
            and analyzed_point.getx() >= min(self.__point_A.getx(), self.__point_B.getx()) \
            and analyzed_point.getx() <= max(self.__point_A.getx(), self.__point_B.getx()) \
            and analyzed_point.gety() >= min(self.__point_A.gety(), self.__point_B.gety()) \
            and analyzed_point.gety() <= max(self.__point_A.gety(), self.__point_B.gety()):
            return "on"
        return "right"        

#class "Polygon" characterised by various amount of vertices 
class Polygon:
    def __init__(self, *v): 
        self.__number_of_v = len(v)

        #if the amount of vertices is lower than 3, the exception is raised, because from the vertices no polygon can be constructed
        if len(v) < 3:
            raise Exception("The shape is not a polygon, because less than three vertices were given.")
        
        self.__vertices = v

        #all edges of the polygon are appended to the list of edges 
        self.list_of_edges = []
        for i, vrchol in enumerate(self.__vertices):
            self.list_of_edges.append(Line(self.__vertices[i-1],vrchol))

    #function "location_of_point" determines the orientation of point for every edge of polygon, and then decides about the location of the point 
    def location_of_point(self, analyzed_point):
        last_orientation = None
        for edge in self.list_of_edges:
            orientation = edge.location(analyzed_point)
            if orientation == "on":
                return "The point lies on the edge of the polygon."
            elif last_orientation and orientation != last_orientation:
                return "The point lies outside of the polygon."
            last_orientation = orientation
            return "The point lies inside of the polygon."
      
#the exception against opening an empty or non-existing file
try:
    with open("67_vrcholy_a_bod.txt", encoding = "utf-8") as f:
        assert(len(f.readlines()) > 0)
except FileNotFoundError:
    print("The file you are trying to open does not exist.")
    quit()
except AssertionError:
    print("You are opening an empty file.")
    quit()

#opening the file "67_vrcholy_a_bod.txt" for reading and loading it to the variable "data"       
with open("67_vrcholy_a_bod.txt", encoding = "utf-8") as f:
    data = f.read()

    #loading dates to the list
    list_of_data = data.split("\n")

    #list of points to which the points from the list of dates are added and they become objects from class Point
    list_of_points = []
    for b in list_of_data:
        x, y = b.split(",")
        list_of_points.append(Point(float(x),float(y)))

    #an object from class "Point", which is on the last position in the list "list_of_points" and it represents the point, whose location we analyze        
    point = list_of_points[-1]

    #an object from class "Polygon", which is characterised by the "list_of_points" but without the item on the list position of the list and these items represent the vertices of the polygon
    polygon = Polygon(*list_of_points[0:-1])

    print(polygon.location_of_point(point))

    #visualising the polygon
    for vrchol in polygon._Polygon__vertices:
        turtle.setpos(vrchol.getx(),vrchol.gety())
    turtle.setpos(polygon._Polygon__vertices[0].getx(),polygon._Polygon__vertices[0].gety())

    #visualising the point
    turtle.penup()
    turtle.setpos(point.getx(),point.gety())
    turtle.pendown()
    turtle.dot()

    turtle.exitonclick()






