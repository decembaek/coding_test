/*
https://school.programmers.co.kr/learn/courses/30/lessons/120909

문제 설명
어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ n ≤ 1,000,000
입출력 예
n	result
144	1
976	2
입출력 예 설명
입출력 예 #1

144는 12의 제곱이므로 제곱수입니다. 따라서 1을 return합니다.
입출력 예 #2

976은 제곱수가 아닙니다. 따라서 2를 return합니다.

*/

/*
check 한번 더 보기
제곱근 구하는 함수 Math.sqrt(double)
제곱 구하는 함수 Math.pow(double,double) => (밑수, 지수)

 */
class Solution {
    public int solution(int n) {
        int answer = 0;
        double num = Math.sqrt((double) n);

        if(num % 1 != 0) answer = 2;
        else answer = 1;
        return answer;
    }
}