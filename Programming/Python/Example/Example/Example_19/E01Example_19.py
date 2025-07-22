import os
import sys

import random
from Example.Example_19.Search import findVal_ByLinear, findVal_ByBinary

"""
탐색 (Search) 이란?
- 데이터의 집합으로부터 특정 데이터를 찾아오는 것을 의미한다. (+ 즉, 원하는 데이터를 찾는 행위를 의미한다.)

탐색 알고리즘 종류
- 선형 탐색
- 이진 탐색
- 해시 탐색
"""


# Example 19 (탐색)
def start(args):
	oListValues = [random.randrange(1, 100) for i in range(0, 10)]
	oListValues.sort()
	
	print("=====> 리스트 <=====")
	print(oListValues)
	
	nVal = int(input("\n정수 입력 : "))
	
	# nResult = findVal_ByLinear(oListValues, nVal)
	nResult = findVal_ByBinary(oListValues, nVal)
	
	print(f"결과 : {nResult}")
	