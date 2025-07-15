import os
import sys

import random

"""
람다 (Lambda) 란?
- 이름이 존재하지 않는 함수를 구현하는 기능을 의미한다. (+ 즉, 람다는 이름이 존재하지 않기 때문에
일반적인 함수와 달리 재사용을 위해서 구현 되는 함수가 아니라는 것을 알 수 있다.)

람다는 일회성 함수를 구현하는데 주로 활용되며 람다 내부에는 한 라인에 해당하는 명령문만 작성 할 수 있다. (+ 즉,
람다 내부에는 복잡한 명령문을 작성하는 것이 불가능하다.)

람다는 주로 다른 함수 내부에 구현되기 때문에 내장 함수라고도 불리며 람다를 감싸고 있는 외부 함수에 존재하는
지역 변수에 접근하는 것이 가능하다. (+ 즉, 람다는 외부 함수 내부에 존재하기 때문에 외부 함수의 일부로
인식 된 다는 것을 알 수 있다.)

Python 람다 구현 방법
- lambda + 매개 변수 + 람다 몸체

Ex)
oLambda = lambda a_nVal: print(a_nVal)
oLambda(10)

위와 같이 lambda 키워드를 활용하면 람다를 구현하는 것이 가능하며 구현 된 람다는 변수에 할당 후 호출하는 것이
가능하다. (+ 즉, oLambda 변수에는 람다를 참조하는 참조 값이 할당 된 다는 것을 알 수 있다.)

지역 함수 (Local Function) 란?
- 함수 내부에 함수를 정의 할 수 있는 기능을 의미한다. (+ 즉, 지역 함수는 지역 변수와 같이
함수가 정의 된 지역 내부에서만 접근 가능하다는 것을 알 수 있다.)

지역 함수는 람다와 같이 함수를 감싸고 있는 외부 함수에 선언 된 지역 변수에 접근하는 것이 가능하다.

Ex)
def someOuterFunc():
	def someInnerFunc():
		# Do Something
		
	someInnerFunc()			<- 호출 가능
	
someInnerFunc()				<- 호출 불가

위와 같이 someInnerFunc 함수는 someOuterFunc 내부에 구현 되었기 때문에 someOuterFunc 함수 내부에서는
호출이 가능하지만 외부에서는 호출이 불가능하다는 것을 알 수 있다.
"""


# Example 14 (함수 - 4)
def start(args):
	oListValues = []
	
	"""
	람다를 구현하면 람다 내부에 작성한 명령문을 참조 할 수 있는 참조 값이 반한되기 때문에 아래처럼
	명령문을 작성하면 람다를 구현과 동시에 호출하는 것이 가능하다.
	
	단, 일반적으로 함수는 구현 시점과 호출 시점이 다르며 람다 또한 구현과 동시에 호출하는 경우보다
	구현 된 람다를 변수에 할당 후 필요 할 때 람다를 호출하는 것이 일반적인 구조이다.
	"""
	(lambda : print("람다 함수가 호출되었습니다.\n"))()
	
	for i in range(0, 10):
		nVal = random.randrange(1, 100)
		oListValues.append(nVal)
	
	print("=====> 리스트 <=====")
	
	oPtr_PrintValues = printValues
	oPtr_PrintValues(oListValues)
	
	nVal_Local = 0
	
	"""
	지역 함수는 외부 함수 영역 내부에 구현되기 때문에 외부 함수의 일부분으로 인지가 된다. (+ 즉, 지역 함수는
	외부 함부 영역에 선언 된 지역 변수에 자유롭게 접근하는 것이 가능하다.)
	"""
	# 값을 비교한다
	def compareVal(a_nLhs, a_nRhs):
		"""
		nonlocal 키워드란?
		- global 키워드와 마찬가지로 외부 지역에 선언 된 지역 변수를 사용하겠다고 파이썬 인터프리터에게
		알리는 역할을 수행하는 키워드를 의미한다. (+ 즉, 해당 키워드를 이용해 외부 지역 변수에 대한 사용을
		파이썬 인터프리터에게 알리고 나면 해당 변수의 값을 변경하는 것이 가능하다.)
		"""
		nonlocal nVal_Local
		nVal_Local = 10
		
		# print(nVal_Local)
		return a_nLhs - a_nRhs
	
	"""
	아래와 같이 함수는 다른 함수의 입력으로 전달하는 것이 가능하다. (+ 즉, 함수를 데이터처럼 취급하는 것이
	가능하다.)
	"""
	sortValues(oListValues, compareVal)
	
	print("\n=====> 리스트 - 오름 차순 정렬 후 <=====")
	printValues(oListValues)
	
	sortValues(oListValues, lambda a_nLhs, a_nRhs: a_nRhs - a_nLhs)
	
	print("\n=====> 리스트 - 내림 차순 정렬 후 <=====")
	printValues(oListValues)
	
	oLambdaA = getLambda(10)
	oLambdaB = getLambda(20)
	
	print("\n=====> 람다 호출 <=====")
	oLambdaA()
	oLambdaB()


# 람다를 반환한다
def getLambda(a_nVal):
	"""
	람다 내부에서는 람다를 감싸고 있는 외부 지역에 존재하는 변수에 자유롭게 접근하는 것이 가능하다. (+ 즉,
	외부 지역에 선언 된 변수의 생명 주기와 상관 없이 접근이 가능하다는 것을 알 수 있다.)
	
	이는 람다 내부에 외부 지역에 선언 된 변수와 동일한 사본 변수가 존재하기 때문이다. (+ 즉,
	외부 지역에 선언 된 변수와 동일한 이름과 데이터를 지니고 있는 변수가 람다 내부에 선언 된다는 것을
	알 수 있다.)
	"""
	return lambda: print(f"정수 : {a_nVal}")


# 값을 정렬한다
def sortValues(a_oListValues, a_oCompare):
	for i in range(0, len(a_oListValues)):
		for j in range(0, len(a_oListValues) - (i + 1)):
			nLhs = a_oListValues[j]
			nRhs = a_oListValues[j + 1]
			
			# 정렬이 필요 없을 경우
			if a_oCompare(nLhs, nRhs) <= 0:
				continue
			
			a_oListValues[j], a_oListValues[j + 1] = nRhs, nLhs


# 값을 출력한다
def printValues(a_oListValues):
	for nVal in a_oListValues:
		print(f"{nVal}, ", end = "")
	
	print()
