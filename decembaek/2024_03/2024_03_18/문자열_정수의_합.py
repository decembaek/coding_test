"""
https://school.programmers.co.kr/learn/courses/30/lessons/181849
프로그래머스 Lv.0

제목 : 문자열 정수의 합
"""


# decembaek 풀이
def solution(num_str):
    answer = 0
    for num in num_str:
        answer += int(num)
    return answer


# 다른사람
def solution(num_str):
    return sum(map(int, list(num_str)))
