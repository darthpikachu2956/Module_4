from fake_math import divide as div_f
from true_math import divide as div_t


result1 = div_f(10, 2)
result2 = div_f(11, 0)
result3 = div_t(20, 2)
result4 = div_t(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
