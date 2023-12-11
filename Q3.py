#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20222080 이름 : 윤서현

import os
import time

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):

    answer = []   # 결과를 저장할 리스트를 초기화한다.

    for i in str(age):   # 내장 함수 str을 통해 age를 문자열로 변경하고 각 자리의 숫자(i)에 대해 반복한다.
        answer += chr(ord('a') + int(i))    
        # 내장 함수 ord와 chr, int를 이용해 각 숫자에 대해 알파벳으로 변경하여 결과에 올린다.
        # 예를 들어 자릿수가 2라면 ord('a')+int(2) = 99가 되고, chr(99)는 'c'가 리턴된다.
        # ord('a') 대신 97를 쓰는 것도 가능하다.

    return ''.join(answer)  # 총 결과를 문자열로 return 한다.

result1 = solution(22)    # 검증을 위해 변수 result1을 선언해 함수를 사용한다.
result2 = solution(857)   # 검증을 위해 변수 result2을 선언해 함수를 사용힌디.
print(result1)   # 확인을 위해 result1 값을 프린트, cc가 출력되어야 한다.
print(result2)   # 확인을 위해 result2 값을 프린트, ifh가 출력되어야 한다.

