"""
https://school.programmers.co.kr/learn/courses/30/lessons/181843
프로그래머스 Lv.0

제목 : 부분 문자열인지 확인하기

"""


# decembaek 풀이(대만족)
def solution(my_string, target):
    return 1 if target in my_string else 0


# 다른사람 풀이
def solution(my_string, target):
    return int(target in my_string)
