import os
import sys


# 큐
class CQueue:
	# 초기화
	def __init__(self):
		self.m_nFront = 0
		self.m_nRear = 0
		
		self.m_oListValues = [0] * 5
		
	# 빈 여부를 검사한다
	def isEmpty(self):
		return self.m_nFront == self.m_nRear
	
	# 값을 추가한다
	def enqueue(self, a_nVal):
		# 리스트가 가득 찼을 경우
		if (self.m_nRear + 1) % len(self.m_oListValues) == self.m_nFront:
			nNumValues = 0
			oListValues_New = [0] * (len(self.m_oListValues) * 2)
			
			while not self.isEmpty():
				oListValues_New[nNumValues] = self.dequeue()
				nNumValues += 1
				
			self.m_nFront = 0
			self.m_nRear = nNumValues
			
			self.m_oListValues = oListValues_New
			
		self.m_oListValues[self.m_nRear] = a_nVal
		self.m_nRear = (self.m_nRear + 1) % len(self.m_oListValues)
		
	# 값을 제거한다
	def dequeue(self):
		nVal = self.m_oListValues[self.m_nFront]
		self.m_nFront = (self.m_nFront + 1) % len(self.m_oListValues)
		
		return nVal
	