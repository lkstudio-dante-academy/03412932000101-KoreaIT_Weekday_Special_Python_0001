import os
import sys
import random

from Training.Training_22.CUnit import CMarine, CFirebat, CGhost


# Training 22
def start(args):
	oListUnits = []
	
	while True:
		printMenu()
		nMenu = int(input("\n선택 : "))
		
		# 종료 일 경우
		if nMenu == MENU_EXIT:
			break
			
		# 유닛 생산 일 경우
		if nMenu != MENU_ATTACK_ALL_UNITS:
			oUnit = createUnit(nMenu)
			oListUnits.append(oUnit)
			
			oClass_Unit = type(oUnit)
			nRange_Attack = oUnit.m_nRange_Attack
			
			print(f"사정 거리 {nRange_Attack} {oClass_Unit.NAME} 을(를) 추가했습니다.\n")
			continue
			
		nRange_Enemy = random.randrange(1, 15)
		print(f"적이 사정 거리 {nRange_Enemy} 범위에 등장했습니다.")
		
		print("\n=====> 모든 유닛 공격 결과 <=====")
		
		for oUnit in oListUnits:
			oUnit.attack(nRange_Enemy)
			
		print()
		
	print("프로그램을 종료합니다.")


MENU_ATTACK_ALL_UNITS = 4
MENU_EXIT = 5

# 메뉴를 출력한다
def printMenu():
	print("=====> 메뉴 <=====")
	print("1. 마린 추가 (사정 거리 : 5 ~ 8)")
	print("2. 파이이 벳 추가 (사정 거리 : 2 ~ 5)")
	print("3. 고스트 추가 (사정 거리 : 8 ~ 11)")
	print("4. 모든 유닛 공격 지시")
	print("5. 종료")
	
	
# 유닛을 생성한다
def createUnit(a_nMenu):
	oListInfos_Range = [
		(), (5, 8), (2, 5), (8, 11)
	]
	
	oInfo_Range = oListInfos_Range[a_nMenu]
	nRange_Attack = random.randrange(oInfo_Range[0], oInfo_Range[1] + 1)
	
	oListClasses_Unit = [
		None, CMarine, CFirebat, CGhost
	]
	
	return oListClasses_Unit[a_nMenu](nRange_Attack)
