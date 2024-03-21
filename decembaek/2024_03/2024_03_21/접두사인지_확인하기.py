"""
https://school.programmers.co.kr/learn/courses/30/lessons/181906
프로그래머스 Lv.0

제목 : 접두사인지 확인하기
"""


# decembaek 풀이
def solution(my_string, is_prefix):
    for i in range(0, len(my_string)):
        if my_string[:i] == is_prefix:
            return 1
    return 0


# 다른사람
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))
