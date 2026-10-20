# def score(*args):
#     return sum(args)/len(args)

#**kwargs => 딕셔너리로 반환
def score(**kwargs):
    total = 0

    for subject, score in kwargs.items():
        total += score

    return total / len(kwargs)