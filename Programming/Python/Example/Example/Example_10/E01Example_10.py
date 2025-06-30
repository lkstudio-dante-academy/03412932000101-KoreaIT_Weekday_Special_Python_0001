import os
import sys

"""
리스트 컴프리헨션 (List Comprehension) 이란?
- 열거 가능한 데이터를 기반으로 리스트를 생성 할 수 있는 기능을 의미한다. (+ 즉, 리스트 컴프리헨션을 활용하면
좀 더 간단한 방법으로 여러 데이터를 지니고 있는 리스트를 생성하는 것이 가능하다.)

Ex)
oListValues = [i + 1 for i in range(0, 10)]			<- [1, 2, 3, ..., 10] 리스트 생성

위와 같이 리스트 컴프리헨션을 활용하면 리스트를 생성하는 명령문과 리스트에 값을 추가하는 명령문을
따로 작성하지 않아도 된다는 것을 알 수 있다.

딕셔너리 컴프리헨션 (Dictionary Comprehension) 이란?
- 리스트 컴프리헨션과 마찬가지로 열거 가능한 데이터를 기반으로 딕셔너리를 생성 할 수 있는 기능을 의미한다. (+ 즉,
딕셔너리 컴프리헨션을 활용하면 좀 더 간단한 방법으로 다양한 데이터를 지니고 있는 딕셔너리를 생성하는 것이 가능하다.)

Ex)
oDictValues = {str(i + 1): i + 1 for i in range(0, 10)]			<- {"1": 1, ..., "10": 10} 딕셔너리 생성

위와 같이 딕셔너리 컴프리헨션을 활용하면 리스트 컴프리헨션과 마찬가지로 딕셔너리를 생성하는 명령문과
딕셔너리에 값을 추가하는 명령문을 따로 작성하지 않아도 된다는 것을 알 수 있다.
"""


# Example 9 (컬렉션 - 3)
def start(args):
	"""
	아래와 같이 리스트 컴프리헨션은 필요에 따라 조건문을 사용하는 것이 가능하다. (+ 즉, 조건문을 통해
	특정 조건을 만족하는 데이터만으로 리스트를 생성하는 것이 가능하다.)
	
	또한 리스트 컴프리헨션에 사용되는 반복문은 중첩 시키는 것이 가능하다. (+ 즉, 필요에 따라 원하는 만큼
	반복문을 중첩해서 리스트를 생성하는 것이 가능하다.)
	"""
	oListValuesA = [i + 1 for i in range(0, 10)]
	oListValuesB = [i + 1 for i in range(0, 10) if (i + 1) % 2 != 0]
	oListValuesC = [i + j for i in range(0, 10) if (i + 1) % 2 != 0 for j in range(0, 10) if (j + 1) % 2 != 0]
	
	print("=====> 리스트 컴프리헨션 <=====")
	print(f"리스트 A : {oListValuesA}")
	print(f"리스트 B : {oListValuesB}")
	print(f"리스트 C : {oListValuesC}")
	
	"""
	아래와 같이 딕셔너리 또한 리스트 컴프리헨션과 같이 조건문과 반복문을 중첩 시키는 것이 가능하다.
	"""
	oDictValuesA = {f"Key_{i + 1:02}": i + 1 for i in range(0, 10)}
	oDictValuesB = {f"Key_{i + 1:02}": i + 1 for i in range(0, 10) if (i + 1) % 2 != 0}
	oDictValuesC = {f"Key_{i + j:02}": i + j for i in range(0, 10) if (i + 1) % 2 != 0 for j in range(0, 10) if (j + 1) % 2 != 0}
	
	print("\n=====> 딕셔너리 컴프리헨션 <=====")
	print(f"딕셔너리 A : {oDictValuesA}")
	print(f"딕셔너리 B : {oDictValuesB}")
	print(f"딕셔너리 C : {oDictValuesC}")
