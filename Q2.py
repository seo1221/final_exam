#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20222080 이름 : 윤서현

import os
import time

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):    # 해석을 편하게 하기 위해 솔루션 출력 값으로 carpediem이 나온다고 미리 가정하겠습니다.

    morse = {    # 모스부호 딕셔너리
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}

    answer = ''  # 해독 결과를 저장할 문자열을 초기화해준다.

    morse_key = letter.split()   #  모스부호는 공백으로 구분하므로, 공백을 기준으로 문자를 나눈다.
    # 가정한 값으로는, morse_key가 ['-.-.','.-','.-.','.--.','.','-..','..','.','--']로 나누어진다.

    for key in morse_key:   # 나누어진 문자 안의 key에 대해서 반복한다.
        answer += morse[key]   # key에 맞는 value 값(알파벳)을 answer에 넣는다.
        # 가정한 값으로는, key가 '-.-.'인 value값은 'c', '.-'는 'a', '.-.'는 'r'... 해당 과정을 반복해 carpediem이 된다.
    return answer   # 결과를 저장한 문자열을 return 한다.

result = solution("-.-. .- .-. .--. . -.. .. . --") # 검증을 위해 변수 result을 선언해 함수를 사용한다.
print(result)  # 확인을 위해 result 값을 프린트, carpe diem이 출력되어야 한다.
