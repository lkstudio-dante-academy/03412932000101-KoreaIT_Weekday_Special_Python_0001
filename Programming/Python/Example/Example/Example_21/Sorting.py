import os
import sys


# 값을 정렬한다
def sortValues_BySelection(a_oListValues):
	for i in range(0, len(a_oListValues) - 1):
		nIdx_Compare = i
		
		for j in range(i + 1, len(a_oListValues)):
			# 정렬이 필요 없을 경우
			if a_oListValues[nIdx_Compare] <= a_oListValues[j]:
				continue
				
			nIdx_Compare = j
			
		nLhs = a_oListValues[i]
		nRhs = a_oListValues[nIdx_Compare]
		
		a_oListValues[i], a_oListValues[nIdx_Compare] = nRhs, nLhs


# 값을 정렬한다
def sortValues_ByHeap(a_oListValues):
	for i in range(0, len(a_oListValues) // 2)[::-1]:
		sortValues_ByHeap_Internal(a_oListValues, i, len(a_oListValues))
		
	for i in range(1, len(a_oListValues))[::-1]:
		nLhs = a_oListValues[0]
		nRhs = a_oListValues[i]
		
		a_oListValues[0], a_oListValues[i] = nRhs, nLhs
		sortValues_ByHeap_Internal(a_oListValues, 0, i)


# 값을 정렬한다
def sortValues_ByHeap_Internal(a_oListValues, a_nIdx_Start, a_nNumValues):
	nIdx = a_nIdx_Start
	
	while nIdx < a_nNumValues // 2:
		nIdx_Compare = (nIdx * 2) + 1
		
		# 오른쪽 자식이 존재 할 경우
		if nIdx_Compare + 1 < a_nNumValues:
			nIdx_RChild = nIdx_Compare + 1
			nIdx_Compare = nIdx_Compare if a_oListValues[nIdx_Compare] >= a_oListValues[nIdx_RChild] else nIdx_RChild
			
		# 값 정렬이 불가능 할 경우
		if a_oListValues[nIdx] >= a_oListValues[nIdx_Compare]:
			break
			
		nLhs = a_oListValues[nIdx]
		nRhs = a_oListValues[nIdx_Compare]
		
		a_oListValues[nIdx], a_oListValues[nIdx_Compare] = nRhs, nLhs
		nIdx = nIdx_Compare


# 값을 정렬한다
def sortValues_ByQuick(a_oListValues):
	sortValues_ByQuick_Internal(a_oListValues, 0, len(a_oListValues) - 1)


# 값을 정렬한다
def sortValues_ByQuick_Internal(a_oListValues, a_nLeft, a_nRight):
	# 값 정렬이 불가능 할 경우
	if a_nLeft >= a_nRight:
		return
	
	nLeft = a_nLeft + 1
	nRight = a_nRight
	
	nPivot = a_nLeft
	
	while True:
		while nLeft < nRight and a_oListValues[nLeft] < a_oListValues[nPivot]:
			nLeft += 1
			
		while nRight >= nLeft and a_oListValues[nRight] >= a_oListValues[nPivot]:
			nRight -= 1
			
		# 값 정렬이 불가능 할 경우
		if nLeft >= nRight:
			break
			
		nLhs = a_oListValues[nLeft]
		nRhs = a_oListValues[nRight]
		
		a_oListValues[nLeft], a_oListValues[nRight] = nRhs, nLhs
		
	nLhs = a_oListValues[nPivot]
	nRhs = a_oListValues[nRight]
	
	a_oListValues[nPivot], a_oListValues[nRight] = nRhs, nLhs
	
	sortValues_ByQuick_Internal(a_oListValues, a_nLeft, nRight - 1)
	sortValues_ByQuick_Internal(a_oListValues, nRight + 1, a_nRight)
	