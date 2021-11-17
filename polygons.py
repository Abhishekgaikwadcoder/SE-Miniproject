#area and shape prediction
#arguments: 1 number of sides, side length for regular polygon
#arguments: interior exterior angle and then calculate area
#irregular polygon: shape prediction can be done not area!

import math

shapes = {3:'Equilateral Triangle',4:'Square',5:'Regular Pentagon',6:'Regular hexagon',7:'Regular heptagon',8:'Regular Octagon',9:'Regular Nonagon',10:'Regular Decagon'}

class polygon:

    shape_predict=None
    area = None
    
    #NOTE:https://www.quora.com/What-is-the-maximum-number-of-sides-a-regular-polygon-can-have-such-that-its-interior-angles-in-degrees-are-integers
    
    def predict_shape(self,n):
        if(n in shapes.keys()):
            self.shape_predict = 'It is ' + shapes[n]
        else:
            self.shape_predict = 'It is Polgon with ' + str(n) + 'sides'
        print(self.shape_predict)
        return

    def get_area(self,n,length_of_side):
        apothem = 1/(2*math.tan((math.pi)/n))
        area = (n * length_of_side * apothem)/2
        return area

    def polygon_features(self,no_of_sides,length_of_side):
        self.area = get_area(no_of_sides,length_of_side)
        self.perimeter = n * length_of_side          
        self.interior_angle = 180 * (n-2)/n
        self.exterior_angle = 180 - self.interior_angle
        print(self.area,self.perimeter, self.interior_angle,self.exterior_angle)
        return

    def sides_length(self,no_of_sides,length_of_side):
        if(not type(no_of_sides) is int):
             raise Exception('Number of sides should be integere is provided!')
        if(not type(length_of_side) is float and not type(length_of_side) is int):
            raise Exception('Length of side should integer or float')
        elif(no_of_sides in [0,1,2,360]):
            raise Exception('Polygon must have number of sides >=3 and less than 360 sides.Input valid number of sides.')
        elif(no_of_sides < 0 or length_of_side<0):
            raise Exception('Polygon cannot havenegative no of sides as well as length of side.')
        elif(length_of_side==0):
            raise Exception('Polygon cannot have side with length 0!Input valid length')
        else:
            self.predict_shape(no_of_sides)
            self.polygon_features(n,length_of_side)
        return

    def interior_angle(self,interior_angle,length_of_sides):
        if(not type(interior_angle) is int and not type(interior_angle) is float):
            raise Exception('Interior angle should be integer or float')
        if(not type(length_of_side) is float and not type(length_of_side) is int):
            raise Exception('Length of side should integer or float')
        if(interior_angle >=180 and interior_angle<=0):
            raise Exception("You have entered invalid interior angle.")
        elif(length_of_side<=0):
            raise Exception('Length of side <= 0 which is invalid!')
        #interior_angle = 180 * (n-2)/n
        #interior_angle / 180 = 1-2/n i.e 1- (interior_angle/180) = 2/n i.e n = 2 / (1-interior_angle/180) then if n is integer then it is valid
        temp = float(interior_angle / 180)
        temp = 1 - temp
        n = float(2/temp)
        if( n - int(n) == 0):
            self.predict_shape(no_of_sides)
            self.polygon_features(n,length_of_side)
        else:
            raise Exception('We are getting number of sides as float!You entered Invalid  interior angle')
        return

    def exterior_angle(self,exterior_angle,length_of_sides):
        if(not type(exterior_angle) is int and not type(exterior_angle) is float):
            raise Exception('Wrong input type is provided!')
        if(not type(length_of_side) is float and not type(length_of_side) is int):
            raise Exception('Length of side should integer or float')
        if(exterior_angle >=180 and exterior_angle<=0):
            raise Exception("You have entered invalid interior angle")
        elif(length_of_side==0):
            raise Exception('Polygon cannot have side with length 0!Input valid length')
        n = float(360/exterior_angle)
        if( n - int(n) == 0):
            self.predict_shape(no_of_sides)
            self.polygon_features(n,length_of_side)
        else:
            raise Exception('We are getting number of sides as float which is impossible!You entered Invalid  interior angle')
        return

    #for triangle rectangle
    def irregular_polygon(*args):
        n = len(args)
        if(n in [0,1,2]):
            raise Exception('Polygon must have number of sides>=3')
        for k in args:
            if(not type(k) is int or not type(k) is float):
                raise Exception('Wrong input type is provided!')
            elif(k==0):
                pass
        return
