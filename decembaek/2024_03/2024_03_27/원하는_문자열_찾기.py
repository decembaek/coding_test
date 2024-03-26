"""
https://school.programmers.co.kr/learn/courses/30/lessons/181878
프로그래머스 Lv.0

제목 : 원하는 문자열 찾기
"""


# decembaek 풀이
def solution(myString, pat):
    return 1 if pat.lower() in myString.lower() else 0


# 다른사람
def solution(myString, pat):
    return int(pat.lower() in myString.lower())
