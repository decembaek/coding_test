"""
https://school.programmers.co.kr/learn/courses/30/lessons/181908
프로그래머스 Lv.0

제목 : 접미사인지 확인하기
"""


# decembaek 풀이
def solution(my_string, is_suffix):
    for i in range(0, len(my_string)):
        if my_string[i:] == is_suffix:
            return 1
    return 0


# 다른사람
def solution(m, s):
    if m[-len(s) :] == s:
        return 1
    return 0
