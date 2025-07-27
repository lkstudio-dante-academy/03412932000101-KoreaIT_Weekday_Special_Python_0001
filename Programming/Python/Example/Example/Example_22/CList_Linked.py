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
		
	# 개수를 반환한다
	def getNumValues(self):
		return self.m_nNumValues
	
	# 값을 반환한다
	def getVal(self, a_nIdx):
		oNode = self.findNode_At(a_nIdx)
		return oNode.m_oNode_Next.m_nVal
	
	# 값을 추가한다
	def addVal(self, a_nVal):
		oNode_Tail = self.m_oNode_Head
		
		while oNode_Tail.m_oNode_Next != None:
			oNode_Tail = oNode_Tail.m_oNode_Next
		
		oNode_Tail.m_oNode_Next = self.createNode(a_nVal)
		self.m_nNumValues += 1
		
		"""
		더미 헤드를 사용하지 않을 경우 아래와 같이 헤드 노드의 존재 여부에 따라 코드가 달라진다는
		단점이 존재한다. (+ 즉, 새로운 값을 추가하는 과정이 통일 되지 않는다는 것을 의미한다.)
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
	
	# 값을 추가한다
	def insertVal(self, a_nIdx, a_nVal):
		oNode = self.findNode_At(a_nIdx)
		
		oNode_New = self.createNode(a_nVal)
		oNode_New.m_oNode_Next = oNode.m_oNode_Next
		
		oNode.m_oNode_Next = oNode_New
		self.m_nNumValues += 1
	
	# 값을 제거한다
	def removeVal(self, a_nVal):
		oNode = self.findNode(a_nVal)
		
		# 값 제거가 불가능 할 경우
		if oNode == None:
			return
		
		oNode_Remove = oNode.m_oNode_Next
		oNode.m_oNode_Next = oNode_Remove.m_oNode_Next
		
		self.m_nNumValues -= 1
	
	# 노드를 탐색한다
	def findNode(self, a_nVal):
		oNode = self.m_oNode_Head
		
		while oNode.m_oNode_Next != None:
			# 값이 존재 할 경우
			if oNode.m_oNode_Next.m_nVal == a_nVal:
				return oNode
			
			oNode = oNode.m_oNode_Next
		
		return None
	
	# 노드를 탐색한다
	def findNode_At(self, a_nIdx):
		oNode = self.m_oNode_Head
		
		for i in range(0, a_nIdx):
			oNode = oNode.m_oNode_Next
			
		return oNode
	
	# 노드를 생성한다
	def createNode(self, a_nVal):
		return CList_Linked.CNode(a_nVal)
