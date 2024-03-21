"""
https://school.programmers.co.kr/learn/courses/30/lessons/181928
프로그래머스 Lv.0

제목 : 이어 붙인 수
"""


# decembaek 풀이
def solution(num_list):
    a = ""
    b = ""
    for num in num_list:
        if num % 2 == 0:
            a += str(num)
        else:
            b += str(num)
    return int(a) + int(b)


# 다른사람
