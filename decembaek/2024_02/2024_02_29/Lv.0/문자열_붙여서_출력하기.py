"""
https://school.programmers.co.kr/learn/courses/30/lessons/181946

프로그래머스 Lv.0

제목 : 문자열 붙여서 출력하기
"""

# 풀이 시작
str1, str2 = input().strip().split(" ")


# decembaek 풀이
str1, str2 = input().strip().split(" ")
print(str1 + str2)


# 다른사람 풀이
print(input().strip().replace(" ", ""))
