from copy import copy
from itertools import permutations

def recursive_all_sum(target, current_sum, start, output, result):
 if current_sum == target:
   output.append(copy(result))
 for i in range(start, target):
   temp_sum = current_sum + i
   if temp_sum <= target:
     result.append(i)
     recursive_all_sum(target, temp_sum, i, output, result)
     result.pop()
   else:
     return

def aux_all_sum(target):
   output = []
   result = []
   recursive_all_sum(target, 0, 1, output, result)
   #print(output)
   return output

normal_subset = aux_all_sum(3)
final_subset=[]
houses = 2

for i in normal_subset:
    if len(i) == houses:
        final_subset.append(list(set(permutations(i))))
        #final_subset2=final_subset[0]

print(final_subset)
