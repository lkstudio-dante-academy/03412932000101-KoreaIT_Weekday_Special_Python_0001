import os
import sys

import random
from Example.Example_21.Sorting import sortValues_BySelection, sortValues_ByHeap, sortValues_ByQuick

"""
불안정 정렬 알고리즘 종류
- 선택 정렬 (Selection Sort)
- 힙 정렬 (Heap Sort)
- 퀵 정렬 (Quick Sort)
"""


# Example 21 (정렬 - 2)
def start(args):
	oListValues = [random.randrange(1, 100) for i in range(0, 10)]
	
	print("=====> 리스트 - 정렬 전 <=====")
	print(oListValues)
	
	sortValues_BySelection(oListValues)
	# sortValues_ByHeap(oListValues)
	# sortValues_ByQuick(oListValues)
	
	print("\n=====> 리스트 - 정렬 후 <=====")
	print(oListValues)
