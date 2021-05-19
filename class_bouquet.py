from copy import copy
from itertools import permutations

class bouquet():

    def __init__(self, formula_buquet) -> str:
        self.formula_buquet = formula_buquet
        self.final_subset=[]
        self.houses = 5
        self.normal_subset = self.__aux_all_sum(int(formula_buquet[-1]))
        for i in self.normal_subset:
            if len(i) == self.houses:
                self.final_subset.append(list(set(permutations(i))))

    def design_name(self):
        design_name = self.formula_buquet[0]
        return design_name

    def size(self):
        bouquet_size = self.formula_buquet[1]
        return bouquet_size

    def max_size(self):
        last_char = self.formula_buquet[-1]
        return last_char

    def flowers(self):
        flowers = [self.formula_buquet[i:i+2] for i in range(2, len(self.formula_buquet)-2, 2)]
        return flowers
    
    def __recursive_all_sum(self,target, current_sum, start, output, result):
     if current_sum == target:
       output.append(copy(self.result))
     for i in range(start, target):
       temp_sum = current_sum + i
       if temp_sum <= target:
         self.result.append(i)
         self.__recursive_all_sum(target, temp_sum, i, output, result)
         self.result.pop()
       else:
         return

    def __aux_all_sum(self,target):
        self.output = []
        self.result = []
        self.__recursive_all_sum(target, 0, 1, self.output, self.result)
        return self.output

    def combination(self):
        return self.final_subset

obj=bouquet("AS2a2b3c1d2e9")
print(obj.design_name())
print(obj.size())
print(obj.max_size())
print(obj.flowers())
print(obj.combination())