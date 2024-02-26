/*
https://school.programmers.co.kr/learn/courses/30/lessons/120822

문제 설명
문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ my_string의 길이 ≤ 1,000
입출력 예
my_string	return
"jaron"	"noraj"
"bread"	"daerb"
입출력 예 설명
입출력 예 #1

my_string이 "jaron"이므로 거꾸로 뒤집은 "noraj"를 return합니다.
입출력 예 #2

my_string이 "bread"이므로 거꾸로 뒤집은 "daerb"를 return합니다.
*/
class Solution {
    public String solution(String my_string) {
        String answer = "";
        char[] charList = new char[my_string.length()];

        for(int i=0; i< charList.length; i++){
            charList[charList.length-i-1] = my_string.charAt(i);
        }
        for(char char_my : charList){
            answer = answer + char_my;
        }

        return answer;
    }
    // 더 줄일 수 있어보여 줄임.
    public String solution(String my_string) {
        String answer = "";

        for(int i= my_string.length()-1; i>=0; i--){
            answer = answer + my_string.charAt(i);
        }

        return answer;
    }


}