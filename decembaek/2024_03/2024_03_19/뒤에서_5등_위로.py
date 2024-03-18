"""
https://school.programmers.co.kr/learn/courses/30/lessons/181852
프로그래머스 Lv.0

제목 : 뒤에서 5등 위로
"""


# decembaek 풀이
def solution(num_list):
    sorted_list = sorted(num_list)
    result = sorted_list[5:]
    return result


# 다른사람
def solution(num_list):
    return sorted(num_list)[5:]
