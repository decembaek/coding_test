"""
https://school.programmers.co.kr/learn/courses/30/lessons/181944

프로그래머스 Lv.0

제목 : 홀짝 구분하기


문제 설명:
자연수 n이 입력으로 주어졌을 때 
만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.

제한사항
1 ≤ n ≤ 1,000


입출력 예:

입력 #1
100

출력 #1
100 is even

입력 #2
1
출력 #2
1 is odd

"""

# 풀이 시작
a = int(input())


# decembaek 풀이
a = int(input())
if a % 2 == 0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")

# 다른 사람 풀이
n = int(input())
print(f"{n} is {'eovdedn'[n&1::2]}")

N = int(input())
print(f"{N} is {'even' if N % 2 == 0 else 'odd'}")
