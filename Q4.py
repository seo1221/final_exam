#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20222080 이름 : 윤서현

import os
import time

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):

    answer = 0  # 원 사이의 점 개수를 카운트해줄 결과 변수를 0으로 초기화한다.

    for x in range(-r2, r2+1):  # 정수만을 반환해주는 특징이 있는 range 함수를 사용
        # x축을 표현하는 범위는 -r2부터 r2인데, 끝 숫자는 반환 범위에 포함하지 않는 range 특징을 고려해 
        # r2+1까지로 범위를 잡아주었다.
        for y in range(-r2, r2+1):
            # 위의 x축과 같이 y축을 표현하는 범위를 -r2부터 r2로 잡고, +1 해주었다.
            if r1**2 <= x**2 + y**2 <= r2**2:  # 원 공식, 두 원 사이 범위에 존재하는지에 대한 조건문
                answer += 1   # 두 원 사이 범위에 해당된다면 카운트를 올린다.

    return answer   # 총 결과를 return 한다.

result = solution(2, 3)   # 검증을 위해 변수 result을 선언해 함수를 사용한다.
print(result)   # 확인을 위해 result 값을 프린트, 20이 출력되어야 한다.
