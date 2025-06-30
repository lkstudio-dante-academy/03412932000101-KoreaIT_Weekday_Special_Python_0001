import os
import sys

"""
Python 연습 문제 6
- 합계 및 평균 출력하기
- 사용자로부터 정수를 입력 받는다
- 입력 받은 정수가 0 보다 클 경우 값을 누적 후 다시 정수를 입력 받는다
- 입력 받은 정수가 0 이하 일 경우 입력을 종료하고 합계와 평균을 출력한다

Ex)
1 번째 정수 입력 : 1
2 번째 정수 입력 : 3
3 번째 정수 입력 : 5
4 번째 정수 입력 : 0

합계 : 14
평균 : 3.0
"""


# Training 6
def start(args):
	nVal_Sum = 0
	nNumValues = 0
	
	bIsContinue = True
	
	while bIsContinue:
		nVal = int(input(f"{nNumValues + 1} 번째 정수 입력 : "))
		
		# 입력을 종료했을 경우
		if nVal <= 0:
			bIsContinue = False
		
		else:
			nVal_Sum += nVal
			nNumValues += 1
	
	print(f"\n합계 : {nVal_Sum}")
	print(f"평균 : {nVal_Sum / nNumValues}")
	