"""
https://school.programmers.co.kr/learn/courses/30/lessons/181842
프로그래머스 Lv.0

제목 : 부분 문자열

"""


# decembaek 풀이(대만족)
def solution(str1, str2):
    return 1 if str1 in str2 else 0


# 다른사람 풀이
def solution(str1, str2):
    return int(str1 in str2)
