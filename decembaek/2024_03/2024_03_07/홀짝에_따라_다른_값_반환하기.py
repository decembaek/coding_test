"""
https://school.programmers.co.kr/learn/courses/30/lessons/181935
프로그래머스 Lv.0

제목 : 홀짝에 따라 다른 값 반환하기

"""


# 풀이 시작
def solution(n):
    answer = 0
    return answer


# decembaek 풀이
def solution(n):
    answer = 0
    if n % 2 == 0:
        for i in range(0, n + 1):
            if i % 2 == 0:
                answer += i**2
    else:
        for i in range(0, n + 1):
            if i % 2 != 0:
                answer += i
    return answer


# 다른사람 풀이
def solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)


def solution(n):
    if n % 2:
        return sum(range(1, n + 1, 2))
    return sum([i * i for i in range(2, n + 1, 2)])
