"""
https://school.programmers.co.kr/learn/courses/30/lessons/181896
프로그래머스 Lv.0

제목 : 첫 번째로 나오는 음수

"""


# decembaek 풀이
def solution(num_list):
    for idx, num in enumerate(num_list):
        if num < 0:
            return idx
    return -1


# 다른사람
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1


# 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
