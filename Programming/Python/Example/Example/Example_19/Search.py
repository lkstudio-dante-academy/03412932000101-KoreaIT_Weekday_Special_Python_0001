import os
import sys


# 값을 탐색한다
def findVal_Linear(a_oListValues, a_nVal):
	for i in range(0, len(a_oListValues)):
		# 값이 존재 할 경우
		if a_nVal == a_oListValues[i]:
			return i
		
	return -1


# 값을 탐색한다
def findVal_Binary(a_oListValues, a_nVal):
	nLeft = 0
	nRight = len(a_oListValues) - 1
	
	while nLeft <= nRight:
		nMiddle = (nLeft + nRight) // 2
		
		# 값이 존재 할 경우
		if a_nVal == a_oListValues[nMiddle]:
			return nMiddle
		
		# 값이 왼쪽에 존재 할 경우
		if a_nVal < a_oListValues[nMiddle]:
			nRight = nMiddle - 1
			
		else:
			nLeft = nMiddle + 1
			
	return -1
