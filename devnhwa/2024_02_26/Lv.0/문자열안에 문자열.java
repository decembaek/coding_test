/*
https://school.programmers.co.kr/learn/courses/30/lessons/120908
문제 설명
문자열 str1, str2가 매개변수로 주어집니다. str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ str1의 길이 ≤ 100
1 ≤ str2의 길이 ≤ 100
문자열은 알파벳 대문자, 소문자, 숫자로 구성되어 있습니다.
입출력 예
str1	str2	result
"ab6CDE443fgh22iJKlmn1o"	"6CD"	1
"ppprrrogrammers"	"pppp"	2
"AbcAbcA"	"AAA"	2
입출력 예 설명
입출력 예 #1

"ab6CDE443fgh22iJKlmn1o" str1에 str2가 존재하므로 1을 return합니다.
입출력 예 #2
aba55 5
abc 3

"ppprrrogrammers" str1에 str2가 없으므로 2를 return합니다.
입출력 예 #3

"AbcAbcA" str1에 str2가 없으므로 2를 return합니다.
*/
class Solution {
    public int solution(String str1, String str2) {
        int answer = 2;
        if(str1.length() >= str2.length()){
            for(int i = 0; i <= str1.length() - str2.length(); i++){
                if(str1.substring(i, (str2.length()+i)).equals(str2)) answer = 1;
            }
        }else{
            answer = 2;
        }

        return answer;
    }
}

// !! 한번 틀림 => substring(strIdx, endIndex)
// strIdx 포함, endIdx 안포함 => String A = 'ABCD'
// substring(0,2) = 'AB'
