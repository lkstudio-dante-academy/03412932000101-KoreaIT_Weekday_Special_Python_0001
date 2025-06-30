import os
import sys

import random

"""
재귀 호출 (Recursive Call) 이란?
- 함수가 자기 자신을 다시 호출 할 수 있는 기능을 의미한다, (+ 즉, 함수는 필요에 따라 자기 자신을
다시 호출함으로서 복잡한 문제를 쉽게 풀어내는 것이 가능하다.)

단, 재귀 호출은 반드시 호출을 멈추기 위한 명령문을 작성해줘야한다. (+ 즉, 재귀 호출을 멈추기 위한 명령문을
작성하지 않을 경우 특정 함수가 자기 자신을 무한히 호출하는 무한 루프에 빠진다는 것을 알 수 있다.)

Ex)
def someMethod():
	someMethod()
	
someMethod()

위와 같이 함수는 자기 자신을 다시 호출하는 것이 가능하지만 재귀 호출을 끝내기 위한 명령문이 없을 경우
무한 루프에 빠진다는 것을 알 수 있다.
"""


# Example 13 (함수 - 3)
def start(args):
	nVal = int(input("정수 입력 : "))
	nFactorial = getFactorial(nVal)
	
	print(f"{nVal}! : {nFactorial}")
	oListValues = []
	
	for i in range(0, 10):
		nVal = random.randrange(1, 100)
		oListValues.append(nVal)
	
	print("\n=====> 리스트 <=====")
	
	for nVal in oListValues:
		print(f"{nVal}, ", end = "")
	
	nVal_Sum = getVal_Sum(oListValues, 0)
	print(f"\n\n합계 : {nVal_Sum}")
	
	print("\n=====> 피보나치 수열 <=====")
	
	for i in range(0, 10):
		nVal = getNumber_Fibonacci(i)
		print(f"{nVal}, ", end = "")
	
	print()


# 팩토리얼을 반환한다
def getFactorial(a_nVal):
	"""
	아래와 같이 재귀 호출을 종료 시키기 위한 명령문을 반드시 작성해줘야한다.
	"""
	# 0 이하 일 경우
	if a_nVal <= 0:
		return 1
	
	return a_nVal * getFactorial(a_nVal - 1)


# 합계를 반환한다
def getVal_Sum(a_oListValues, a_nIdx):
	# 범위를 벗어났을 경우
	if a_nIdx >= len(a_oListValues):
		return 0
	
	return a_oListValues[a_nIdx] + getVal_Sum(a_oListValues, a_nIdx + 1)


# 피보나치 수를 반환한다
def getNumber_Fibonacci(a_nVal):
	# 1 이하 일 경우
	if a_nVal <= 1:
		return 0 if a_nVal <= 0 else 1
	
	return getNumber_Fibonacci(a_nVal - 1) + getNumber_Fibonacci(a_nVal - 2)
