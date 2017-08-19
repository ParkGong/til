def get_rawdata_from_(filename):


    '''get_rawdata_from_(filename) -> dict of rawdata
    엑셀에서 raw데이터를 불러와서 딕셔너리를 반환한다.'''
    wb = load_workbook('filename')
    ws = wb.active

    raw_data = {}

    g = ws.rows

    for c1, c2 in g:
        raw_data.update({c1.value : c2.value})
    return raw_data


def scores_(scores):
    scores = []

    for score in raw_data.values():
        scores.append(score)
    return scores



def avrg_maker(scores)

    avrg = reduce(lambda a, b: a+b, scores)/len(scores)
    return avrg

def variance_maker(scores)

    variance = reduce(lambda a, b: a +b ,
                      map(lambda a :
                          (a - avrg)**2 ,scores)) / len(scores)

    return variance



def std_maker(variance)
    std_dev = round(math.sqrt(variance), 1)
    return std_dev

