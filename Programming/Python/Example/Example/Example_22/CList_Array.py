import os
import sys


# 배열 리스트
class CList_Array:
	# 초기화
	def __init__(self, a_nSize = 5):
		self.m_nNumValues = 0
		self.m_oValues = [0] * a_nSize
	
	# 개수를 반환한다
	def getNumValues(self):
		return self.m_nNumValues
	
	# 값을 반환한다
	def getVal(self, a_nIdx):
		return self.m_oValues[a_nIdx]
	
	# 값을 추가한다
	def addVal(self, a_tVal):
		# 공간이 부족 할 경우
		if self.m_nNumValues >= len(self.m_oValues):
			self.resize(len(self.m_oValues) * 2)
		
		self.m_oValues[self.m_nNumValues] = a_tVal
		self.m_nNumValues += 1
	
	# 값을 추가한다
	def insertVal(self, a_nIdx, a_tVal):
		# 공간이 부족 할 경우
		if self.m_nNumValues >= len(self.m_oValues):
			self.resize(len(self.m_oValues) * 2)
		
		for i in range(a_nIdx + 1, self.m_nNumValues + 1)[::-1]:
			self.m_oValues[i] = self.m_oValues[i - 1]
		
		self.m_oValues[a_nIdx] = a_tVal
		self.m_nNumValues += 1
	
	# 값을 제거한다
	def removeVal(self, a_tVal):
		nResult = self.findVal(a_tVal)
		
		# 값 제거가 불가능 할 경우
		if nResult < 0:
			return
		
		self.removeVal_At(nResult)
	
	# 값을 제거한다
	def removeVal_At(self, a_nIdx):
		for i in range(a_nIdx, self.m_nNumValues - 1):
			self.m_oValues[i] = self.m_oValues[i + 1]
		
		self.m_nNumValues -= 1
	
	# 값을 탐색한다
	def findVal(self, a_tVal):
		for i in range(0, self.m_nNumValues):
			# 값이 존재 할 경우
			if a_tVal == self.m_oValues[i]:
				return i
		
		return -1
	
	# 크기를 변경한다
	def resize(self, a_nSize_New):
		oValues_New = [0] * a_nSize_New
		
		for i in range(0, len(self.m_oValues)):
			oValues_New[i] = self.m_oValues[i]
		
		self.m_oValues = oValues_New
		