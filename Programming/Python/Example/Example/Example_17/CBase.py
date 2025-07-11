import os
import sys


# 부모 클래스
class CBase:
	# 초기화
	def __init__(self, a_nVal, a_fVal):
		self.m_nVal = a_nVal
		self.m_fVal = a_fVal
	
	# 정보를 출력한다
	def showInfo(self):
		print(f"정수 : {self.m_nVal}")
		print(f"실수 : {self.m_fVal}")
