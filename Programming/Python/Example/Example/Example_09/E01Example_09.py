import os
import sys

import random

"""
비선형 컬렉션 (Non Linear Collection) 란?
- 내부적으로 데이터를 복잡한 형태로 관리하는 컬렉션을 의미한다. (+ 즉, 비선형 컬렉션은 선형 컬렉션에 비해
내부 동작이 복잡하다는 것을 알 수 있다.)

비선형 컬렉션은 데이터를 복잡한 형태로 관리하기 때문에 선형 컬렉션에 비해 구현 난이도가 높지만 많은 데이터를
효율적으로 관리 할 수 있다는 장점이 존재한다. (+ 즉, 비선형 컬렉션은 관리되는 데이터의 개수가 많을수록 성능이
뛰어나다는 것을 알 수 있다.)

Python 비선형 컬렉션 종류
- 셋 (Set)
- 딕셔너리 (Dictionary)

셋 (Set) 이란?
- 관리되는 데이터의 중복을 허용하지 않는 컬렉션을 의미한다. (+ 즉, 셋은 수학의 집합의 특징을 지니고 있다는 것을
알 수 있다.)

딕셔너리 (Dictionary) 란?
- 탐색에 특화 된 컬렉션을 의미한다. (+ 즉, 딕셔너리는 데이터가 많을수록 효율적이라는 것을 알 수 있다.)

딕셔너리는 키/벨류 쌍으로 데이터를 관리하기 때문에 다른 컬렉션에 비해 메모리 사용량이 높으며 사용 방법이
조금 복잡하다는 단점이 존재한다.

키 (Key) 데이터는 데이터를 제어하기 위한 식별자이기 때문에 중복을 허용하지 않지만 벨류 (Value) 는
딕셔너리를 통해 실제 관리 할 데이터에 해당하기 때문에 중복이 허용 된다. (+ 즉, 딕셔너리는 키를 통해 벨류를
제어하는 컬렉션이라는 것을 알 수 있다.)
"""


# Example 8 (컬렉션 - 2)
def start(args):
	print("=====> 데이터 입력 <=====")
	oSetValues = set()
	
	for i in range(0, 10):
		nVal = random.randrange(1, 10)
		print(f"{nVal}, ", end = "")
		
		"""
		add 함수를 활용하면 셋에 데이터를 추가하는 것이 가능하다. (+ 즉, add 함수는 내부적으로 데이터의
		중복 여부를 검사 후 새로운 데이터를 추가한다는 것을 알 수 있다.)
		"""
		oSetValues.add(nVal)
	
	print("\n\n=====> 셋 <=====")
	
	for nVal in oSetValues:
		print(f"{nVal}, ", end = "")
	
	print(f"\n\n개수 : {len(oSetValues)}")
	oDictValues = dict()
	
	for i in range(0, 10):
		oKey = f"Key_{i + 1:02}"
		
		"""
		딕셔너리에 키를 지정해서 벨류 (데이터) 를 할당하면 데이터가 추가 된다.
		
		만약 딕셔너리에 이미 동일한 키에 해당하는 벨류가 존재 할 경우 해당 벨류를 새로운 벨류로 덮어쓴다는
		것을 알 수 있다. (+ 즉, 변수와 값이 기존에 존재하던 벨류는 사라진다는 것을 알 수 있다.)
		"""
		oDictValues[oKey] = i + 1
	
	print("\n=====> 딕셔너리 <=====")
	
	"""
	items 함수를 활용하면 키/벨류 쌍으로 이루어진 데이터를 가져오는 것이 가능하다. (+ 즉, items 함수는
	내부적으로 키/벨류 쌍으로 이루어진 데이터의 리스트를 반환한다는 것을 알 수 있다.)
	
	for 반복문에 딕셔너리 데이터를 명시 할 경우 키 데이터만을 가져오기 때문에 딕셔너리를 순회하는데
	번거로움이 존재한다.
	
	Ex)
	oDictValues = { "Key_01":1, "Key_02":2, "Key_03":3 }
	
	for oKey in oDictValues:
		nVal = oDictValues[oKey]
		
	위와 같이 for 반복문 내부에서 벨류를 가져오기 위한 별도의 명령문이 필요하다는 것을 알 수 있다.
	"""
	for oKey, nVal in oDictValues.items():
		print(f"{oKey}:{nVal}, ", end = "")
	
	oKey_Remove = input("\n\n키 입력 (제거) : ")
	
	"""
	리스트와 마찬가지로 del 키워드를 이용하면 딕셔너리에 존재하는 데이터를 제거하는 것이 가능하다. (+ 즉,
	딕셔너리에 존재하지 않는 데이터를 제거 할 경우 예외가 발생한다는 것을 알 수 있다.)
	"""
	del oDictValues[oKey_Remove]
	
	print("\n=====> 딕셔너리 - 제거 후 <=====")
	
	for oKey, nVal in oDictValues.items():
		print(f"{oKey}:{nVal}, ", end = "")
	
	print()
