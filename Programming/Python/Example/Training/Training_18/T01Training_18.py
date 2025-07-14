import os
import sys

import random

"""
Python 연습 문제 18
- 이진 탐색 구현하기 (+ 반복문, 재귀 호출 활용)
- 1 ~ 10 사이의 수 중 랜덤하게 10 개를 추출해서 리스트를 생성한다
- 해당 리스트를 기반으로 이진 탐색 결과 출력하기

Ex)
=====> 리스트 - 정렬 전 <=====
1, 10, 5, 8, 2, 3, 9, 7, 4, 2

=====> 리스트 - 정렬 후 <=====
1, 2, 2, 3, 4, 5, 7, 8, 9, 10

정수 입력 : 6
결과 : -1

정수 입력 : 8
결과 : 6
"""


# Training 18
def start(args):
	oListValues = [random.randrange(0, 10) + 1 for i in range(0, 10)]
	
	print("=====> 리스트 - 정렬 전 <=====")
	print(oListValues)
	
	oListValues.sort()
	
	print("\n=====> 리스트 - 정렬 후 <=====")
	print(oListValues)
	
	nVal = int(input("\n정수 입력 : "))
	
	nResultA = findValA(oListValues, nVal)
	nResultB = findValB(oListValues, nVal)
	
	print(f"결과 : {nResultA}, {nResultB}")
	
	
# 값을 탐색한다
def findValA(a_oListValues, a_nVal):
	nLeft = 0
	nRight = len(a_oListValues) - 1
	
	while nLeft <= nRight:
		nMiddle = (nLeft + nRight) // 2
		
		# 값이 존재 할 경우
		if a_nVal == a_oListValues[nMiddle]:
			return nMiddle
		
		# 값이 왼쪽에 존재 할 경우
		if a_nVal < a_oListValues[nMiddle]:
			nRight = nMiddle - 1
			
		else:
			nLeft = nMiddle + 1
			
	return -1


# 값을 탐색한다
def findValB(a_oListValues, a_nVal):
	nLeft = 0
	nRight = len(a_oListValues) - 1
	
	return findValB_Internal(a_oListValues, a_nVal, nLeft, nRight)


# 값을 탐색한다
def findValB_Internal(a_oListValues, a_nVal, a_nLeft, a_nRight):
	# 값 탐색이 불가능 할 경우
	if a_nLeft > a_nRight:
		return -1
	
	nMiddle = (a_nLeft + a_nRight) // 2
	
	# 값이 존재 할 경우
	if a_nVal == a_oListValues[nMiddle]:
		return nMiddle
	
	# 값이 왼쪽에 존재 할 경우
	if a_nVal < a_oListValues[nMiddle]:
		return findValB_Internal(a_oListValues,
								 a_nVal, a_nLeft, nMiddle - 1)
	
	return findValB_Internal(a_oListValues,
							 a_nVal, nMiddle + 1, a_nRight)