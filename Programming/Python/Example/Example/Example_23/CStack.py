import os
import sys


# 스택
class CStack:
	# 초기화
	def __init__(self):
		self.m_nTop = 0
		self.m_oListValues = [0] * 5
		
	# 빈 여부를 검사한다
	def isEmpty(self):
		return self.m_nTop <= 0
		
	# 값을 추가한다
	def push(self, a_nVal):
		# 리스트가 가득 찼을 경우
		if self.m_nTop >= len(self.m_oListValues):
			oListValues_New = [0] * (len(self.m_oListValues) * 2)
			
			for i in range(0, len(self.m_oListValues)):
				oListValues_New[i] = self.m_oListValues[i]
				
			self.m_oListValues = oListValues_New
			
		self.m_oListValues[self.m_nTop] = a_nVal
		self.m_nTop += 1
		
	# 값을 제거한다
	def pop(self):
		nVal = self.m_oListValues[self.m_nTop - 1]
		self.m_nTop -= 1
		
		return nVal
	