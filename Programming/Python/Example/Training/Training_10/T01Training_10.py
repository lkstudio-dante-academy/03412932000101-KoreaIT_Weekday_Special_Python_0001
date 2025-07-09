import os
import sys

"""
Python 연습 문제 10
- 데이터 이동하기
- 1 ~ 5 범위의 수를 지니고 있는 리스트를 생성한다
- 사용자로부터 메뉴를 입력받아 리스트에 있는 데이터를 오른쪽 or 왼쪽으로
이동시킨다

Ex)
=====> 리스트 - 원본 <=====
1, 2, 3, 4, 5

=====> 메뉴 <=====
1. 왼쪽으로 이동
2. 오른쪽으로 이동
3. 종료

선택 : 1
=====> 리스트 - 이동 후 <=====
2, 3, 4, 5, 1

선택 : 2
=====> 리스트 - 이동 후 <=====
1, 2, 3, 4, 5

선택 : 3
프로그램을 종료합니다.
"""


# Training 10
def start(args):
	MENU_MOVE_LEFT = 1
	MENU_MOVE_RIGHT = 2
	MENU_EXIT = 3
	
	oListValues = [1, 2, 3, 4, 5]
	
	print("=====> 리스트 - 원본 <=====")
	print(f"{oListValues}\n")
	
	while True:
		print("=====> 메뉴 <=====")
		print("1. 왼쪽으로 이동")
		print("2. 오른쪽으로 이동")
		print("3. 종료")
		
		nMenu = int(input("\n선택 : "))
		
		# 종료 일 경우
		if nMenu == MENU_EXIT:
			"""
			break 키워드란?
			- 반복문 내부에서만 사용 가능한 키워드로 프로그램의 흐름을 반복문 밖으로 이동 시키는 역할을
			수행한다. (+ 즉, 해당 키워드를 활용하면 반복문을 즉시 종료 시키는 것이 가능하다.)
			"""
			break
			
		# 왼쪽으로 이동 일 경우
		if nMenu == MENU_MOVE_LEFT:
			nVal = oListValues[0]
			del oListValues[0]
			
			oListValues.append(nVal)
		
		# 오른쪽으로 이동 일 경우
		elif nMenu == MENU_MOVE_RIGHT:
			nVal = oListValues[-1]
			del oListValues[-1]
			
			oListValues.insert(0, nVal)
		
		print("=====> 리스트 - 이동 후 <=====")
		print(oListValues)
