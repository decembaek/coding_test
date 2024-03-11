"""
https://school.programmers.co.kr/learn/courses/30/lessons/181884
프로그래머스 Lv.0

제목 : n보다 커질 때까지 더하기

"""


# decembaek 풀이
def solution(numbers, n):
    answer = 0
    for num in numbers:
        answer += num
        if answer > n:
            return answer


# 다른사람 풀이
def solution(numbers, n):
    return next(
        sum(numbers[: i + 1]) for i in range(len(numbers)) if sum(numbers[: i + 1]) > n
    )
