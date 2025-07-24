import os
import sys


# 이진 탐색 트리
class CTree_BSearch:
	ORDER_PRE = 0
	ORDER_IN = 1
	ORDER_POST = 2
	
	# 노드
	class CNode:
		# 초기화
		def __init__(self, a_nVal):
			self.m_nVal = a_nVal
			
			self.m_oNode_LChild = None
			self.m_oNode_RChild = None
			
	# 초기화
	def __init__(self):
		self.m_oNode_Root = None
		
	# 값을 추가한다
	def addVal(self, a_nVal):
		# 루트 노드가 없을 경우
		if self.m_oNode_Root == None:
			self.m_oNode_Root = self.createNode(a_nVal)
			return
		
		oNode = self.m_oNode_Root
		oNode_Parent = None
		
		while oNode != None:
			oNode_Parent = oNode
			
			# 값이 작을 경우
			if a_nVal <= oNode.m_nVal:
				oNode = oNode.m_oNode_LChild
				
			else:
				oNode = oNode.m_oNode_RChild
				
		oNode_New = self.createNode(a_nVal)
				
		# 값이 작을 경우
		if a_nVal <= oNode_Parent.m_nVal:
			oNode_Parent.m_oNode_LChild = oNode_New
			
		else:
			oNode_Parent.m_oNode_RChild = oNode_New
			
	# 값을 제거한다
	def removeVal(self, a_nVal):
		oNode_Remove, oNode_Parent = self.findNode(a_nVal)
		
		# 자식 노드가 모두 존재 할 경우
		if oNode_Remove.m_oNode_LChild != None and oNode_Remove.m_oNode_RChild != None:
			oNode_Parent = oNode_Remove
			oNode_Descendants = oNode_Remove.m_oNode_RChild
			
			while oNode_Descendants.m_oNode_LChild != None:
				oNode_Parent = oNode_Descendants
				oNode_Descendants = oNode_Descendants.m_oNode_LChild
				
			oNode_Remove.m_nVal = oNode_Descendants.m_nVal
			oNode_Remove = oNode_Descendants
			
		# 루트 노드 일 경우
		if oNode_Remove == self.m_oNode_Root:
			self.m_oNode_Root = oNode_Remove.m_oNode_LChild if oNode_Remove.m_oNode_LChild != None else oNode_Remove.m_oNode_RChild
			
		# 왼쪽 자식이 존재 할 경우
		if oNode_Remove.m_oNode_LChild != None:
			# 제거 할 노드가 부모의 왼쪽 자식 일 경우
			if oNode_Remove == oNode_Parent.m_oLChild:
				oNode_Parent.m_oNode_LChild = oNode_Remove.m_oNode_LChild
				
			else:
				oNode_Parent.m_oNode_RChild = oNode_Remove.m_oNode_RChild
				
		else:
			# 제거 할 노드가 부모의 왼쪽 자식 일 경우
			if oNode_Remove == oNode_Parent.m_oNode_LChild:
				oNode_Parent.m_oNode_LChild = oNode_Remove.m_oNode_RChild
				
			else:
				oNode_Parent.m_oNode_RChild = oNode_Remove.m_oNode_RChild
		
	# 노드를 탐색한다
	def findNode(self, a_nVal):
		oNode = self.m_oNode_Root
		oNode_Parent = None
		
		while oNode != None and a_nVal != oNode.m_nVal:
			oNode_Parent = oNode
			
			# 값이 작을 경우
			if a_nVal <= oNode.m_nVal:
				oNode = oNode.m_oNode_LChild
				
			else:
				oNode = oNode.m_oNode_RChild
				
		return (oNode, oNode_Parent)
	
	# 노드를 순회한다
	def enumerate(self, a_nOrder, a_oCallback):
		self.m_oListFunctions = [
			self.enumerate_ByPreOrder,
			self.enumerate_ByInOrder,
			self.enumerate_ByPostOrder
		]
		
		self.m_oListFunctions[a_nOrder](self.m_oNode_Root, a_oCallback)
		
	# 노드를 전위 순회한다
	def enumerate_ByPreOrder(self, a_oNode, a_oCallback):
		# 순회가 불가능 할 경우
		if a_oNode == None:
			return
		
		a_oCallback(a_oNode.m_nVal)
		
		self.enumerate_ByPreOrder(a_oNode.m_oNode_LChild, a_oCallback)
		self.enumerate_ByPreOrder(a_oNode.m_oNode_RChild, a_oCallback)
	
	# 노드를 중위 순회한다
	def enumerate_ByInOrder(self, a_oNode, a_oCallback):
		# 순회가 불가능 할 경우
		if a_oNode == None:
			return
		
		self.enumerate_ByInOrder(a_oNode.m_oNode_LChild, a_oCallback)
		a_oCallback(a_oNode.m_nVal)
		
		self.enumerate_ByInOrder(a_oNode.m_oNode_RChild, a_oCallback)
	
	# 노드를 후위 순회한다
	def enumerate_ByPostOrder(self, a_oNode, a_oCallback):
		# 순회가 불가능 할 경우
		if a_oNode == None:
			return
		
		self.enumerate_ByPostOrder(a_oNode.m_oNode_LChild, a_oCallback)
		self.enumerate_ByPostOrder(a_oNode.m_oNode_RChild, a_oCallback)
		
		a_oCallback(a_oNode.m_nVal)
		
	# 노드를 생성한다
	def createNode(self, a_nVal):
		return CTree_BSearch.CNode(a_nVal)
	