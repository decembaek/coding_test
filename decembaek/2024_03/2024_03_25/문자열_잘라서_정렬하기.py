"""
https://school.programmers.co.kr/learn/courses/30/lessons/181866
프로그래머스 Lv.0

제목 : 문자열 잘라서 정렬하기
"""


# decembaek 풀이ㅂ
def solution(myString):
    split_strings = [s for s in myString.split("x") if s != ""]
    sorted_strings = sorted(split_strings)
    return sorted_strings


# 다른사람
def solution(myString):
    return sorted(ch for ch in myString.split("x") if ch)
