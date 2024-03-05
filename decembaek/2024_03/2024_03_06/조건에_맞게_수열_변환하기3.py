"""
https://school.programmers.co.kr/learn/courses/30/lessons/181835
프로그래머스 Lv.0

제목 : 조건에 맞게 수열 변환하기 3

"""


# 풀이 시작
def solution(arr, k):
    answer = []
    return answer


# decembaek 풀이
def solution(arr, k):
    answer = []
    if k % 2 == 0:
        for v in arr:
            answer.append(v + k)
    else:
        for v in arr:
            answer.append(v * k)
    return answer


# 다른사람 풀이
def solution(arr, k):
    return [i * k if k % 2 != 0 else i + k for i in arr]
