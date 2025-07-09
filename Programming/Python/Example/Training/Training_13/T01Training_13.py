import os
import sys


# Training 13
def start(args):
	MENU_ADD_MEMBER = 1
	MENU_REMOVE_MEMBER = 2
	MENU_SEARCH_MEMBER = 3
	MENU_SHOW_MEMBERS_ALL = 4
	MENU_EXIT = 5
	
	nMenu = 0
	oDictMembers = {}
	
	while nMenu != MENU_EXIT:
		print("=====> 메뉴 <=====")
		print("1. 회원 추가")
		print("2. 회원 제거")
		print("3. 회원 검색")
		print("4. 모든 회원 출력")
		print("5. 종료")
		
		nMenu = int(input("\n선택 : "))
		
		# 회원 추가 일 경우
		if nMenu == MENU_ADD_MEMBER:
			oName = input("이름 입력 : ")
			oPNumber = input("전화 번호 입력 : ")
			
			# 회원이 존재 할 경우
			if oName in oDictMembers:
				print(f"{oName} 은(는) 이미 존재하는 회원입니다.")
			
			else:
				oMember = (oName, oPNumber)
				oDictMembers[oName] = oMember
				
				print(f"{oName} 을(를) 추가했습니다.")
		
		# 회원 제거 일 경우
		elif nMenu == MENU_REMOVE_MEMBER:
			oName = input("이름 입력 : ")
			
			# 회원이 존재 할 경우
			if oName in oDictMembers:
				del oDictMembers[oName]
				print(f"{oName} 을(를) 제거했습니다.")
			
			else:
				print(f"{oName} 은(는) 존재하지 않습니다.")
		
		# 회원 검색 일 경우
		elif nMenu == MENU_SEARCH_MEMBER:
			oName = input("이름 입력 : ")
			
			# 회원이 존재 할 경우
			if oName in oDictMembers:
				oMember = oDictMembers[oName]
				
				print("=====> 회원 정보 <=====")
				print(f"이름 : {oMember[0]}")
				print(f"전화 번호 : {oMember[1]}")
			
			else:
				print(f"{oName} 은(는) 존재하지 않습니다.")
		
		# 모든 회원 출력 일 경우
		elif nMenu == MENU_SHOW_MEMBERS_ALL:
			print("=====> 모든 회원 정보 <=====")
			
			for oKey, oMember in oDictMembers.items():
				print(f"이름 : {oMember[0]}")
				print(f"전화 번호 : {oMember[1]}\n")
		
		print()
	
	print("프로그램을 종료합니다.")
	