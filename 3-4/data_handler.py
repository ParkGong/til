#반 성적을 가져와서
#연고나된 모든 연산
#이 연산한 결과를 cashing
#NormDist : 객체를 상속할 것인가?
#inheritance: IS-A
#합성할 것인가?
#composition : HAS-A

#class method로 만들까
#아니면 intance method로 만들까

from nomal_dist import *
import openpyxl
from functools import reduce


class DataHandler:
    evaluator = NormDist()

    @classmethod
    def get_data_from_excel(cls, filename):
        '''
        get_data_from_excel(filename) -> {'name1' : 'score1', 'name2' : 'score2', ....}
        엑셀 파일에서 데이터를 가져옵니다.
        반환 값은 key가 학생 이름이고 value가 점수인 딕셔너리입니다. 
        '''
        dic = {}
        wb = openpyxl.load_workbook(filename)
        ws = wb.active
        g = ws.rows

        for name, score in g:
            dic[name.value] = score.value

        print(dic)
        return dic
    
    def __init__(self, filename, clsname):
        self.rawdata = DataHandler.get_data_from_excel(filename)
        self.clsname = clsname
        #가져온 데이터랑
        #필요할때마다 연산된
        #데이터 결과값을 저장해 두는 역할
        self.cache = {}

    #캐시 이용법
    def get_scores(self):
        if 'scores' not in self.cache:
            self.cache['scores'] = \
                list(self.rawdata.values())

        return self.cache['scores']

    def get_average(self):
        if 'average' not in self.cache:
            avrg = self.evaluator.average(
                self.get_scores())
            self.cache['average'] = avrg

        return self.cache['average']

    def get_variance(self):
        if 'variance' not in self.cache:
            va = self.evaluator.variance(
                self.get_scores(),self.get_average())
            self.cache['variance'] = va
            
        return self.cache['variance']

    def get_std_dev(self):
        if 'std_dev' not in self.cache:
            dev = self.evaluator.std_dev(
                self.get_variance())
            self.cache['std_dev'] = dev

        return self.cache['std_dev']
    

    def who_is_highest(self):
        
        if 'highest' not in self.cache:
            high = reduce(lambda a, b:
                          a if self.rawdata.get(a) > self.rawdata.get(b) else b,
                          self.rawdata.keys())
            self.cache['highest'] = high
            
        return self.cache.get('highest')
                

    def get_highest_score(self):
        return self.rawdata[self.who_is_highest()]


    def who_is_lowest(self):
        if 'lowest' not in self.cache:
            high = reduce(lambda a, b:
                          a if self.rawdata.get(a) < self.rawdata.get(b) else b,
                          self.rawdata.keys())
            self.cache['lowest'] = high   
        return self.cache.get('lowest')


        
    def get_lowest_score(self):
        return self.rawdata[self.who_is_lowest()]


    def GetEvaluation(self, total_avrg):
        print('*' * 50)
        print("%s 반 성적 분석 결과" % self.clsname)
        print(
        "{0}반의 평균은 {1}점이고 분산은 {2}이며,따라서 표준편차는{3}이다".format(
            self.clsname,
            self.get_average(),
            self.get_variance(),
            self.get_std_dev()))
        print('*' * 50)
        print("%s 반 종합 평가" % self.clsname)
        print('*' * 50)
        self.evaluateClass(total_avrg)

    def evaluateClass(self, total_avrg):
        avrg = self.get_average()
        std_dev = self.get_std_dev()
        
        if avrg <total_avrg and std_dev >20:
            print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
        elif avrg > total_avrg and std_dev >20:
            print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
        elif avrg < total_avrg and std_dev <20:
            print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
        elif avrg > total_avrg and std_dev <20:
            print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")
