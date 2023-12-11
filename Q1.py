#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20222080 이름 : 윤서현

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_strung, target):

    str1 = my_strung             # 변수 str1을 my_strung로 선언한다.
    str2 = target                # 변수 str2을 target으로 선언한다.

    if str2 in str1:             # my_strung 안에 target이 있는지 확인하기 위한 조건문
        return 1                 # 있다면(참이면) 1을 return한다.
    else:                        # 다른 경우
        return 0                 # 없다면(거짓이면) 0을 return한다.
    
result1 = solution("hello world", "hello")  # 검증을 위해 변수 result1을 선언해 함수를 사용한다.
result2 = solution("hello world", "hi")     # 검증을 위해 변수 result2을 선언해 함수를 사용힌디.
print(result1)  # 확인을 위해 result1 값을 프린트, 1가 출력되어야 한다.
print(result2)  # 확인을 위해 result2 값을 프린트, 0가 출력되어야 한다.

