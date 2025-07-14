import os
import sys


# 위젯
class CWidget:
	m_nVal_Static = 0
	
	# 초기화
	def __init__(self):
		self.m_nVal = 0
		
	# 값을 증가 시킨다
	def incrVal(self, a_nVal):
		self.m_nVal += a_nVal
		CWidget.m_nVal_Static += a_nVal
		
	# 정보를 출력한다
	def showInfo(self):
		print(f"멤버 변수 : {self.m_nVal}")
		print(f"클래스 변수 : {CWidget.m_nVal_Static}")
		