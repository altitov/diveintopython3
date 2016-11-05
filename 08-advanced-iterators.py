import re
import itertools


a_string = "The sixth sick sheikh's sixth sheep's sick"
occ = re.findall(' s.*? s', a_string)
a_list = a_string.split(' ')
print(a_list)
print(set(a_list))
print(set(a_list[1]))

assert 1 + 1 == 2

print(ord('c'))

list(itertools.permutations(['ACB'], 3))