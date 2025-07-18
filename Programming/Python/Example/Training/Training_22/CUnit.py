import os
import sys


# 유닛
class CUnit:
	# 초기화
	def __init__(self, a_nRange):
		self.m_nRange_Attack = a_nRange
		
	# 공격 가능 여부를 검사한다
	def isEnable_Attack(self, a_nRange):
		return a_nRange <= self.m_nRange_Attack
	
	# 적을 공격한다
	def attack(self, a_nRange):
		oMsgA = f"사정 거리 {self.m_nRange_Attack}"
		
		# 공격이 가능 할 경우
		if self.isEnable_Attack(a_nRange):
			oMsgB = self.attack_Internal()
		
		else:
			oMsgB = "공격에 실패했습니다."
			
		oClass_Unit = type(self)
		print(f"{oMsgA} {oClass_Unit.NAME} 이(가) {oMsgB}")
		
	# 적을 공격한다
	def attack_Internal(self):
		pass
	
	
# 마린
class CMarine(CUnit):
	NAME = "마린"
	
	# 초기화
	def __init__(self, a_nRange):
		super().__init__(a_nRange)
	
	# 적을 공격한다
	def attack_Internal(self):
		return "적을 향해 총을 발사했습니다."
	

# 파이어 벳
class CFirebat(CUnit):
	NAME = "파이어 벳"
	
	# 초기화
	def __init__(self, a_nRange):
		super().__init__(a_nRange)
	
	# 적을 공격한다
	def attack_Internal(self):
		return "적을 향해 화염 방사기를 방사했습니다."
	

# 고스트
class CGhost(CUnit):
	NAME = "고스트"
	
	# 초기화
	def __init__(self, a_nRange):
		super().__init__(a_nRange)
		
	# 적을 공격한다
	def attack_Internal(self):
		return "적을 향해 장총을 발사했습니다."
	