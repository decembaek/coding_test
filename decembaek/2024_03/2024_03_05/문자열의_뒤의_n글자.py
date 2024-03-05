"""
https://school.programmers.co.kr/learn/courses/30/lessons/181910

프로그래머스 Lv.0

제목 : 문자열의 뒤의 n 글자
"""


# 풀이 시작
def solution(my_string, n):
    answer = ""
    return answer


# decembaek 풀이 (만족)
def solution(my_string, n):
    return my_string[-n:]


# 다른사람 풀이
def solution(my_string, n):
    return my_string[-n:]


solution = lambda my_string, n: my_string[len(my_string) - n :]
