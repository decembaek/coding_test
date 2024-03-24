"""
https://school.programmers.co.kr/learn/courses/30/lessons/181941
프로그래머스 Lv.0

제목 : 문자 리스트를 문자열로 변환하기
"""


# decembaek 풀이
def solution(arr):
    text = ""
    for s in arr:
        text += s
    return text


# 다른사람
def solution(arr):
    return "".join(arr)
