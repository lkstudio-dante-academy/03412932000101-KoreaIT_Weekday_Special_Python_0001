import os
import sys

"""
중첩 반복문이란?
- 반복문 내부에 반복문을 작성하는 구조를 의미한다. (+ 즉, 반복문은 필요에 따라 중첩이 가능하다는 것을
의미한다.)

Ex)
for i in range(0, 10):
	for j in range(0, 10):
		# Do Something

위와 같이 반복문 내부에 반복문을 작성하면 외부 반복문이 반복 할 때마다 내부 반복문이 실행 된다는 것을
알 수 있다. (+ 즉, 위의 경우 내부 반복문은 10 번 실행 된다는 것을 알 수 있다.)
"""


# Example 7 (반복문 - 2)
def start(args):
	for i in range(2, 10):
		print(f"=====> {i} 단 <=====")
		
		for j in range(1, 10):
			print(f"{i} * {j} = {i * j}")
			
		print()
		