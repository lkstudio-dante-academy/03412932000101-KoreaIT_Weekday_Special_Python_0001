import os
import sys

from Example.Example_24.CQueue import CQueue

"""
큐 (Queue) 란?
- FIFO (First In First Out) or LILO (Last In Last Out) 구조로 데이터를 관리하는 자료구조를 의미한다.
(+ 즉, 큐 또한 스택과 같이 데이터의 입/출력 순서가 엄격하게 관리되는 자료구조라는 것을 알 수 있다.)

큐 관련 용어
- Enqueue			<- 데이터 추가
- Dequeue			<- 데이터 제거
- Front				<- 데이터 제거 위치
- Rear				<- 데이터 추가 위치
"""


# Example 24 (큐)
def start(args):
	oQueueValues = CQueue()
	print("=====> 입력 순서 <=====")
	
	for i in range(0, 10):
		print(f"{i + 1}, ", end = "")
		oQueueValues.enqueue(i + 1)
	
	print("\n\n=====> 큐 <=====")
	
	while not oQueueValues.isEmpty():
		nVal = oQueueValues.dequeue()
		print(f"{nVal}, ", end = "")
		
	print()
	