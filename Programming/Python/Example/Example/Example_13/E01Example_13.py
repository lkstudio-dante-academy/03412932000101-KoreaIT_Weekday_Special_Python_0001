import os
import sys

"""
디폴트 매개 변수란?
- 매개 변수에 초기 데이터를 설정 할 수 있는 기능을 의미한다. (+ 즉, 매개 변수에 기본 값을
설정 할 수 있다는 것을 의미한다.)

일반적으로 함수를 호출 할 경우 해당 함수의 매개 변수에 개수만큼 입력 데이터를 명시해야하지만
디폴트 매개 변수를 활용하면 입력 데이터를 생략하는 것이 가능하다. (+ 즉, 입력 데이터가 생략 된 매개 변수는
초기 데이터를 설정 된다는 것을 알 수 있다.)

Ex)
def someFunc(a_nValA, a_nValB = 0):
	# Do Something
	
someFunc(10)				<- a_nValA = 10, a_nValB = 0 전달
someFunc(10, 20)			<- a_nValA = 10, a_nValB = 20 전달

위와 같이 매개 변수 a_nValB 는 디폴트 값이 명시되어있기 때문에 함수를 호출 할 때 해당 매개 변수에 대한
데이터를 명시하지 않으면 자동으로 0 으로 설정된다는 것을 알 수 있다.

네임드 매개 변수란?
- 입력 데이터를 전달 받을 매개 변수를 직접 명시 할 수 있는 기능을 의미한다.

기본적으로 입력 데이터는 순서에 의해 매개 변수에 전달 되기 때문에 입력 데이터의 순서와 매개 변수의 순서가
동일해야한다.

반면 네임드 매개 변수는 입력 데이터를 전달 받을 매개 변수를 직접 명시 할 수 있기 때문에 입력 데이터의 순서와
매개 변수의 순서가 달라질 수 있다는 차이점이 존재한다.

Ex)
def someFunc(a_nValA, a_nValB):
	# Do Something
	
someFunc(a_nValB = 20, a_nValA = 10)			<- a_nValA = 10, a_nValB = 20 전달

위와 같이 네임드 매개 변수를 활용하면 입력 데이터를 전달 받을 매개 변수를 명시하는 것이 가능하다.
"""


# Example 13 (함수 - 3)
def start(args):
	nVal_SumA = getVal_Sum(10)
	nVal_SumB = getVal_Sum(10, 20)
	
	print("=====> 디폴트 매개 변수 <=====")
	print(f"합계 A : {nVal_SumA}")
	print(f"합계 B : {nVal_SumB}")
	
	"""
	아래와 같이 네임드 매개 변수를 활용하면 순서에 상관 없이 입력 데이터를 명시하는 것이 가능하다.
	"""
	nVal_SumC = getVal_Sum(10, a_nValC = 20)
	
	print("\n=====> 네임드 매개 변수 <=====")
	print(f"합계 C : {nVal_SumC}")


# 합계를 반환한다
def getVal_Sum(a_nValA, a_nValB = 0, a_nValC = 0):
	return a_nValA + a_nValB + a_nValC
