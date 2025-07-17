import os
import sys


# 유닛 A
class CUnitA:
	NAME = "유닛 A"
	PRICE = 250
	
	# 초기화
	def __init__(self, a_oTime):
		self.m_nIdx = 0
		self.m_oTime = a_oTime


# 유닛 B
class CUnitB:
	NAME = "유닛 B"
	PRICE = 500
	
	# 초기화
	def __init__(self, a_oTime):
		self.m_nIdx = 1
		self.m_oTime = a_oTime
		
		
# 유닛 C
class CUnitC:
	NAME = "유닛 C"
	PRICE = 750
	
	# 초기화
	def __init__(self, a_oTime):
		self.m_nIdx = 2
		self.m_oTime = a_oTime
		