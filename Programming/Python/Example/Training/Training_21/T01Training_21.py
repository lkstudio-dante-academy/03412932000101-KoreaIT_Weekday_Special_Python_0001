import os
import sys

from Training.Training_21.CFactory_Unit import CFactory_Unit

"""
Python 연습 문제 21
- 유닛 생산 시뮬레이션 제작하기
- 유닛은 3 종류가 존재한다
- 사용자로부터 메뉴를 선택 받아 유닛을 생성한다
- 단, 유닛 생산에는 비용이 필요하며 비용이 부족 할 경우 유닛 생산 불가
- 초기 비용은 프로그램 시작 시 사용자로부터 입력 받는다

Ex)
소지 금액 입력 : 1000

=====> 메뉴 <=====
1. 유닛 A 생산 (가격 : 250)
2. 유닛 B 생산 (가격 : 500)
3. 유닛 C 생산 (가격 : 750)
4. 생산 된 유닛 정보 출력
5. 종료

선택 (소지 금액 : 1000) : 1
유닛 A 을(를) 생산했습니다.

선택 (소지 금액 : 750) : 2
유닛 B 을(를) 생산했습니다.

선택 (소지 금액 : 250) : 4
유닛 A 을(를) {시간} 에 생산했습니다.
유닛 B 을(를) {시간} 에 생산했습니다.
"""


# Training 21
def start(args):
	nAmount = int(input("소지 금액 입력 : "))
	oListUnits = []
	
	while True:
		printMenu()
		nMenu = int(input(f"\n선택 (소지 금액 : {nAmount}) : "))
		
		# 종료 일 경우
		if nMenu == MENU_EXIT:
			break
			
		# 유닛 생산 일 경우
		if nMenu != MENU_SHOW_INFOS_ALL_UNIT:
			oClass_Unit = CFactory_Unit.getInst().getClass_Unit(nMenu - 1)
			
			# 금액이 부족 할 경우
			if nAmount < oClass_Unit.PRICE:
				print("금액이 부족합니다.")
				continue
			
			oUnit = CFactory_Unit.getInst().createUnit(nMenu - 1)
			oListUnits.append(oUnit)
			
			nAmount -= oClass_Unit.PRICE
			print(f"{oClass_Unit.NAME} 을(를) 생산했습니다.")
			
		else:
			for oUnit in oListUnits:
				oClass_Unit = CFactory_Unit.getInst().getClass_Unit(oUnit.m_nIdx)
				print(f"{oClass_Unit.NAME} 은(는) {oUnit.m_oTime} 에 생산했습니다.")
				
		print()
		
	print("프로그램을 종료합니다.")


MENU_SHOW_INFOS_ALL_UNIT = CFactory_Unit.getInst().getNumKinds_Unit() + 1
MENU_EXIT = CFactory_Unit.getInst().getNumKinds_Unit() + 2

# 메뉴를 출력한다
def printMenu():
	print("=====> 메뉴 <=====")
	nNumKinds_Unit = CFactory_Unit.getInst().getNumKinds_Unit()
	
	for i in range(0, nNumKinds_Unit):
		oClass_Unit = CFactory_Unit.getInst().getClass_Unit(i)
		print(f"{i + 1}. {oClass_Unit.NAME} 생산 (가격 : {oClass_Unit.PRICE})")
		
	print(f"{MENU_SHOW_INFOS_ALL_UNIT}. 생산 된 유닛 정보 출력")
	print(f"{MENU_EXIT}. 종료")
	