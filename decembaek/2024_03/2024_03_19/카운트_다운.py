"""
https://school.programmers.co.kr/learn/courses/30/lessons/181899
프로그래머스 Lv.0

제목 : 카운트 다운
"""


# decembaek 풀이
def solution(start, end_num):
    num = start - end_num
    answer = []
    for i in range(0, num + 1):
        answer.append(start - i)
    return answer


# 다른사람
def solution(start, end):
    return list(range(start, end - 1, -1))
