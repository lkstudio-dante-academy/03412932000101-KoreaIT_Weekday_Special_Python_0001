import os
import sys

"""
연산자 (Operator) 란?
- 데이터나 프로그램의 흐름을 제어하기 위한 특별한 의미를 지니는 기호 (심볼) 를 의미한다. (+ 즉, 연산자를 활용하면
데이터를 프로그램의 목적에 맞게 처리하는 것이 가능하다.)

Python 연산자 종류
- 산술 연산자 (+, -, *, /, %, **, //)
- 관계 연산자 (<, >, <=, >=, ==, !=)
- 논리 연산자 (and, or, not)
- 비트 연산자 (&, |, ^, <<, >>, ~)
- 할당 연산자 (=, +=, -=, *=, /= 등등...)
- 기타 연산자 (type, 조건 연산자 등등...)
"""


# Example 4 (연산자)
def start(args):
	"""
	split 함수란?
	- 문자열을 특정 문자를 기준으로 분할하는 역할을 수행하는 함수를 의미한다. (+ 즉, split 함수를 활용하면
	문자열을 여러 문자열로 나누는 것이 가능하다.)
	
	split 함수는 입력 데이터로 기준이 되는 문자를 요구하며 만약 해당 문자를 명시하지 않을 경우
	공백을 기준으로 문자열을 분할한다.
	
	split 함수를 통해 분할 된 문자열은 리스트의 현태로 반환되기 때문에
	[] (인덱스 연산자) 와 인덱스 번호를 통해서 특정 위치에 있는 데이터를 제어하는 것이 가능하다. (+ 단,
	인덱스 번호는 0 부터 시작하기 때문에 주의가 필요하다.)
	"""
	oTokens = input("정수 (2 개) 입력 : ").split()
	
	"""
	int 와 같은 자료형을 활용하면 숫자로 이루어진 문자열를 해당 자료형의 데이터로 변환하는 것이 가능하다.
	(+ 즉, int 를 활용하면 숫자로 이루어진 문자열을 정수 데이터로 변환하는 것이 가능하다.)
	
	단, 숫자가 아닌 문자가 문자열에 포함되어있을 경우 예외가 발생하기 때문에 주의가 필요하다. (+ 즉,
	크래시가 발생한다는 것을 알 수 있다.)
	
	Ex)
	int("10")				<- 정수 10 로 변환
	float("3.14")			<- 실수 3.14 로 변환
	
	위와 같이 숫자로 이루어진 문자열이 해당 자료형 데이터로 변환 된다는 것을 알 수 있다.
	"""
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
	
	"""
	컴퓨터는 0 을 제외한 모든 수를 참으로 인식하지만 Python 은 참 or 거짓을 의미하는 True or False 데이터를
	제공한다. (+ 즉, Python 에서 거짓을 나타내기 위해서는 0 or False 를 명시하면 된다는 것을 알 수 있다.)
	"""
	print("\n=====> 관계 연산자 <=====")
	print(f"{nValA} < {nValB} = {nValA < nValB}")
	print(f"{nValA} > {nValB} = {nValA > nValB}")
	print(f"{nValA} <= {nValB} = {nValA <= nValB}")
	print(f"{nValA} >= {nValB} = {nValA >= nValB}")
	print(f"{nValA} == {nValB} = {nValA == nValB}")
	print(f"{nValA} != {nValB} = {nValA != nValB}")
	
	print("\n=====> 논리 연산자 <=====")
	print(f"{nValA} and {nValB} = {nValA and nValB}")
	print(f"{nValA} or {nValB} = {nValA or nValB}")
	print(f"not {nValA} = {not nValA}")
	
	"""
	조건 연산자는 if ~ else 조건문을 단순화시킨 기능을 의미한다. (+ 즉, 간단한 명령문은 조건 연산자로
	대체하는 것이 가능하다.)
	
	조건 연산자는 if 조건문이 참 일 경우 if 기호의 왼쪽 데이터를 반환하는 반면 거짓 일 경우
	else 기호의 오른쪽 데이터를 반환한다.
	
	Ex)
	nValA = 10
	nValB = 20
	
	nResult = nValA if nValA >= nValB else nValB
	
	위의 경우 조건 연산자에 의해 nResult 변수에는 nValA 변수와 nValB 변수가 지니고 있는
	데이터 중 큰 데이터가 할당 된다는 것을 알 수 있다.
	"""
	nVal_Max = nValA if nValA >= nValB else nValB
	
	print("\n=====> 조건 연산자 <=====")
	print(f"{nValA} if {nValA} > {nValB} else {nValB} = {nVal_Max}")
	
	"""
	컴퓨터는 음수에 대한 계산을 단순화시키기 위해서 음수를 2 의 보수법으로 표현한다. (+ 즉,
	음수를 2 의 보수법으로 표현함으로서 덧셈 연산을 통해 간단하게 음수에 대한 결과를 계산하는 것이 가능하다.)
	
	Ex)
	0101			<- 5
	1011			< -5
	
	위와 같이 2 의 보수는 1 의 보수를 구한 다음에 +1 을 더해줌으로서 간단하게 계산하는 것이 가능하다.
	"""
	print("\n=====> 비트 연산자 <=====")
	print(f"{nValA:#b} & {nValB:#b} = {nValA & nValB:#b}")
	print(f"{nValA:#b} | {nValB:#b} = {nValA | nValB:#b}")
	print(f"{nValA:#b} ^ {nValB:#b} = {nValA ^ nValB:#b}")
	print(f"{nValA:#b} << 1 = {nValA << 1:#b}")
	print(f"{nValA:#b} >> 1 = {nValA >> 1:#b}")
	print(f"~{nValA:#b} = {~nValA:#b}")
