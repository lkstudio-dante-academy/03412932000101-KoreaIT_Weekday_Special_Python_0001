import os
import sys

"""
Python 연습 문제 9
- 모든 조합 출력하기
- 서로 다른 가격의 물건이 3 개 존재한다 (+ Ex. 50 원, 250 원, 500 원)
- 사용자로부터 소지 금액을 입력 받아 구입 가능한 모든 조합 출력하기
- 단, 소지 금액은 모두 소비해야한다

Ex)
소지 금액 입력 : 1000

=====> 구입 가능 조합 <=====
물건 A x 0 개, 물건 B x 0 개, 물건 C x 2 개
물건 A x 0 개, 물건 B x 2 개, 물건 C x 1 개
물건 A x 0 개, 물건 B x 4 개, 물건 C x 0 개
...이하 생략
"""

# Training 9
def start(args):
	PRICE_STUFF_A = 50
	PRICE_STUFF_B = 250
	PRICE_STUFF_C = 500
	
	nAmount = int(input("소지 금액 입력 : "))
	print("\n=====> 구입 가능 조합 <=====")
	
	for i in range(0, nAmount + 1, PRICE_STUFF_A):
		for j in range(0, nAmount + 1, PRICE_STUFF_B):
			for k in range(0, nAmount + 1, PRICE_STUFF_C):
				# 조합이 불가능 할 경우
				if i + j + k != nAmount:
					continue
					
				nNumStuffsA = i // PRICE_STUFF_A
				nNumStuffsB = j // PRICE_STUFF_B
				nNumStuffsC = k // PRICE_STUFF_C
				
				oMsgA = f"물건 A x {nNumStuffsA} 개"
				oMsgB = f"물건 B x {nNumStuffsB} 개"
				oMsgC = f"물건 C x {nNumStuffsC} 개"
				
				print(f"{oMsgA}, {oMsgB}, {oMsgC}")
