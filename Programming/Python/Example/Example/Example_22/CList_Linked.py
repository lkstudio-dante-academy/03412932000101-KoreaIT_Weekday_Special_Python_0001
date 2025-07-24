import os
import sys


# 연결 리스트
class CList_Linked:
	# 노드
	class CNode:
		# 초기화
		def __init__(self, a_nVal):
			self.m_nVal = a_nVal
			self.m_oNode_Next = None
			
	
	# 초기화
	def __init__(self):
		self.m_nNumValues = 0
		self.m_oNode_Head = self.createNode(0)
	
	# 값을 추가한다
	def addVal(self, a_nVal):
		oNode_Tail = self.m_oNode_Head
		
		while oNode_Tail.m_oNode_Next != None:
			oNode_Tail = oNode_Tail.m_oNode_Next
		
		oNode_Tail.m_oNode_Next = self.createNode(a_nVal)
		self.m_nNumValues += 1
		
		"""
		더미 헤드를 사용하지 않을 경우 아래와 같이 헤드 노드의 존재 여부에 따라 명령문이 달라진다는 단점이
		존재한다. (+ 즉, 새로운 값을 추가하는 과정이 통일 되지 않는다는 것을 의미한다.)
		"""
		# if self.m_oNode_Head == None:
		# 	self.m_oNode_Head = self.createNode(a_nVal)
		#
		# else:
		# 	oNode_Tail = self.m_oNode_Head
		#
		# 	while oNode_Tail.m_oNode_Next != None:
		# 		oNode_Tail = oNode_Tail.m_oNode_Next
		#
		# 	oNode_Tail.m_oNode_Next = self.createNode(a_nVal)
	
	# 노드를 생성한다
	def createNode(self, a_nVal):
		return CList_Linked.CNode(a_nVal)
