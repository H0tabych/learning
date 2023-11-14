import random

len_list: int = 3

rand_list = tuple(random.randint(-100, 100) for i in range(len_list))

print(rand_list)
print(max(rand_list))
