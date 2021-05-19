all_buq_formula = [] #create global object all_buq_formula::list for all flowers buquet
all_flowers = {}

#BOUQUET FORMULA INPUT
while True:
    buq_formula = input("Enter the bouquet formula: ") 
    if buq_formula == "": #if input::string == empty::string, break the BUQUET FORMULA INPUT
        break
    else:
        all_buq_formula.append(buq_formula) #add buq_formula::string to all_buq_formula::list
print(all_buq_formula)

#FLOWERS INPUT
while True:
    flower_formula = input("Enter flowers: ")
    if flower_formula in all_flowers:
        all_flowers[flower_formula] += 1
    else:
        all_flowers[flower_formula] = 1
    print (all_flowers)

