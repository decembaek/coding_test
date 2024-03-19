"""
https://school.programmers.co.kr/learn/courses/30/lessons/181891
프로그래머스 Lv.0

제목 : 순서 바꾸기
"""


# decembaek 풀이
def solution(num_list, n):
    first = num_list[:n]
    second = num_list[n:]
    return second + first


# 다른사람
def solution(num_list, n):
    if not isinstance(num_list, list):
        raise TypeError(num_list)
    if not isinstance(n, int):
        raise TypeError(n)

    if not (2 <= len(num_list) <= 30):
        raise ValueError(num_list)
    if not (1 <= n <= len(num_list)):
        raise ValueError(num_list, n)

    if not all(isinstance(num, int) for num in num_list):
        raise TypeError(num_list)
    if not all(1 <= num <= 9 for num in num_list):
        raise ValueError(num_list)

    return num_list[n:] + num_list[:n]
