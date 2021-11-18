from polygons import *
# import rich
from prettytable import PrettyTable


# Colors 
valid = '\033[92m'   # Green
invalid = '\033[91m' # Red
endc = '\033[0m'
yellow = '\033[93m'
blue = '\033[94m'

# TABLE : TEST_CASE:  | Arguments |  Output  |
class testing_polygon():
    def print_features(self,features):
        f=""
        f+='Shape: '+features[0]+'\n'
        f+='Area: '+str(features[1])+'\n'
        f+='Perimeter: '+str(features[2])+'\n'
        f+='Interior_angle: '+str(features[3])+'\n'
        f+='Exterior_angle: '+str(features[4])+'\n'
        return f

    def print_features_1(self,features):
        f=""
        f+='Shape: '+features[0]+'\n'
        f+='Area: '+str(features[1])+'\n'
        f+='Perimeter: '+str(features[2])+'\n'
        return f

    def testing_using_sides(self):

        test_table = PrettyTable([blue + "TEST_CASE"+ endc, blue + "arguments" + endc,blue + "Output" + endc])
        test_table.align = 'l'
        p1 = polygon()
        try:
            features = p1.sides_length(6.2,8)
        except Exception as e:
            test_table.add_row(["Float input:", "N=6.2,L=8",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.sides_length(0,4)
        except Exception as e:
             test_table.add_row(["Zero no of sides:", "N=0,L=4",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.sides_length(2,8)
        except Exception as e:
             test_table.add_row(["2 sides:", "N=2,L=8",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.sides_length('abhishek',8)
        except Exception as e:
            test_table.add_row(["String input:", "N='abhishek',L=8",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.sides_length(-3,5)
        except Exception as e:
             test_table.add_row(["Negative input:", "N=-3,L=5",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.sides_length(6,0)
        except Exception as e:
            test_table.add_row(["Length of side:0", "N=6,L=0",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.sides_length(5,'a')
        except Exception as e:
            test_table.add_row(["Character input:", "N=5,L='a'",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.sides_length(5,-44)
        except Exception as e:
             test_table.add_row(["Negative length of side:", "N=5,L=-44",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.sides_length(6,10)
            test_table.add_row(["Valid input", "N=6,L=10",valid + self.print_features(features) + endc])
        except Exception as e:
             test_table.add_row(["Failed!", "N=6,L=10", invalid + str(e) + endc])
        print(test_table)
        return

    def testing_using_interior_angle(self):
        test_table = PrettyTable([blue + "TEST_CASE"+ endc, blue + "arguments" + endc,blue + "Output" + endc])
        test_table.align = 'l'

        p1 = polygon()
        try:
            p1.use_interior_angle(190,3)
        except Exception as e:
            test_table.add_row(["Interior angle beyond 180\u00b0:", "measure=190\u00b0,side=3",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            p1.use_interior_angle(0,4)
        except Exception as e:
            test_table.add_row(["Zero input:", "measure=0\u00b0,side=4",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            p1.use_interior_angle(-12,8)
        except Exception as e:
            test_table.add_row(["Negative input:", "measure=-12\u00b0,side=3",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            p1.use_interior_angle('string',6)
        except Exception as e:
            test_table.add_row(["string input:", "measure='string',side=8",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            p1.use_interior_angle(120,0)
        except Exception as e:
            test_table.add_row(["length of side(zero):", "measure=120\u00b0,side=0",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            p1.use_interior_angle(90,-2)
        except Exception as e:
           test_table.add_row(["Negative length of side:", "measure=90\u00b0,side=-2",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            p1.use_interior_angle(72,5)
        except Exception as e:
            test_table.add_row(["Invalid interior angle:", "measure=72\u00b0,side=5",invalid + str(e) + endc])
        test_table.add_row(['','',''])  
        try:
            features=p1.use_interior_angle(108,6)
            test_table.add_row(["Valid input:", "measure=108\u00b0,side=6",valid + self.print_features(features) + endc])
        except Exception as e:
            test_table.add_row(["Invalid input:", "measure=108,side=6",invalid + str(e) + endc])
        try:
            features=p1.use_interior_angle(144,12)
            test_table.add_row(["Valid input:", "measure=108\u00b0,side=6", valid + self.print_features(features) + endc])
        except Exception as e:
            test_table.add_row(["Invalid input:", "measure=108,side=6",invalid + str(e) + endc])
        
        print(test_table)
        return

    def testing_using_exterior_angle(self):
        p1 = polygon()
        test_table = PrettyTable([blue + "TEST_CASE"+ endc, blue + "arguments" + endc,blue + "Output" + endc])
        test_table.align = 'l'

        p1 = polygon()
        try:
            p1.use_exterior_angle(210,3)
        except Exception as e:
            test_table.add_row(["Exterior angle out of range:", "measure=210\u00b0,side=3",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            p1.use_exterior_angle(0,4)
        except Exception as e:
            test_table.add_row(["Zero input:", "measure=0\u00b0,side=4",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            p1.use_exterior_angle(-35,8)
        except Exception as e:
            test_table.add_row(["Negative input:", "measure=-35\u00b0,side=8",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            p1.use_exterior_angle('string11',6)
        except Exception as e:
            test_table.add_row(["string input:", "measure='string11',side=6",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            p1.use_exterior_angle(120,0)
        except Exception as e:
            test_table.add_row(["Zero input:", "measure=120\u00b0,side=0",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            p1.use_exterior_angle(60,-3)
        except Exception as e:
            test_table.add_row(["Negative input:", "measure=60\u00b0,side=-3",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features = p1.use_exterior_angle(90,5)
            test_table.add_row(["Valid input:", "measure=90\u00b0,side=5", valid + self.print_features(features) + endc])
        except Exception as e:
            test_table.add_row(["Invalid input:", "measure=90\u00b0,side=5",invalid + str(e) + endc])
        test_table.add_row(['','',''])    
        try:
            features=p1.use_exterior_angle(72,8)
            test_table.add_row(["Valid input:", "measure=72\u00b0,side=8",valid + self.print_features(features) + endc])
        except Exception as e:
            test_table.add_row(["Invalid input:", "measure=72,side=8",invalid + str(e) + endc])
        print(test_table)
        return

    def testing_using_irregular_polygon(self):
        test_table = PrettyTable([blue + "TEST_CASE"+ endc, blue + "arguments" + endc,blue + "Output" + endc])
        test_table.align = 'l'
        p1=polygon()
        try:
            features=p1.irregular_polygon(0,2,1)
        except Exception as e:
            test_table.add_row(["Zero input:", "sides are : 0,2,1",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.irregular_polygon(0,2)
        except Exception as e:
            test_table.add_row(["No_of_sides(2)input:", "sides are : 0, 2",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.irregular_polygon('a',2,2)
        except Exception as e:
            test_table.add_row(["Data type invalid:","sides are 'a',2,2",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.irregular_polygon(1,2,3)
        except Exception as e:
            test_table.add_row(["Not a Triangle:", "sides are 1 ,2 ,3",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.irregular_polygon(3,3,3)
            test_table.add_row(["Valid Input:", "N=3,3,3", valid + self.print_features_1(features) + endc])
        except Exception as e:
            test_table.add_row(["Invalid input:", "No=3,3,3",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.irregular_polygon(3,2,4)
            test_table.add_row(["Valid input:", "N=3,2,4", valid + self.print_features_1(features) + endc])
        except Exception as e:
            test_table.add_row(["Invalid input:", "sides are : 3,2,4",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.irregular_polygon(3,3,4)
            test_table.add_row(["Valid input:", "N=3,3,4", valid + self.print_features_1(features) + endc])
        except Exception as e:
            test_table.add_row(["Invalid input:", "sides are : 3,3,4",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.irregular_polygon(4,3,4,3)
            test_table.add_row(["Valid input:", "N=4,3,4,3", valid + self.print_features_1(features) + endc])
        except Exception as e:
            test_table.add_row(["Invalid input:", "sides are :4,3,4,3",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.irregular_polygon(4,4,4,4)
            test_table.add_row(["Valid input:", "N=4,4,4,4", valid + self.print_features_1(features) + endc])
        except Exception as e:
            test_table.add_row(["Invalid input:", "sides are :4,4,4,4",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        try:
            features=p1.irregular_polygon(4,-2,4,-2)
        except Exception as e:
            test_table.add_row(["Negative input:", "sides are :4,-2,4,-2",invalid + str(e) + endc])
        test_table.add_row(['','',''])
        print(test_table)


c = testing_polygon()
c.testing_using_sides()
c.testing_using_interior_angle()
c.testing_using_exterior_angle()
c.testing_using_irregular_polygon()
