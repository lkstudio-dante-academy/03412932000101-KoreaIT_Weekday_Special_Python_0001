import os
import sys

"""
Python 연습 문제 4
- 구구단 출력하기
- 사용자로부터 2 ~ 9 사이의 수를 입력 받아 해당 수에 해당하는 구구단 출력하기
- 단, 범위를 벗어나는 수를 입력 할 경우 잘못된 입력이라는 메세지 출력하기

Ex)
정수 (2 ~ 9) 입력 : 1
2 ~ 9 사이의 수를 입력해주세요.

정수 (2 ~ 9) 입력 : 3
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
...이하 생략
"""


# Training 4
def start(args):
	nVal = int(input("정수 (2 ~ 9) 입력 : "))
	
	# 올바른 수를 입력했을 경우
	if 2 <= nVal <= 9:
		i = 1
		
		while i <= 9:
			nResult = nVal * i
			print(f"{nVal} * {i} = {nResult}")
			
			i += 1
	
	else:
		print("2 ~ 9 사이의 수를 입력해주세요.")
