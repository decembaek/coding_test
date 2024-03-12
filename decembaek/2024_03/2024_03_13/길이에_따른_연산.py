"""
https://school.programmers.co.kr/learn/courses/30/lessons/181879
프로그래머스 Lv.0

제목 : 길이에 따른 연산

"""

# decembaek 풀이
import math


def solution(num_list):
    answer = 1
    return sum(num_list) if len(num_list) >= 11 else math.prod(num_list)


# 다른사람
def solution(num_list):
    if len(num_list) >= 11:
        return eval("+".join(list(map(str, num_list))))
    else:
        return eval("*".join(list(map(str, num_list))))
