"""
https://school.programmers.co.kr/learn/courses/30/lessons/120818?language=python3


문제 설명
머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

제한사항
10 ≤ price ≤ 1,000,000
price는 10원 단위로(1의 자리가 0) 주어집니다.
소수점 이하를 버린 정수를 return합니다.
입출력 예
price	result
150,000	142,500
580,000	464,000
입출력 예 설명
입출력 예 #1

150,000원에서 5%를 할인한 142,500원을 return 합니다.
입출력 예 #2

580,000원에서 20%를 할인한 464,000원을 return 합니다.
"""

def solution(price):
    if price>=500000:
        price = price *0.8
    elif price>=300000:
        price = price *0.9
    elif price>=100000:
        price = price * 0.95
    return int(price)