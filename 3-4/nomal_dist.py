#정규분포 관련 함수 라이브러리
#함수 3개 평균 , 분산 , 표준편차

import math
from functools import reduce


class NormDist:


    def average(self, scores):
        return reduce(
            lambda a, b:
            a + b,
            scores)/len(scores)

    def variance(self, scores, avrg):
        return round(
            reduce(
            lambda a, b:
            a + b,
            map(
                lambda s:
                (s-avrg)**2,
                scores))/len(scores),
                     1)

    def std_dev(self, variance):
        return round(
            math.sqrt(variance),
            1)


if __name__ == '__main__':

    li = [1,2,3,4,5]

    nd = NormDist()
    print(nd.average(li))
    av = nd.average(li)
    va = nd.variance(li,av)
    st = nd.std_dev(va)
