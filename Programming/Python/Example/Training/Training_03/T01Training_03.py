import os
import sys

"""
Python 연습 문제 3
- 범위 포함 여부 검사하기
- 정수를 입력 받아 1 ~ 100 사이에 포함 되는지 여부를 검사한다

Ex)
정수 입력 : 120
120 은 1 ~ 100 사이에 존재하지않습니다.
"""


# Training 3
def start(args):
	nVal = int(input("정수 입력 : "))
	
	nVal_Min = 1
	nVal_Max = 100
	
	print("\n=====> 결과 <=====")
	
	# 범위에 포함 될 경우
	if nVal >= nVal_Min and nVal <= nVal_Max:
		print(f"{nVal} 은(는) {nVal_Min} ~ {nVal_Max} 사이에 존재합니다.")
		
	else:
		print(f"{nVal} 은(는) {nVal_Min} ~ {nVal_Max} 사이에 존재하지않습니다.")
	
	"""
	비교 연산자 체이닝이란?
	- 여러 비교 연산자를 논리 and 연산자 없이 연속으로 사용 할 수 있는 기능을 의미한다. (+ 즉,
	비교 연산자 체이닝을 활용하면 범위 비교 조건문을 좀 더 직관적으로 작성하는 것이 가능하다.)
	
	Ex)
	nValA = 10
	nValB = 20
	nValC = 30
	nValD = 40
	
	bIsTrueA = nValA <= nValB <= nValC <= nValD
	bIsTrueB = nValA <= nValB and nValB <= nValC and nValC <= nValD
	
	위와 같이 비교 연산자 체이닝을 활용하면 논리 and 연산자를 사용 할 때 보다 비교 명령문을 축약해서 작성하는 것이
	가능하다.
	"""
	# 범위에 포함 될 경우
	if nVal_Min <= nVal <= nVal_Max:
		print(f"{nVal} 은(는) {nVal_Min} ~ {nVal_Max} 사이에 존재합니다.")
	
	else:
		print(f"{nVal} 은(는) {nVal_Min} ~ {nVal_Max} 사이에 존재하지않습니다.")
		