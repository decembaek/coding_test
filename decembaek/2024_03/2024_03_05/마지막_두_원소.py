"""
https://school.programmers.co.kr/learn/courses/30/lessons/181927

프로그래머스 Lv.0

제목 : 마지막 두 원소
"""


# 풀이 시작
def solution(num_list):
    answer = []
    return answer


# decembaek 풀이
def solution(num_list):
    last = num_list[-1]
    last_second = num_list[-2]
    if last > last_second:
        num_list.append(last - last_second)
        return num_list
    else:
        num_list.append(last * 2)
        return num_list


# 다른사람 풀이
def solution(l):
    l.append(l[-1] - l[-2] if l[-1] > l[-2] else l[-1] * 2)
    return l


def solution(num_list):
    a = num_list[-1]
    b = num_list[-2]
    if a > b:
        num_list.append(a - b)
    else:
        num_list.append(2 * a)
    return num_list
