import os
import sys

import random

"""
Python 연습 문제 11
- 리스트 치환하기
- 1 ~ 15 사이의 수를 랜덤하게 10 개 추출한다
- 사용자에게 위치를 입력받아 해당 위치를 포함한 주변 데이터 중 1 자리수 숫자를
모두 -1 로 치환하기

Ex)
=====> 리스트 - 치환 전 <=====
1, 10, 3, 4, 9, 12, 15, 14, 1, 2

위치 입력 : 3

=====> 리스트 - 치환 후 <=====
1, 10, -1, -1, -1, 12, 15, 14, 1, 2
"""


# Training 11
def start(args):
	oListValues = []
	
	for i in range(0, 10):
		nVal = random.randrange(1, 16)
		oListValues.append(nVal)
		
	print("=====> 리스트 - 치환 전 <=====")
	print(oListValues)
	
	nIdx = int(input("\n위치 입력 : "))
	
	# 인덱스가 유효하지 않을 경우
	if nIdx < 0 or nIdx >= len(oListValues):
		print("인덱스가 유효하지 않습니다.")
		return
	
	i = nIdx
	
	while i >= 0 and len(f"{oListValues[i]}") == 1:
		oListValues[i] = -1
		i -= 1
		
	i = nIdx + 1
	
	while i < len(oListValues) and len(f"{oListValues[i]}") == 1:
		oListValues[i] = -1
		i += 1
		
	print("\n=====> 리스트 - 치환 후 <=====")
	print(oListValues)
	