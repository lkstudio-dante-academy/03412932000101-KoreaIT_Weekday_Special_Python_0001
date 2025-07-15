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
		"""
		클래스 변수에 접근 하기 위해서는 아래와 같이 클래스 이름을 명시해줘야한다. (+ 즉,
		클래스 이름을 명시하지 않으면 지역 변수에 접근하는 것으로 인지 된다는 것을 알 수 있다.)
		"""
		self.m_nVal += a_nVal
		CWidget.m_nVal_Static += a_nVal
		
	# 정보를 출력한다
	def showInfo(self):
		print(f"멤버 변수 : {self.m_nVal}")
		print(f"클래스 변수 : {CWidget.m_nVal_Static}")
		