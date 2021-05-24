import re

class bouquet():

    """
    A class(input::string) used to represent an flower bouquet
    input="<"A"-"Z"><"L","S"><<1-9><"a"-"z">>...<1-99>"
    ...

    Methods
    -------
    design_name()
        Set name of the bouquet from string::buq_formula
        Output: "A".."Z"

    size()
        Set size of the bouquet from string::buq_formula
        Output: "S","L"
    
    max_size()
        Set max size of the bouquet from string::buq_formula
        Output: 1..9
    
    flowers()
    Set flowers of the bouquet from string::buq_formula
    Output: {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    """

    def __init__(self, formula_bouquet) -> str:
        self.formula_bouquet = formula_bouquet

    def design_name(self):
        design_name = self.formula_bouquet[0]
        return design_name

    def size(self):
        bouquet_size = self.formula_bouquet[1]
        return bouquet_size

    def max_size(self):
        if  self.formula_bouquet[-2].isnumeric():
            last_char = self.formula_bouquet[-2:]
        else:
            last_char = self.formula_bouquet[-1]
        return last_char

    def flowers(self):
        flowers = {}
        size = self.size()
        var = 0
        for i in self.formula_bouquet[2:]:
            if i.isalpha():
                flowers[i+size]=int(var)
                var = 0
            else:
                var+= int(i)
        return flowers

#Class create for coloring the terminal, should work on all ANSI/VT100 terminals
class colors:
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'

#redu(adds::int)
#Reduce the flower formula, check if max::int value is equal or smaller then the value needed adds::int, if so interate to fill final::dict
def redu(adds):
     if adds >= max:
        sume= adds-max
        for x in final:
            for y in list(final)[1:]:
                if final[x]>1 and all_flowers[y]-1 > 0 or x == y :
                    final[x]-= 1
                    sume-= 1
            if sume == 0:
                return
        redu(adds-1) 

#Prepare the pretty print with the last check, distributing the flowers to empty slots
def check_complete():
    pprint=''
    look_fail=flower.flowers()
    for  flow in look_fail:
        if flow in final:
            pass
        else:
            return ""
    for flow in final:
        if final[flow] == 0:
            zero_place=flow
            for alter in final:
                if final[alter] > 2:
                    final[alter]-= 1
                    final[zero_place]+= 1
    for flow in final:
        pprint+=str(final[flow]) + flow[0]
    for y in all_flowers:
        if y in final:
            all_flowers[y]-= final[y]    
    return pprint

all_buq_formula = [] #create var all_buq_formula::all_flowers for all flowers buquet inputs
all_flowers = {} #create var all_flower::dictionary to store all flowers in stock


#BOUQUET FORMULA INPUT
while True:
    buq_formula = input(f"{colors.BLUE}Enter the bouquet formula: {colors.ENDC}") 
    if buq_formula == "" and len(all_buq_formula) > 0 : #if inputI/O::string == ""::string, break the BUQUET FORMULA INPUT (if input is empty it has reach the end of the bouquet formula input,break the while)
        break             
    else:
        if re.match(r"\A[A-Z][L,S]([0-9]+[a-z])+[1-9]\d{0,1}\Z", buq_formula):
            all_buq_formula.append(bouquet(buq_formula))#else append inputI/O::string to all_buq_formula::all_flowers (all_buq_formula is where all bouquet formulas are stored)
        else:
            print(f"{colors.RED}Wrong buquet formula input format !{colors.ENDC}")    


#FLOWERS INPUT
while True:
    flower_formula = input(f"{colors.GREEN}Enter flowers: {colors.ENDC}")
    if flower_formula == "" and len(all_flowers) > 0 : #if inputI/O::string == ""::string, break the BUQUET FORMULA INPUT (if input is empty it has reach the end of the bouquet formula input,break the while)
        break
    if re.match(r"[a-z][L,S]$",flower_formula):
        if flower_formula in all_flowers:
            all_flowers[flower_formula]+= 1
        else:
            all_flowers[flower_formula]= 1
    else:
        print(f"{colors.RED}Wrong flower input format !{colors.ENDC}") 


#MAIN INTERATION WITH OBJECTS
for flower in all_buq_formula * 10:
    name = flower.design_name()#name::string = flower.design.name()::string
    size_of = flower.size()#size_of ::string = flower.size()::string
    one_set = flower.flowers()#one_set::dictionary = flower.flowers()::dictionary
    max = int(flower.max_size())#max::int = flower.max_size()::string
    adds = 0
    final = {}#creating 
    for buqu in one_set:
        if buqu in all_flowers:
            if all_flowers[buqu] >= 1:
                final[buqu]=one_set[buqu]               
    for summing in final:
        adds+= final[summing]
    redu(adds)
    response=check_complete()
    if response != "":
        print(colors.BLUE,"BOUQUET FOUND ---> ", name,size_of,response, colors.ENDC,sep = "")

# import unittest
# from unittest import mock
 
# class Test_bloomon(unittest.TestCase):
 

    # @mock.patch(f'{__name__}1.foo', autospec=True, side_effect=bouquet("AS2a2b3"))
    # def test_foo_return_and_local_params_values(self, mocked):
        # self.assertEqual('A', mocked.side_effect.design_name) #PASS
        # self.assertEqual("S", mocked.side_effect.size) #PASS
        # self.assertEqual(3, mocked.side_effect.max_size) #PASS 
        # self.assertEqual({'a':2,'b':2}, mocked.side_effect.flowers) #PASS

    # @mock.patch(f'{__name__}2.foo', autospec=True, side_effect=bouquet("BL2a2"))
    # def test_foo_return_and_local_params_values(self, mocked):
        # self.assertEqual('B', mocked.side_effect.design_name) #PASS
        # self.assertEqual("L", mocked.side_effect.size) #PASS
        # self.assertEqual(2, mocked.side_effect.max_size) #PASS 
        # self.assertEqual({'a':2}, mocked.side_effect.flowers) #PASS

    # @mock.patch(f'{__name__}3.foo', autospec=True, side_effect=bouquet("CL2a2b3f4g5q2"))
    # def test_foo_return_and_local_params_values(self, mocked):
        # self.assertEqual('C', mocked.side_effect.design_name) #PASS
        # self.assertEqual("L", mocked.side_effect.size) #PASS
        # self.assertEqual(2, mocked.side_effect.max_size) #PASS 
        # self.assertEqual({'a':2,'b':3,'f':3,'g':4,'q':5}, mocked.side_effect.flowers) #PASS


    # def TEST_check_complete(self):
        #type(self).max = 3
        #type(self).final={'as':2,'bs':2}
        # self.assertEqual(redu(4),type(self).final={'as':1,'bs':2}) #PASS

        #type(self).max = 2
        #type(self).final={'as':2,'bs':2}
        # self.assertEqual(redu(4),type(self).final={'as':1,'bs':1}) #PASS

        #type(self).max = 3
        #type(self).final={'as':2,'bs':2}
        # self.assertEqual(redu(3),type(self).final={'as':1,'bs':1}) #PASS

        #type(self).max = 4
        #type(self).final={'as':2,'bs':2}
        # self.assertEqual(redu(3),type(self).final={'as':2,'bs':2}) #PASS

        #type(self).max = 5
        #type(self).final={'as':2,'bs':2}
        # self.assertEqual(redu(5),type(self).final={}) #PASS
        
        #type(self).max = 1
        #type(self).final={'as':1}
        # self.assertEqual(redu(5),type(self).final={'as':1,'bs':1}) #PASS