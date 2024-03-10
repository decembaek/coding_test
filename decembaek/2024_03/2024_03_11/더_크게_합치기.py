"""
https://school.programmers.co.kr/learn/courses/30/lessons/181939
프로그래머스 Lv.0

제목 : 더 크게 합치기

"""


# decembaek 풀이(대만족)
def solution(a, b):
    _a = int(str(a) + str(b))
    _b = int(str(b) + str(a))
    return _a if _a > _b else _b


# 다른사람 풀이
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))


def solution(a, b):
    a, b = str(a), str(b)
    return int(max(a + b, b + a))
