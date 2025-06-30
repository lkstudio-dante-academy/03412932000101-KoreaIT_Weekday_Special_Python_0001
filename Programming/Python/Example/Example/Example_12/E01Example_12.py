import os
import sys

"""
가변 길이 매개 변수 (Variable Parameter) 란?
- 일반적인 매개 변수와 달리 매개 변수의 개수가 고정 되어있지 않는 매개 변수를 의미한다. (+ 즉,
가변 길이 매개 변수를 활용하면 매개 변수 개수가 유동적인 메서드를 구현하는 것이 가능하다.)

Python 의 가변 길이 매개 변수는 위치 기반 매개 변수와 키워드 기반 매개 변수가 존재하며 각각 튜플과 딕셔너리 형태로
데이터를 전달 받는다. (+ 즉, 함수 호출 시 입력으로 전달되는 데이터를 Python 인터프리터가 자동으로 튜플 or 딕셔너리로
변환한다는 것을 알 수 있다.)

Ex)
void someFuncA(*args):				<- 위치 기반 매개 변수
	# Do Something
	
void someFuncB(**kwargs):			<- 키워드 기반 매개 변수
	# Do Something

someFuncA(10)								<- (10) 전달
someFuncA(10, 20)							<- (10, 20) 전달

someFuncB(nValA = 10)						<- { "nValA": 10 } 전달
someFuncB(nValA = 10, nValB = 20)			<- { "nValA": 10, "nValB": 20 } 전달

위와 같이 가변 길이 매개 변수는 개수가 고정 되어있지 않기 때문에 메서드 호출 시 마다 전달하는 데이터의 개수가
달라 질 수 있다는 것을 알 수 있다.

또한 필요에 따라 위치 기반 매개 변수와 키워드 기반 매개 변수를 동시에 사용하는 것도 가능하다.
"""


# Example 12 (함수 - 2)
def start(args):
	nVal_SumA = getVal_Sum(1, 2, 3)
	nVal_SumB = getVal_Sum(1, 2, 3, 4, 5, 6)
	nVal_SumC = getVal_Sum(1, 2, 3, 4, 5, 6, 7, 8, 9)
	
	print("=====> 위치 기반 매개 변수 <=====")
	print(f"{nVal_SumA}, {nVal_SumB}, {nVal_SumC}")
	
	print("\n=====> 키워드 기반 매개 변수 <=====")
	printValues(nValA = 10, nValB = 20, nValC = 30)


# 합계를 반환한다
def getVal_Sum(*args):
	nVal_Sum = 0
	
	"""
	아래와 같이 위치 기반 매개 변수는 튜플 형태로 입력 데이터가 전달 된다는 것을 알 수 있다.
	"""
	for nVal in args:
		nVal_Sum += nVal
		
	return nVal_Sum


# 결과를 출력한다
def printValues(**kwargs):
	"""
	아래와 같이 키워드 기반 매개 변수는 딕셔너리 형태로 입력 데이터가 전달 된다는 것을 알 수 있다.
	"""
	for oKey, nVal in kwargs.items():
		print(f"{oKey}: {nVal}, ", end = "")
		
	print()
	