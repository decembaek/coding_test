"""
https://school.programmers.co.kr/learn/courses/30/lessons/120803
프로그래머스 Lv.0

제목 : 두 수의 차

문제 설명
정수 num1과 num2가 주어질 때, num1에서 num2를 뺀 값을 return하도록 soltuion 함수를 완성해주세요.

제한사항
-50000 ≤ num1 ≤ 50000
-50000 ≤ num2 ≤ 50000

입출력 예
num1	num2	result
2	3	-1
100	2	98

"""

# 풀이
int solution(int num1, int num2) {
    int answer = 0;
    answer = num1 - num2;
    return answer;
}

"""
https://school.programmers.co.kr/learn/courses/30/lessons/120804

프로그래머스 Lv.0

제목 : 두 수의 곱

문제 설명
정수 num1, num2가 매개변수 주어집니다. num1과 num2를 곱한 값을 return 하도록 solution 함수를 완성해주세요.

제한사항
0 ≤ num1 ≤ 100
0 ≤ num2 ≤ 100
입출력 예
num1	num2	result
3	4	12
27	19	513

"""
# 문제 풀이
int solution(int num1, int num2) {
    int answer = 0;
    answer = num1 * num2;
    return answer;
}

"""
https://school.programmers.co.kr/learn/courses/30/lessons/120804
제목:: 두 수의 합

정수 num1과 num2가 주어질 때, num1과 num2의 합을 return하도록 soltuion 함수를 완성해주세요.

제한사항
-50,000 ≤ num1 ≤ 50,000
-50,000 ≤ num2 ≤ 50,000
입출력 예
num1	num2	result
2	3	5
100	2	102


"""

int solution(int num1, int num2) {
    int answer = 0;
    answer = num1 + num2;
    return answer;
}

"""
https://school.programmers.co.kr/learn/courses/30/lessons/120806

제목: 두 수의 나눗셈

문제 설명
정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수를 완성해주세요.

제한사항
0 < num1 ≤ 100
0 < num2 ≤ 100
입출력 예
num1	num2	result
3	2	1500
7	3	2333
1	16	62


"""

int solution(int num1, int num2) {
    int answer = 0;
    answer = ((float)num1 / num2) * 1000;
    return answer;
}