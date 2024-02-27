/*
https://school.programmers.co.kr/learn/courses/30/lessons/120813

문제 설명
정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ n ≤ 100
입출력 예
n	result
10	[1, 3, 5, 7, 9]
15	[1, 3, 5, 7, 9, 11, 13, 15]
입출력 예 설명
입출력 #1

10 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9]를 return합니다.
입출력 #1

15 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9, 11, 13, 15]를 return합니다.
 */
class Solution {
    public int[] solution(int n) {
        int count = 0;
        if(n % 2 == 0) count = n / 2;
        else count = n / 2 + 1;
        int[] answer = new int[count];
        for(int i=1; i<=count; i++){
            answer[i-1] = 1+ 2 * (i-1);
        }
        return answer;
    }
}