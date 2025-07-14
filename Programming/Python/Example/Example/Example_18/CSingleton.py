import os
import sys


# 싱글턴
class CSingleton:
	m_oInst = None
	
	# 초기화
	def __init__(self):
		self.m_nVal = 0
	
	# 인스턴스를 반환한다
	@classmethod
	def getInst(cls):
		# 인스턴스가 없을 경우
		if cls.m_oInst == None:
			cls.m_oInst = CSingleton()
			
		return cls.m_oInst
	
	# 값을 변경한다
	def setVal(self, a_nVal):
		self.m_nVal = a_nVal
		
	# 정보를 출력한다
	def showInfo(self):
		print(f"멤버 변수 : {self.m_nVal}")
		