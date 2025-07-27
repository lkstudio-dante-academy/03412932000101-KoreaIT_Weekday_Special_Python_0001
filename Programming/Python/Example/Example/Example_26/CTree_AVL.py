import os
import sys


# AVL 트리
class CTree_AVL:
	# 노드
	class CNode:
		# 초기화
		def __init__(self, a_nVal):
			self.m_nVal = a_nVal
			
			self.m_oNode_Parent = None
			self.m_oNode_LChild = None
			self.m_oNode_RChild = None
			
	
	# 초기화
	def __init__(self):
		self.m_oNode_Root = None
		
	# 높이를 반환한다
	def getHeight(self, a_oNode):
		# 높이 반환이 불가능 할 경우
		if a_oNode == None:
			return 0
		
		nHeight_LSubTree = self.getHeight(a_oNode.m_oNode_LChild)
		nHeight_RSubTree = self.getHeight(a_oNode.m_oNode_RChild)
		
		return 1 + max(nHeight_LSubTree, nHeight_RSubTree)
	
	# 값을 추가한다
	def addVal(self, a_nVal):
		oNode_New = self.createNode(a_nVal)
		
		# 루트 노드가 없을 경우
		if self.m_oNode_Root == None:
			self.m_oNode_Root = oNode_New
		
		else:
			oNode = self.m_oNode_Root
			oNode_Parent = None
			
			while oNode != None:
				oNode_Parent = oNode
				
				# 값이 작을 경우
				if a_nVal <= oNode.m_nVal:
					oNode = oNode.m_oNode_LChild
				
				else:
					oNode = oNode.m_oNode_RChild
			
			oNode_New.m_oNode_Parent = oNode_Parent
			
			# 값이 작을 경우
			if a_nVal <= oNode_Parent.m_nVal:
				oNode_Parent.m_oNode_LChild = oNode_New
			
			else:
				oNode_Parent.m_oNode_RChild = oNode_New
			
		self.rebalance(oNode_New)
	
	# 값을 제거한다
	def removeVal(self, a_nVal):
		oNode_Remove = self.findNode(a_nVal)
		
		# 자식 노드가 모두 존재 할 경우
		if oNode_Remove.m_oNode_LChild != None and oNode_Remove.m_oNode_RChild != None:
			oNode_Descendants = oNode_Remove.m_oNode_RChild
			
			while oNode_Descendants.m_oNode_LChild != None:
				oNode_Descendants = oNode_Descendants.m_oNode_LChild
			
			oNode_Remove.m_nVal = oNode_Descendants.m_nVal
			oNode_Remove = oNode_Descendants
		
		# 루트 노드 일 경우
		if oNode_Remove == self.m_oNode_Root:
			self.m_oNode_Root = oNode_Remove.m_oNode_LChild if oNode_Remove.m_oNode_LChild != None else oNode_Remove.m_oNode_RChild
		
		# 왼쪽 자식이 존재 할 경우
		if oNode_Remove.m_oNode_LChild != None:
			# 제거 할 노드가 부모의 왼쪽 자식 일 경우
			if oNode_Remove == oNode_Remove.m_oNode_Parent.m_oLChild:
				oNode_Remove.m_oNode_Parent.m_oNode_LChild = oNode_Remove.m_oNode_LChild
			
			else:
				oNode_Remove.m_oNode_Parent.m_oNode_RChild = oNode_Remove.m_oNode_RChild
		
		else:
			# 제거 할 노드가 부모의 왼쪽 자식 일 경우
			if oNode_Remove == oNode_Remove.m_oNode_Parent.m_oNode_LChild:
				oNode_Remove.m_oNode_Parent.m_oNode_LChild = oNode_Remove.m_oNode_RChild
			
			else:
				oNode_Remove.m_oNode_Parent.m_oNode_RChild = oNode_Remove.m_oNode_RChild
				
		self.rebalance(oNode_Remove)
	
	# 노드를 탐색한다
	def findNode(self, a_nVal):
		oNode = self.m_oNode_Root
		
		while oNode != None and a_nVal != oNode.m_nVal:
			# 값이 작을 경우
			if a_nVal <= oNode.m_nVal:
				oNode = oNode.m_oNode_LChild
			
			else:
				oNode = oNode.m_oNode_RChild
		
		return oNode
	
	# 균형을 회복한다
	def rebalance(self, a_oNode):
		# 균형 회복이 불가능 할 경우
		if a_oNode == None:
			return
		
		nHeight_LSubTree = self.getHeight(a_oNode.m_oNode_LChild)
		nHeight_RSubTree = self.getHeight(a_oNode.m_oNode_RChild)
		
		# 균형 회복이 필요 없을 경우
		if abs(nHeight_LSubTree - nHeight_RSubTree) <= 1:
			self.rebalance(a_oNode.m_oNode_Parent)
			return
		
		# 왼쪽 하위 트리 균형 회복이 필요 할 경우
		if nHeight_LSubTree - nHeight_RSubTree >= 1:
			self.rebalanceSubTree_Left(a_oNode)
			
		else:
			self.rebalanceSubTree_Right(a_oNode)
		
		self.rebalance(a_oNode.m_oNode_Parent)
		
	# 왼쪽 서브 트리 균형을 회복한다
	def rebalanceSubTree_Left(self, a_oNode):
		nHeight_LSubTree = self.getHeight(a_oNode.m_oNode_LChild.m_oNode_LChild)
		nHeight_RSubTree = self.getHeight(a_oNode.m_oNode_LChild.m_oNode_RChild)
		
		# LR 상태 일 경우
		if nHeight_LSubTree - nHeight_RSubTree < 0:
			self.rotateNode_Left(a_oNode.m_oNode_LChild)
			
		self.rotateNode_Right(a_oNode)
		
	# 오른쪽 서브 트리 균형을 회복한다
	def rebalanceSubTree_Right(self, a_oNode):
		nHeight_LSubTree = self.getHeight(a_oNode.m_oNode_RChild.m_oNode_LChild)
		nHeight_RSubTree = self.getHeight(a_oNode.m_oNode_RChild.m_oNode_RChild)
		
		# RL 상태 일 경우
		if nHeight_LSubTree - nHeight_RSubTree > 0:
			self.rotateNode_Right(a_oNode.m_oNode_RChild)
		
		self.rotateNode_Left(a_oNode)
		
	# 노드를 왼쪽으로 회전한다
	def rotateNode_Left(self, a_oNode):
		oNode_Parent = a_oNode.m_oNode_Parent
		oNode_RChild = a_oNode.m_oNode_RChild
		oNode_RLChild = oNode_RChild.m_oNode_LChild
		
		a_oNode.m_oNode_Parent = oNode_RChild
		a_oNode.m_oNode_RChild = oNode_RLChild
		
		oNode_RChild.m_oNode_Parent = oNode_Parent
		oNode_RChild.m_oNode_LChild = a_oNode
		
		# 루트 노드 일 경우
		if a_oNode == self.m_oNode_Root:
			self.m_oNode_Root = oNode_RChild
			
		# RL 노드가 존재 할 경우
		if oNode_RLChild != None:
			oNode_RLChild.m_oNode_Parent = a_oNode
		
		# 부모 노드가 존재 할 경우
		if oNode_Parent != None:
			# 회전 노드가 부모의 왼쪽 자식 일 경우
			if a_oNode == oNode_Parent.m_oNode_LChild:
				oNode_Parent.m_oNode_LChild = oNode_RChild
				
			else:
				oNode_Parent.m_oNode_RChild = oNode_RChild
	
	# 노드를 오른쪽으로 회전한다
	def rotateNode_Right(self, a_oNode):
		oNode_Parent = a_oNode.m_oNode_Parent
		oNode_LChild = a_oNode.m_oNode_LChild
		oNode_LRChild = oNode_LChild.m_oNode_RChild
		
		a_oNode.m_oNode_Parent = oNode_LChild
		a_oNode.m_oNode_LChild = oNode_LRChild
		
		oNode_LChild.m_oNode_Parent = oNode_Parent
		oNode_LChild.m_oNode_RChild = a_oNode
		
		# 루트 노드 일 경우
		if a_oNode == self.m_oNode_Root:
			self.m_oNode_Root = oNode_LChild
		
		# LR 노드가 존재 할 경우
		if oNode_LRChild != None:
			oNode_LRChild.m_oNode_Parent = a_oNode
		
		# 부모 노드가 존재 할 경우
		if oNode_Parent != None:
			# 회전 노드가 부모의 왼쪽 자식 일 경우
			if a_oNode == oNode_Parent.m_oNode_LChild:
				oNode_Parent.m_oNode_LChild = oNode_LChild
			
			else:
				oNode_Parent.m_oNode_RChild = oNode_LChild
		
	# 노드를 순회한다
	def enumerate(self, a_oCallback):
		self.enumerate_ByInOrder(self.m_oNode_Root, 0, a_oCallback)

	# 노드를 중위 순회한다
	def enumerate_ByInOrder(self, a_oNode, a_nDepth, a_oCallback):
		# 순회가 불가능 할 경우
		if a_oNode == None:
			return
		
		self.enumerate_ByInOrder(a_oNode.m_oNode_LChild, a_nDepth + 1, a_oCallback)
		a_oCallback(a_nDepth, a_oNode.m_nVal)
		
		self.enumerate_ByInOrder(a_oNode.m_oNode_RChild, a_nDepth + 1, a_oCallback)

	# 노드를 생성한다
	def createNode(self, a_nVal):
		return CTree_AVL.CNode(a_nVal)
	