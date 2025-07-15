import os
import sys

"""
싱글턴 (Singleton) 이란?
- 디자인 패턴 (Design Pattern) 중 하나로서 객체의 생성 개수를 1 개로 제한하는 구조를 의미한다. (+ 즉,
싱글턴 패턴을 활용하면 프로그램 전체에서 자유롭게 접근 가능한 단일 객체를 생성하는 것이 가능하다.)
"""


# 싱글턴
class CSingleton:
	m_oInst = None
	
	# 초기화
	def __init__(self):
		self.m_nVal = 0
		
	# 인스턴스를 반환한다
	@classmethod
	def getInst(cls):
		"""
		@classmethod 데코레이터란?
		- 해당 함수가 클래스 함수라는 것을 알리는 역할을 수행하는 데코레이터를 의미한다. (+ 즉,
		@classmethod 데코레이터가 명시 된 함수는 클래스에 종속 되는 클래스 함수라는 것을 의미한다.)
		
		cls 매개 변수란?
		- 해당 함수를 호출 한 클래스를 의미한다. (+ 즉, 클래스 함수는 첫 번째 매개 변수는 해당 함수를 호출 한
		클래스가 입력으로 전달 된다는 것을 알 수 있다.)
		"""
		
		# 인스턴스가 없을 경우
		if CSingleton.m_oInst == None:
			CSingleton.m_oInst = CSingleton()
			
		return CSingleton.m_oInst
	
	# 값을 변경한다
	def setVal(self, a_nVal):
		self.m_nVal = a_nVal
		
	# 정보를 출력한다
	def showInfo(self):
		print(f"멤버 변수 : {self.m_nVal}")
		