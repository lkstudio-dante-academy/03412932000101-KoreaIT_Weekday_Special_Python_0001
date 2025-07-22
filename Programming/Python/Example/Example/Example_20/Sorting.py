import os
import sys


# 값을 정렬한다
def sortValues_ByBubble(a_oListValues):
	for i in range(0, len(a_oListValues) - 1):
		for j in range(0, len(a_oListValues) - 1 - i):
			# 정렬이 필요 없을 경우
			if a_oListValues[j] <= a_oListValues[j + 1]:
				continue
			
			nLhs = a_oListValues[j]
			nRhs = a_oListValues[j + 1]
			
			a_oListValues[j], a_oListValues[j + 1] = nRhs, nLhs


# 값을 정렬한다
def sortValues_ByInsertion(a_oListValues):
	for i in range(1, len(a_oListValues)):
		j = i - 1
		nVal_Compare = a_oListValues[i]
		
		while j >= 0:
			# 정렬이 필요 없을 경우
			if a_oListValues[j] <= nVal_Compare:
				break
			
			a_oListValues[j + 1] = a_oListValues[j]
			j -= 1
		
		a_oListValues[j + 1] = nVal_Compare


# 값을 정렬한다
def sortValues_ByMerge(a_oListValues):
	oListValues_Temp = [0] * len(a_oListValues)
	sortValues_ByMerge_Internal(a_oListValues, 0, len(a_oListValues) - 1, oListValues_Temp)

# 값을 정렬한다
def sortValues_ByMerge_Internal(a_oListValues, a_nLeft, a_nRight, a_oOutListValues_Temp):
	# 값 정렬이 불가능 할 경우
	if a_nLeft >= a_nRight:
		return
	
	nMiddle = (a_nLeft + a_nRight) // 2
	
	sortValues_ByMerge_Internal(a_oListValues, a_nLeft, nMiddle, a_oOutListValues_Temp)
	sortValues_ByMerge_Internal(a_oListValues, nMiddle + 1, a_nRight, a_oOutListValues_Temp)
	
	nLeft = a_nLeft
	nRight = nMiddle + 1
	
	nNumValues_Sorted = 0
	
	while True:
		while nLeft <= nMiddle:
			# 값 정렬이 불가능 할 경우
			if a_oListValues[nLeft] > a_oListValues[nRight]:
				break
			
			a_oOutListValues_Temp[nNumValues_Sorted] = a_oListValues[nLeft]
			
			nLeft += 1
			nNumValues_Sorted += 1
		
		while nRight <= a_nRight:
			# 값 정렬이 불가능 할 경우
			if a_oListValues[nRight] >= a_oListValues[nLeft]:
				break
			
			a_oOutListValues_Temp[nNumValues_Sorted] = a_oListValues[nRight]
			
			nRight += 1
			nNumValues_Sorted += 1
		
		# 값 정렬이 불가능 할 경우
		if nLeft > nMiddle or nRight > a_nRight:
			break
	
	while nLeft <= nMiddle:
		a_oOutListValues_Temp[nNumValues_Sorted] = a_oListValues[nLeft]
		
		nLeft += 1
		nNumValues_Sorted += 1
	
	while nRight <= a_nRight:
		a_oOutListValues_Temp[nNumValues_Sorted] = a_oListValues[nRight]
		
		nRight += 1
		nNumValues_Sorted += 1
	
	for i in range(0, nNumValues_Sorted):
		a_oListValues[a_nLeft + i] = a_oOutListValues_Temp[i]
		