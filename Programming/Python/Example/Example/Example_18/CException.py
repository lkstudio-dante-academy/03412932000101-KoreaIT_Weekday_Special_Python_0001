import os
import sys


# 사용자 정의 예외
class CException(Exception):
	# 초기화
	def __init__(self, a_oMsg):
		super().__init__(a_oMsg)
		