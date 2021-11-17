#area and shape prediction
#arguments: 1 number of sides, side length for regular polygon
#arguments: interior exterior angle and then calculate area
#irregular polygon: shape prediction can be done not area!

import math

shapes = {3:'Equilateral Triangle',4:'Square',5:'Regular Pentagon',6:'Regular hexagon',7:'Regular heptagon',8:'Regular Octagon',9:'Regular Nonagon',10:'Regular Decagon'}

class polygon:

    shape_predict=None
    area = None
    
    #Ref:https://www.quora.com/What-is-the-maximum-number-of-sides-a-regular-polygon-can-have-such-that-its-interior-angles-in-degrees-are-integers
    def predict_shape(self,n):
        if(n in shapes.keys()):
            self.shape_predict = shapes[n]
        else:
            self.shape_predict = 'Polygon with ' + str(n) + 'sides'
        return

    def get_area(self,n,length_of_side):
        apothem = length_of_side/(2*math.tan((math.pi)/n))
        area = (n * length_of_side * apothem)/2
        return round(area,3)

    def polygon_features(self,no_of_sides,length_of_side):
        n = no_of_sides
        self.area = self.get_area(n,length_of_side)
        self.perimeter = n * length_of_side          
        self.interior_angle = 180 * (n-2)/n
        self.exterior_angle = 180 - self.interior_angle
        return

    def sides_length(self,no_of_sides,length_of_side):
        if(not type(no_of_sides) is int):
            raise Exception('Invalid data type for no_of_sides:{}'.format(type(no_of_sides)))
        if(not type(length_of_side) is float and not type(length_of_side) is int):
            raise Exception('Invalid data type for length_of_each_side:{}'.format(type(length_of_side)))
        elif(no_of_sides in [0,1,2,360]):
            raise Exception('Polygon must have number of sides in [3,360).You entered',no_of_sides)
        elif(no_of_sides < 0 or length_of_side<0):
            raise Exception('Polygon cannot have negative number of sides.')
        elif(length_of_side==0):
            raise Exception('Polygon cannot have side with length 0!')
        else:
            n = no_of_sides
            self.predict_shape(n)
            self.polygon_features(n,length_of_side)
            features=["","","","",""]
            features[0]=self.shape_predict
            features[1]=self.area
            features[2]=self.perimeter
            features[3]=self.interior_angle
            features[4]=self.exterior_angle
        return features

    def use_interior_angle(self,interior_angle,length_of_side):
        if(not type(interior_angle) is int and not type(interior_angle) is float):
            raise Exception('Interior angle should be integer or float')
        if(not type(length_of_side) is float and not type(length_of_side) is int):
            raise Exception('Length of side should integer or float and type you given is :',type(length_of_side))
        if(interior_angle >=180 or interior_angle<=0):
            raise Exception("Interior angle should in range (0,180)!")
        elif(length_of_side<=0):
            raise Exception('Length of side <= 0 which is invalid!')
        #interior_angle = 180 * (n-2)/n
        #interior_angle / 180 = 1-2/n i.e
        # 1- (interior_angle/180) = 2/n 
        #i.e n = 2 / (1-interior_angle/180) then if n is integer then it is valid
        
        temp = interior_angle / 180
        print(temp)
        temp = 1 - temp
        print(temp)
        print(interior_angle,temp)
        n = 2/temp
        n = round(n,3)
        if( n - int(n) == 0):
            self.predict_shape(n)
            self.polygon_features(n,length_of_side)
        else:
            raise Exception('From calculation, We got as {} number of sides'.format(n))
        features=["","","","",""]
        features[0]=self.shape_predict
        features[1]=self.area
        features[2]=self.perimeter
        features[3]=self.interior_angle
        features[4]=self.exterior_angle
        return features

    def use_exterior_angle(self,exterior_angle,length_of_side):
        if(not type(exterior_angle) is int and not type(exterior_angle) is float):
            raise Exception('Wrong input type is provided!')
        if(not type(length_of_side) is float and not type(length_of_side) is int):
            raise Exception('Length of side should integer or float')
        if(exterior_angle >=180 or exterior_angle<=0):
            raise Exception("You have entered invalid exterior angle(not in range(0,180))")
        elif(length_of_side<=0):
            raise Exception('Polygon cannot have side with length <=0!Input valid length')
        n = float(360/exterior_angle)
        if( n - int(n) == 0):
            self.predict_shape(n)
            self.polygon_features(n,length_of_side)
        else:
            raise Exception('We are getting number of sides as float which is impossible!You entered Invalid  interior angle')
        features=["","","","",""]
        features[0]=self.shape_predict
        features[1]=self.area
        features[2]=self.perimeter
        features[3]=self.interior_angle
        features[4]=self.exterior_angle
        return features

    #Handled for triangle and rectangle
    def irregular_polygon(self,*args):
        n = len(args)
        if(n in [0,1,2]):
            raise Exception('Polygon must have number of sides>=3')
        elif(n >=5):
            raise Exception('Currently not available')
        if n==3:
            for x in args:  
                if(not type(x) is int and not type(x) is float):
                    raise Exception("Unsupported Data type")   
                if(x<=0):
                    raise Exception("Polygon with 3 sides not possible(length<=0)!")
            a = args[0]
            b = args[1]
            c = args[2]
            dict={a:0,b:0,c:0}
            dict[a]+=1
            dict[b]+=1
            dict[c]+=1
            if(a<=0 or b<=0 or c<=0):
                raise Exception("Triangle with <=0 sides found") 
            elif(a+b<=c or a+c<=b or b+c<=a):
                raise Exception("Basic Triangle property lost")
            else:
                if(len(dict)==1):
                    self.shape_predict = 'Equilateral Triangle'
                elif(len(dict)==2):
                    self.shape_predict = 'Isosceles Triangle'
                else:
                    self.shape_predict = 'Scalene Triangle'
                s=(a+b+c)/2
                self.area = math.sqrt(s*(s-a)*(s-b)*(s-c))
                self.perimeter = a + b + c
                features=[]
                features.append(self.shape_predict)
                features.append(round(self.area,4))
                features.append(self.perimeter)
        elif n == 4:
            dict={args[0]:0,args[1]:0,args[2]:0,args[3]:0}
            for x in args:
                if(not type(x) is int and not type(x) is float):
                    raise Exception("Unsupported Data type")   
                if(x<=0):
                    raise Exception("Polygon with 4 sides (length<=0)!")
                dict[x]+=1
            if(len(dict)==1):
                self.shape_predict = 'Square'
                self.area = args[0]*args[0]
                self.perimeter = 4*args[0]
            elif(len(dict)==2):
                self.shape_predict = 'Rectangle'
                self.area = 1
                self.perimeter = 0
                for side in dict.keys():
                    self.perimeter +=2*side
                    self.area *= side
            else:
                self.shape_predict = 'Polygon with 4 sides!(neither rectangle nor square)'
                self.perimeter = args[0] + args[1] + args[2] + args[3]
                self.area = "difficult to find!"
            features=[]
            features.append(self.shape_predict)
            features.append(self.area)
            features.append(self.perimeter)
            
        return features
'''
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
'''