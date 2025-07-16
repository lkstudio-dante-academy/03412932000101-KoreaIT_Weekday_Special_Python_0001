import os
import sys

from Training.Training_20.CManager_Member import CManager_Member

"""
Python 연습 문제 20
- 회원 관리 프로그램 제작하기 (+ 클래스 활용)
- 요구 사항은 연습 문제 12 번 참고
"""


# Training 20
def start(args):
	MENU_ADD_MEMBER = 1
	MENU_REMOVE_MEMBER = 2
	MENU_SEARCH_MEMBER = 3
	MENU_SHOW_MEMBERS_ALL = 4
	MENU_EXIT = 5
	
	nMenu = 0
	oManager = CManager_Member()
	
	while True:
		print("=====> 메뉴 <=====")
		print("1. 회원 추가")
		print("2. 회원 제거")
		print("3. 회원 검색")
		print("4. 모든 회원 출력")
		print("5. 종료")
		
		nMenu = int(input("\n선택 : "))
		
		# 종료 일 경우
		if nMenu == MENU_EXIT:
			break
		
		# 회원 추가 일 경우
		if nMenu == MENU_ADD_MEMBER:
			addMember(oManager)
		
		# 회원 제거 일 경우
		elif nMenu == MENU_REMOVE_MEMBER:
			removeMember(oManager)
		
		# 회원 검색 일 경우
		elif nMenu == MENU_SEARCH_MEMBER:
			searchMember(oManager)
		
		# 모든 회원 출력 일 경우
		elif nMenu == MENU_SHOW_MEMBERS_ALL:
			showMembers_All(oManager)
		
		print()
	
	print("프로그램을 종료합니다.")


# 회원을 추가한다
def addMember(a_oManager):
	oName = input("이름 입력 : ")
	oPNumber = input("전화 번호 입력 : ")
	
	nResult = a_oManager.findMember(oName)
	
	# 회원이 존재 할 경우
	if nResult >= 0:
		print(f"{oName} 은(는) 이미 존재하는 회원입니다.")
		
	else:
		a_oManager.addMember(oName, oPNumber)
		print(f"{oName} 을(를) 추가했습니다.")
		

# 회원을 제거한다
def removeMember(a_oManager):
	oName = input("이름 입력 : ")
	nResult = a_oManager.findMember(oName)
	
	# 회원이 존재 할 경우
	if nResult >= 0:
		a_oManager.removeMember(oName)
		print(f"{oName} 을(를) 제거했습니다.")
	
	else:
		print(f"{oName} 은(는) 존재하지 않습니다.")
		

# 회원을 검색한다
def searchMember(a_oManager):
	oName = input("이름 입력 : ")
	nResult = a_oManager.findMember(oName)
	
	# 회원이 존재 할 경우
	if nResult >= 0:
		a_oManager.searchMember(oName)
		
	else:
		print(f"{oName} 은(는) 존재하지 않습니다.")


# 모든 회원 정보를 출력한다
def showMembers_All(a_oManager):
	print("=====> 모든 회원 정보 <=====")
	a_oManager.showMembers_All()
	