import os
import sys

import random

"""
Python 연습 문제 5
- 업/다운 게임 제작하기
- 1 ~ 99 사이의 수 중 하나를 랜덤하게 추출한다
- 사용자로부터 숫자를 입력 받아 정답 여부를 검사한다
- 입력 받은 수가 정답 일 경우 게임을 종료한다
- 입력 받은 수가 정답이 아닐 경우 가이드 메세지를 출력하고 다시 수를 입력 받는다

Ex)
정답 : 85

정수 입력 : 80
정답은 80 보다 큽니다.

정수 입력 : 90
정답은 90 보다 작습니다.

정수 입력 : 85
프로그램을 종료합니다.
"""


# Training 5
def start(args):
	nAnswer = random.randrange(1, 100)
	print(f"정답 : {nAnswer}\n")
	
	bIsContinue = True
	
	while bIsContinue:
		nVal = int(input("정수 입력 : "))
		
		# 정답 일 경우
		if nVal == nAnswer:
			bIsContinue = False
		
		else:
			oMsg = "큽니다." if nVal < nAnswer else "작습니다."
			print(f"정답은 {nVal} 보다 {oMsg}\n")
			
	print("프로그램을 종료합니다.")
	