"""
https://school.programmers.co.kr/learn/courses/30/lessons/120903?language=python3
문제 설명
두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ s1, s2의 길이 ≤ 100
1 ≤ s1, s2의 원소의 길이 ≤ 10
s1과 s2의 원소는 알파벳 소문자로만 이루어져 있습니다
s1과 s2는 각각 중복된 원소를 갖지 않습니다.
입출력 예
s1	s2	result
["a", "b", "c"]	["com", "b", "d", "p", "c"]	2
["n", "omg"]	["m", "dot"]	0
입출력 예 설명
입출력 예 #1

"b"와 "c"가 같으므로 2를 return합니다.
입출력 예 #2

같은 원소가 없으므로 0을 return합니다.


"""

def solution(s1, s2):
    s1=set(s1)
    s2 =set (s2)
    return len(s1.intersection(s2))

"""
교집합
set1.intersection(set2)
합칩합
set1.union(set2)
차집합
set1.difference(set2)
https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EB%B9%84%EA%B5%90-%EA%B0%99%EC%9D%80%EA%B0%92-%EB%8B%A4%EB%A5%B8%EA%B0%92set%EC%9E%90%EB%A3%8C%ED%98%95%ED%95%A9%EC%A7%91%ED%95%A9%EA%B5%90%EC%A7%91%ED%95%A9%EC%B0%A8%EC%A7%91%ED%95%A9


"""