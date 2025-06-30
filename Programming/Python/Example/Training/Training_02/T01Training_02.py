import os
import sys

"""
Python 연습 문제 2
- 세부 학점 계산하기
- 점수를 입력 받아 해당 점수에 해당하는 학점 출력한다

세부 학점 범위
- + : 7 ~ 9
- 0 : 4 ~ 6
- - : 0 ~ 3

Ex)
점수 입력 : 85
학점 : B0
"""


# Training 2
def start(args):
	nScore = int(input("점수 입력 : "))
	
	oGrade = ""
	oGrade_Detail = ""
	
	if nScore < 60:
		oGrade = "F"
	
	else:
		if nScore >= 90:
			oGrade = "A"
		
		elif nScore >= 80:
			oGrade = "B"
		
		elif nScore >= 70:
			oGrade = "C"
		
		else:
			oGrade = "D"
		
		nScore_Detail = nScore % 10
		
		# + 일 경우
		if nScore >= 100 or nScore_Detail >= 7:
			oGrade_Detail = "+"
		
		else:
			oGrade_Detail = "-" if nScore_Detail <= 3 else "0"
	
	print(f"{oGrade}{oGrade_Detail} 학점입니다.")
