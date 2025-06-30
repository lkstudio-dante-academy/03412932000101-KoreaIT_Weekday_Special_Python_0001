import os
import sys

"""
Python 연습 문제 8
- 홀/짝수 구분하기
- 정해진 개수만큼 수를 입력 받는다
- 입력 받은 수가 홀수 일 경우 왼쪽부터 채워나간다
- 입력 받은 수가 짝수 일 경우 오른쪽부터 채워나간다

Ex)
개수 입력 : 5

1 번째 정수 입력 : 1
2 번째 정수 입력 : 2
3 번째 정수 입력 : 3
4 번째 정수 입력 : 4
5 번째 정수 입력 : 5

=====> 결과 <=====
1, 3, 5, 4, 2
"""


# Training 8
def start(args):
	nNumValues = int(input("개수 입력 : "))
	oListValues = [0] * nNumValues
