"""
https://school.programmers.co.kr/learn/courses/30/lessons/181840
프로그래머스 Lv.0

제목 : 정수 찾기
"""


# decembaek 풀이
def solution(num_list, n):
    return 1 if n in num_list else 0


# 다른사람
def solution(num_list, n):
    return int(n in num_list)
