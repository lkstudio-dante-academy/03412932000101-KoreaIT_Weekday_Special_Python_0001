import os
import random
import sys

"""
Python 연습 문제 19
- 슬라이드 퍼즐 게임 제작하기
- 5 x 5 리스트를 생성 후 0 ~ 24 까지 수로 차례대로 초기화한다
- 0 은 공백을 의미한다
- 초기화 된 리스트를 재배치 후 다시 차례대로 순서를 맞추면 게임을 종료한다
- 숫자의 위치를 재배치하는 방법은 사용자로부터 위치를 입력 받아
해당 위치가 공백 주변이라면 공백과 해당 숫자의 위치를 변경한다

Ex)
 1  2  3  4  5
 6  7  8  9 10
11 12 20 14 15
16 24 18 19 13
21 22 23 17

위치 (X, Y) 입력 : 4 3

 1  2  3  4  5
 6  7  8  9 10
11 12 20 14 15
16 24 18 19
21 22 23 17 13

...이하 생략

 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19
21 22 23 24 20

위치 (X, Y) 입력 : 4 4

 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24

프로그램을 종료합니다.
"""


# Training 19
def start(args):
	oListValues = []
	setupValues(oListValues)
	
	while True:
		printValues(oListValues)
		oPos = list(map(int, input("\n위치 (X, Y) 입력 : ").split()))
		
		oListOffsets = [
			(0, 1), (0, -1), (1, 0), (-1, 0)
		]
		
		for oOffset in oListOffsets:
			nPos_NextX = oPos[IDX_X] + oOffset[IDX_X]
			nPos_NextY = oPos[IDX_Y] + oOffset[IDX_Y]
			
			bIsValidA = nPos_NextX >= 0 and nPos_NextX < NUM_COLUMNS
			bIsValidB = nPos_NextY >= 0 and nPos_NextY < NUM_ROWS
			
			# 범위를 벗어났을 경우
			if not bIsValidA or not bIsValidB:
				continue
			
			# 공백 일 경우
			if oListValues[nPos_NextY][nPos_NextX] == 0:
				nPos_X = oPos[IDX_X]
				nPos_Y = oPos[IDX_Y]
				
				nVal = oListValues[nPos_Y][nPos_X]
				nVal_Empty = oListValues[nPos_NextY][nPos_NextX]
				
				oListValues[nPos_Y][nPos_X] = nVal_Empty
				oListValues[nPos_NextY][nPos_NextX] = nVal
				
				break
				
		print()
		
		# 정답 일 경우
		if isAnswer(oListValues):
			break
			
	printValues(oListValues)
	print("프로그램을 종료합니다.")
	

IDX_X = 0
IDX_Y = 1

NUM_ROWS = 5
NUM_COLUMNS = 5

# 정답 여부를 검사한다
def isAnswer(a_oListValues):
	for i in range(0, NUM_ROWS * NUM_COLUMNS):
		nRow = i // NUM_COLUMNS
		nCol = i % NUM_COLUMNS
		
		nVal_Answer = (i + 1) % (NUM_ROWS * NUM_COLUMNS)
		
		# 정답이 아닐 경우
		if a_oListValues[nRow][nCol] != nVal_Answer:
			return False
		
	return True


# 값을 설정한다
def setupValues(a_oListValues):
	for i in range(0, 5):
		oListValues_Column = []
		
		for j in range(0, 5):
			nVal = (i * 5) + j
			oListValues_Column.append(nVal)
	
		a_oListValues.append(oListValues_Column)
		
	shuffleValues(a_oListValues)
	
	
# 값을 재배치한다
def shuffleValues(a_oListValues):
	for i in range(0, len(a_oListValues)):
		for j in range(0, len(a_oListValues[i])):
			nIdx_Row = random.randrange(0, NUM_ROWS)
			nIdx_Col = random.randrange(0, NUM_COLUMNS)
			
			nVal = a_oListValues[i][j]
			nVal_Random = a_oListValues[nIdx_Row][nIdx_Col]
			
			a_oListValues[i][j] = nVal_Random
			a_oListValues[nIdx_Row][nIdx_Col] = nVal
	
	
# 값을 출력한다
def printValues(a_oListValues):
	for i in range(0, len(a_oListValues)):
		for j in range(0, len(a_oListValues[i])):
			nVal = a_oListValues[i][j]
			nVal = " " if nVal == 0 else nVal
			
			print(f"{nVal:3}", end = "")
			
		print()
