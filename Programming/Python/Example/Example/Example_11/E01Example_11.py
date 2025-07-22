import os
import sys

"""
함수 (Function) 란?
- 명령문의 일부 or 전체를 따로 분리해서 재사용 할 수 있는 기능을 의미한다. (+ 즉, 함수를 활용하면 중복적으로
발생하는 명령문을 최소화 시키는 것이 가능하다.)

함수 내부에는 명령문이 존재하며 해당 명령문은 함수가 호출 (실행) 되면 동작한다. (+ 즉, 함수가 호출되지 않으면
함수 내부에 존재하는 명령문은 동작하지 않는다는 것을 알 수 있다.)

Python 의 함수는 수학에서의 함수와 달리 입력과 출력이 존재하거나 없을 수 있다는 차이점이 존재한다. (+ 즉,
입력과 출력의 존재 여부에 따라 4 가지 유형이 존재한다는 것을 알 수 있다.)

Python 함수 유형
- 입력 O, 출력 O
- 입력 O, 출력 X
- 입력 X, 출력 O
- 입력 X, 출력 X

Python 함수 구현 방법
- def + 함수 이름 + 매개 변수 (입력) + 함수 몸체

Ex)
def someFunc(a_nValA, a_nValB):
	return a_nValA + a_nValB
	
nVal = someFunc(10, 20)

위와 같이 함수를 호출 (실행) 하면 함수 내부에 존재하는 명령문이 동작한다는 것을 알 수 있다.

Python 변수 종류
- 지역 변수 (Local Variable)
- 전역 변수 (Global Variable)
- 멤버 변수 (Member Variable)			<- 클래스 주제에서 다룰 예정

위와 같이 Python 변수가 선언 되는 위치에 따라 다양한 변수가 존재한다. (+ 즉, 변수의 종류에 따라 활용 방식에
차이가 있다는 것을 알 수 있다.)

지역 변수 (Local Variable) 란?
- 특정 지역 내부에 선언 된 변수를 의미한다. (+ 즉, 함수 내부에 선언 된 변수를 지역 변수라고 한다는 것을
알 수 있다.)

지역 변수는 해당 변수가 선언 된 함수 내부에서는 유효하지만 함수 외부에서는 접근이 불가능하다는 특징이 존재한다.
(+ 즉, 지역 변수가 선언 된 메서드 하위 지역에서는 접근이 가능하지만 상위 지역에서는 접근이 불가능하다는 것을
알 수 있다.)

Ex)
def someFunc():
	nVal = 0
	print(nVal)
	
print(nVal)			<- 예외 발생

위와 같이 nVal 변수는 someFunc 내부에서 선언 된 지역 변수이기 때문에 someFunc 내부에서는 접근이 가능하지만
someFunc 외부에서 접근을 시도하면 예외가 발생한다는 것을 알 수 있다.

전역 변수 (Global Variable) 란?
- 전역 공간에 선언 된 변수를 의미한다. (+ 즉, 어떤 지역에도 포함되지 않은 영역에 선언 된 변수를
전역 변수라고 한다는 것을 알 수 있다.)

전역 변수는 지역 변수와 달리 프로그램 전체에서 접근이 가능하다. (+ 즉, Python 파일 어디서든지 자유롭게
접근 할 수 있다는 것을 의미한다.)

따라서 전역 변수에 할당 된 데이터는 프로그램이 종료 되기 전까지 유효하다는 특징이 존재한다.
"""


# Example 11 (함수 - 1)
def start(args):
	oTokens = input("수식 입력 : ").split()
	oOperator = oTokens[1]
	
	nValA = int(oTokens[0])
	nValB = int(oTokens[2])
	
	nResult = getResult_Calc(nValA, oOperator, nValB)
	print(f"결과 : {nResult}")


# 계산 결과를 반환한다
def getResult_Calc(a_nValA, a_oOperator, a_nValB):
	# + 일 경우
	if a_oOperator == "+":
		"""
		return 키워드란?
		- 프로그램의 현재 흐름을 종료하고 함수를 호출한 곳으로 이동시키는 역할을 수행하는 키워드를 의미한다.
		(+ 즉, return 키워드를 활용하면 함수를 즉시 종료 시키는 것이 가능하다.)
		
		또한 return 키워드는 프로그램의 흐름을 함수를 호출한 곳으로 이동시키면서 데이터를 전달하는 것이
		가능하다. (+ 즉, return 키워드에 데이터를 명시 할 경우 해당 데이터를 함수를 호출한 곳으로
		전달한다는 것을 알 수 있다.)
		"""
		return a_nValA + a_nValB
	
	# - 일 경우
	elif a_oOperator == "-":
		return a_nValA - a_nValB
	
	# * 일 경우
	elif a_oOperator == "*":
		return a_nValA * a_nValB
	
	# / 일 경우
	elif a_oOperator == "/":
		return a_nValA / a_nValB
	
	"""
	None 키워드란?
	- 아무런 의미 없는 데이터라는 것을 알리는 역할을 수행하는 키워드를 의미한다. (+ 즉, None 키워드를 활용하면
	자료형에 상관 없이 의미 없는 데이터를 통일 시키는 것이 가능하다.)
	"""
	return None


g_nVal = 0

# 값을 증가 시킨다
def incrVal(a_nVal):
	nVal = 0
	nVal += a_nVal
	
	"""
	global 키워드란?
	- 특정 지역 내부에서 전역 변수를 사용하겠다고 인터프리터에게 알리는 역할을 수행하는 키워드를 의미한다. (+ 즉,
	global 키워드를 활용하면 전역 변수에 자유롭게 접근하는 것이 가능하다.)
	
	단, 지역 내부에 동일한 이름의 지역 변수가 이미 존재 할 경우 내부적으로 예외가 발생하기 때문에
	주의가 필요하다. (+ 즉, 지역 변수와 전역 변수의 이름이 동일 할 경우 해당 변수를 동시에 사용하는 것은
	불가능하다는 것을 알 수 있다.)
	"""
	global g_nVal
	g_nVal += a_nVal
	
	print(f"지역 변수 : {nVal}")
	print(f"전역 변수 : {g_nVal}\n")
