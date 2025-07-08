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
	
	nPos_Odd = 0
	nPos_Even = nNumValues - 1
	
	for i in range(0, nNumValues):
		nVal = int(input(f"{i + 1} 번째 정수 입력 : "))
		
		# 홀수 일 경우
		if nVal % 2 != 0:
			oListValues[nPos_Odd] = nVal
			nPos_Odd += 1
		
		else:
			oListValues[nPos_Even] = nVal
			nPos_Even -= 1
	
	print("\n=====> 결과 <=====")
	
	for nVal in oListValues:
		print(f"{nVal}, ", end = "")
	
	print()
