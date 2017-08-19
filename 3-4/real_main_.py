from data_handler import *


dh = DataHandler('class_1.xlsx', '3-4')

dh.get_average()
dh.get_variance()
dh.get_std_dev()
print(dh.get_average())
print(dh.get_variance())
print(dh.get_std_dev())


print(dh.who_is_highest())
print(dh.get_highest_score())


print(dh.cache)

dh.GetEvaluation(50)


