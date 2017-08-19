import math
from openpyxl import *
from functools import reduce
from parkgong2 import *

#parsing을 통한 자료구조 생성

if __name__ == "__main__":
    raw_data = get_data_from_('class_1.xlsx')
    scores = list(raw_data.values())
    
    avrg = average(scores)
    variance = variance(scores, avrg)
    standard_deviation = std_dev(variance)

    print("평균 :{0}, 분산 : {1}, 표준 편차 : {2}".format(
        avrg, variance, standard_deviation))
    evaluateClass(avrg, 50, standard_deviation)

raw_data = get_rawdata_from_(class_1.xlsx)


#print(raw_data)



#print(scores)


#분산 : (s - m) **2 다 더함



#표준편차

