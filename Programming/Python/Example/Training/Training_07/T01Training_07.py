import os
import sys

"""
Python 연습 문제 7
- 삼각형 출력하기
- 라인 수를 입력 받아 해당 라인만큼 삼각형을 출력한다

Ex)
라인 수 입력 : 5
*   *
 * *
  *
 * *
*   *

*****
   *
  *
 *
*****

*   *
**  *
* * *
*  **
*   *

*
**
***
****
*****

*****
****
***
**
*

    *
   **
  ***
 ****
*****

*****
 ****
  ***
   **
    *
    
    *
   ***
  *****
 *******
*********

*********
 *******
  *****
   ***
    *
"""


# Training 7
def start(args):
	nNumLines = int(input("라인 수 입력 : "))
	
	for i in range(0, nNumLines):
		for j in range(0, nNumLines):
			bIsStarA = i == j
			bIsStarB = j == nNumLines - 1 - i
			
			print("*" if bIsStarA or bIsStarB else " ", end = "")
			
		print()
			
	print()
	
	for i in range(0, nNumLines):
		for j in range(0, nNumLines):
			bIsStarA = i == 0
			bIsStarB = i == nNumLines - 1
			bIsStarC = j == nNumLines - 1 - i
			
			print("*" if bIsStarA or bIsStarB or bIsStarC else " ", end = "")
			
		print()
	
	print()
	
	for i in range(0, nNumLines):
		for j in range(0, nNumLines):
			bIsStarA = i == j
			bIsStarB = j == 0
			bIsStarC = j == nNumLines - 1
			
			print("*" if bIsStarA or bIsStarB or bIsStarC else " ", end = "")
			
		print()
	
	print()
	
	for i in range(0, nNumLines):
		for j in range(0, nNumLines):
			bIsStar = j <= i
			print("*" if bIsStar else " ", end = "")
		
		print()
	
	print()
	
	for i in range(0, nNumLines)[::-1]:
		for j in range(0, nNumLines):
			bIsStar = j <= i
			print("*" if bIsStar else " ", end = "")
		
		print()
	
	print()
	
	for i in range(0, nNumLines):
		for j in range(0, nNumLines)[::-1]:
			bIsStar = j <= i
			print("*" if bIsStar else " ", end = "")
		
		print()
	
	print()
	
	for i in range(0, nNumLines)[::-1]:
		for j in range(0, nNumLines)[::-1]:
			bIsStar = j <= i
			print("*" if bIsStar else " ", end = "")
		
		print()
	
	print()
	nWidth_Max = (nNumLines * 2) - 1
	
	for i in range(0, nNumLines):
		nCenter = nWidth_Max // 2
		
		for j in range(0, nWidth_Max):
			bIsStar = j >= nCenter - i and j <= nCenter + i
			print("*" if bIsStar else " ", end = "")
			
		print()
		
	print()
	
	for i in range(0, nNumLines)[::-1]:
		nCenter = nWidth_Max // 2
		
		for j in range(0, nWidth_Max):
			bIsStar = j >= nCenter - i and j <= nCenter + i
			print("*" if bIsStar else " ", end = "")
			
		print()
		