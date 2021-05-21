class bouquet():

    def __init__(self, formula_bouquet) -> str:
        self.formula_bouquet = formula_bouquet
        self.summ=0
        self.flowers_control={}

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
        flowers = {self.formula_bouquet[i+1]+self.size() :int(self.formula_bouquet[i]) for i in range(2, len(self.formula_bouquet)-2, 2)}
        return flowers
    
    def summatory(self,summatory="empty") -> int:
        if summatory == 0:
            self.summ=0
        elif str(summatory).isnumeric():
            self.summ+=summatory
        return self.summ

    def flowers_used(self, value= "empty") -> str:
        if value == 0:
            self.flowers_control.clear()
        elif value == "empty":
            return self.flowers_control
        elif value in self.flowers_control:
            self.flowers_control[value]+=1
        else:
            self.flowers_control[value]=1

def process():

    for flower in all_buq_formula:
        flower.summatory(0)
        flower.flowers_used()
        one_set=flower.flowers()
        big_size= flower.max_size()
        for dic_key in one_set:
            if dic_key in all_flowers:
                if all_flowers[dic_key] >= one_set[dic_key]:
                    flower.summatory(int(one_set[dic_key]))
                    flower.flowers_used(dic_key)
                else:
                    flower.summatory(int(all_flowers[dic_key]))
                if flower.summatory() == int(big_size):
                    flower_summary=flower.flowers_used()
                    for end_list in flower_summary:
                        all_flowers[end_list]-= flower_summary[end_list]
                    flower.summatory(0)
                    flower.flowers_used(0)


    return

all_buq_formula = [] #create global var all_buq_formula::list for all flowers buquet inputs
all_flowers = {} #create global var all_flower::dictionary to store all flowers in stock

#BOUQUET FORMULA INPUT
while True:
    buq_formula = input("Enter the bouquet formula: ") 
    if buq_formula == "": #if inputI/O::string == ""::string, break the BUQUET FORMULA INPUT (if input is empty it has reach the end of the bouquet formula input,break the while)
        break             
    else:
        all_buq_formula.append(bouquet(buq_formula))#else append inputI/O::string to all_buq_formula::list (all_buq_formula is where all bouquet formulas are stored)
#FLOWERS INPUT
while True:
    flower_formula = input("Enter flowers: ")
    if flower_formula in all_flowers:
        all_flowers[flower_formula] += 1
    else:
        all_flowers[flower_formula] = 1
    process()


