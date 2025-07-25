import os
import sys

from Example.Example_23.CStack import CStack

"""
스택 (Stack) 이란?
- FILO (First In Last Out) or LIFO (Last In First Out) 구조로 데이터를 관리하는 자료구조를 의미한다.
(+ 즉, 스택은 데이터의 입/출력 순서가 엄격하게 관리되는 자료구조라는 것을 알 수 있다.)

스택 관련 용어
- Push			<- 데이터 추가
- Pop			<- 데이터 제거
- Top			<- 데이터 추가/제거 위치
"""

# Example 23 (스택)
def start(args):
	oStackValues = CStack()
	print("=====> 입력 순서 <=====")
	
	for i in range(0, 10):
		print(f"{i + 1}, ", end = "")
		oStackValues.push(i + 1)

	print("\n\n=====> 스택 <=====")
	
	while not oStackValues.isEmpty():
		nVal = oStackValues.pop()
		print(f"{nVal}, ", end = "")
		
	print()
	