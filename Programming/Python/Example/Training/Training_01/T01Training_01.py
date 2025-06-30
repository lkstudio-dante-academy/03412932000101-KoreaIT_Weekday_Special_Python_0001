import os
import sys

"""
Python 연습 문제 1
- 다양한 방법으로 ABC 출력하기
- 최소 4 가지 이상의 방법으로 ABC 출력하기
"""


# Training 1
def start(args):
	oStr = "ABC"
	
	print("ABC")
	print(f"{oStr}")
	print(f"{"A"}{"B"}{"C"}")
	print(f"{chr(65)}{chr(66)}{chr(67)}")
	print(f"{10:X}{11:X}{12:X}")
	