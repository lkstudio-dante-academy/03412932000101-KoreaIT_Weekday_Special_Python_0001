import os
import sys

import random

"""
Python 연습 문제 16
- 숫자 야구 게임 제작하기
- 1 ~ 9 사이의 수 중 랜덤하게 중복되지 않는 정답 4 개를 추출한다
- 사용자로부터 숫자 4 개를 입력받아 스트라이크 or 볼 여부를 검사한다
- 사용자가 입력 한 숫자가 정답에 존재하고 위치가 같다면 스트라이크
- 사요자가 입력 한 숫자가 정답에 존재하지만 위치가 다르다면 볼
- 4 스트라이크가 되면 게임을 종료한다

Ex)
정답 : 1 8 2 6

정수 (4 개) 입력 : 1 2 8 6
결과 : 2 Strike, 2 Ball

정수 (4 개) 입력 : 1 8 2 6
결과 : 4 Strike, 0 Ball

프로그램을 종료합니다.
"""

# Training 16
def start(args):
	oAnswer = []
	setupAnswer(oAnswer)
	
	print(f"정답 : {oAnswer}\n")
	
	while True:
		oTokens = input("정답 (4 개) 입력 : ").split()
		oListValues = list(map(int, oTokens))
		
		nCount_Strike = 0
		nCount_Ball = 0
		
		for i in range(0, len(oAnswer)):
			for j in range(0, len(oListValues)):
				# 값이 다를 경우
				if oAnswer[i] != oListValues[j]:
					continue
				
				nCount_Strike += 1 if i == j else 0
				nCount_Ball += 1 if i != j else 0
				
		print(f"결과 : {nCount_Strike} Strike, {nCount_Ball} Ball\n")
		
		# 4 스트라이크 일 경우
		if nCount_Strike >= 4:
			break
			
	print("프로그램을 종료합니다.")


# 정답을 설정한다
def setupAnswer(a_oAnswer):
	oSetValues = set()
	
	while len(oSetValues) < 4:
		nVal = random.randrange(1, 10)
		oSetValues.add(nVal)
		
	for nVal in oSetValues:
		a_oAnswer.append(nVal)
		