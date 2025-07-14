import os
import sys

import random

"""
Python 연습 문제 17
- 리스트 치환하기 (+ 재귀 호출 활용)
- 요구 사항은 연습 문제 11 참고
"""


# Training 17
def start(args):
	oListValues = [random.randrange(1, 16) for i in range(0, 10)]
	
	print("=====> 리스트 - 치환 전 <=====")
	print(oListValues)
	
	nIdx = int(input("\n위치 입력 : "))
	
	# 인덱스가 유효하지 않을 경우
	if nIdx < 0 or nIdx >= len(oListValues):
		print("인덱스가 유효하지 않습니다.")
		return
	
	replaceValues(oListValues, nIdx)
	
	print("\n=====> 리스트 - 치환 후 <=====")
	print(oListValues)


# 값을 치환한다
def replaceValues(a_oListValues, a_nIdx):
	bIsValid = a_nIdx >= 0 and a_nIdx < len(a_oListValues)
	
	# 값 치환이 불가능 할 경우
	if not bIsValid:
		return
	
	# 값 치환이 불가능 할 경우
	if len(f"{a_oListValues[a_nIdx]}") != 1:
		return
	
	a_oListValues[a_nIdx] = -1
	
	replaceValues(a_oListValues, a_nIdx - 1)
	replaceValues(a_oListValues, a_nIdx + 1)
	