import os
import sys

from Example.Example_18.CException import CException

"""
예외 처리 (Exception Handling) 란?
- 프로그램이 실행 되는 도중 발생하는 의도치 않은 상황에 대처하는 것을 의미한다. (+ 즉, 예외 처리는
프로그램을 좀 더 안전하게 제작하는 방법이라는 것을 알 수 있다.)

사용자는 항상 프로그래머의 의도대로 프로그램을 사용하지 않기 때문에 의도치 않은 상황을 대처해서 프로그램을
제작하는 것이 중요하다. (+ 즉, 의도치 않은 상황을 잘 대처 할 필요가 있다.)

Python 은 예외 처리 기능을 제공하며 잘못 된 데이터을 기반으로 명령문을 실행하거나 연산을 처리 할 경우
내부적으로 예외가 발생하도록 설계 되어있다. (+ 즉, 발생 된 예외를 처리하지 않을 경우 프로그램이
중단 된다는 것을 의미한다.)

Python 예외 종류
- SyntaxError				<- 문법 오류
- ZeroDivisionError			<- 0 으로 나누기 시도
- AttributeError			<- 객체에 존재하지 않는 변수 / 메서드 호출
- 등등...

위와 같이 Python 은 다양한 예외를 지원하며 Exception 클래스를 상속함으로서 직접 예외를 정의하는 것도 가능하다.

Ex)
class CSomeException(Exception):
	def __init__(self, a_oMsg):
		# Do Something
		
위와 같이 Exception 클래스를 상속하면 특정 상황에 맞는 예외를 직접 정의하는 것이 가능하다. (+ 즉,
직접 정의 한 예외는 raise 키워드를 이용해서 명시적으로 예외를 발생 시키는 것이 가능하다.)

Python 예외 처리 관련 키워드
- try
- except
- finally
- raise

try 키워드란?
- 예외 발생 가능한 블럭을 지정하는 역할을 수행하는 키워드를 의미한다. (+ 즉,
try 블럭 내부에 작성 된 명령문에서 발생 한 예외는 Python 의 예외 처리 기능을 활용해서 대처하는 것이 가능하다.)

try 블럭 내부에서 예외가 발생 할 경우 프로그램의 흐름은 즉시 중단되고 예외가 전파되는 특징이 존재한다. (+ 즉,
예외가 발생한 명령문 이후에 존재하는 명령문은 실행되지 않는다는 것을 의미한다.)

except 키워드란?
- 발생한 예외를 처리하기 위한 명령문을 작성 할 수 있는 키워드를 의미한다. (+ 즉,
try 블럭 내부에서 예외가 발생하면 except 블럭에서 발생한 예외를 처리하는 것이 가능하다.)

except 키워드를 통해 발생한 예외를 처리했더라도 raise 키워드를 활용하면 다시 예외를 발생 시키는 것이
가능하다. (+ 즉, except 블럭 내부에서 발생 한 예외는 해당 메서드를 호출 한 곳으로 전파 된다는 것을
알 수 있다.)

finally 키워드란?
- try 블럭에서 예외가 발생 하더라도 반드시 실행 할 명령문을 작성 할 수 있는 키워드를 의미한다. (+ 즉,
finally 블럭 내부에 작성한 명령문은 반드시 실행 된다는 것을 알 수 있다.)

따라서 스트림과 같은 컴퓨터 자원을 해제 할 때 finally 블럭을 활용하면 안전하게 자원을 해제하는 것이
가능하다. (+ 즉, try 블럭에서 예외가 발생 하더라도 finally 블럭에 의해 자원을 해제하는 것이 가능하다.)

raise 키워드란?
- 예외를 명시적으로 발생 시키는 키워드를 의미한다. (+ 즉, raise 키워드를 활용하면
잘못 된 데이터나 상황을 처리 할 수 있게 예외를 명시적으로 발생 시키는 것이 가능하다.)

Ex)
try:
	# 예외 발생 가능한 명령문

except:
	# try 블럭에서 발생한 예외 처리 명령문

finally:
	# try 블럭에서 예외가 발생해도 반드시 실행 해야 될 명령문
"""


# Example 17 (예외 처리)
def start(args):
	oTokens = input("정수 (2 개) 입력 : ").split()
	
	try:
		nValA = int(oTokens[0])
		nValB = int(oTokens[1])
		
		print("=====> 산술 연산자 <=====")
		print(f"{nValA} + {nValB} = {nValA + nValB}")
		print(f"{nValA} - {nValB} = {nValA - nValB}")
		print(f"{nValA} * {nValB} = {nValA * nValB}")
		print(f"{nValA} / {nValB} = {nValA / nValB}")
		print(f"{nValA} % {nValB} = {nValA % nValB}")
		print(f"{nValA} ** {nValB} = {nValA ** nValB}")
		print(f"{nValA} // {nValB} = {nValA // nValB}")
		
		invokeException()
	
	except IndexError as oException:
		"""
		위와 같이 처리 할 예외를 직접 명시하면 해당 예외만 처리하는 것이 가능하다. (+ 즉,
		직접 명시한 예외만 처리하고 다른 예외는 해당 메서드를 호출 한 곳으로 전파 시킨다는 것을 알 수 있다.)
		"""
		
		print(f"{oException} 예외가 발생했습니다.")
	
	except ZeroDivisionError as oException:
		"""
		위와 같이 except 블럭은 필요에 따라 여러 개를 명시하는 것이 가능하다. (+ 즉,
		처리 할 예외가 여러 개 일 경우 처리하고 싶은 예외 개수만큼 except 블럭을 명시해주면 된다.)

		except 블럭은 위에서 아래 방향으로 순차적으로 검사가 이루어지기 때문에
		먼저 만족 한 except 블럭만 실행 된다. (+ 즉, if ~ else 조건문과 동일한 구조라는 것을 알 수 있다.)
		"""
		
		print(f"{oException} 예외가 발생했습니다.")
	
	except:
		"""
		위와 같이 처리 할 예외를 명시하지 않으면 모든 예외를 처리하는 것이 가능하지만 어떤 예외가 발생했는지
		구분하는 것은 불가능하다. (+ 즉, 예외를 구분해서 처리하고 싶다면 처리 할 예외를 직접 명시해줘야한다.)
		"""
		
		print("예외가 발생했습니다.")


# 예외를 발생 시킨다
def invokeException():
	try:
		"""
		아래와 같이 raise 키워드를 활용하면 예외를 직접 발생 시키는 것이 가능하다. (+ 즉,
		raise 키워드를 활용하면 예외를 해당 메서드를 호출 한 곳으로 전파 시키는 것이 가능하다.)
		"""
		raise CException("사용자 정의 예외 발생")
	
	finally:
		print("finally 블럭이 실행 되었습니다.")
		