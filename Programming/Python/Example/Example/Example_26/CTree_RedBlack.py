import os
import sys


# 레드 블랙 트리
class CTree_RedBlack:
	COLOR_RED = 0
	COLOR_BLACK = 1
	
	# 노드
	class CNode:
		# 초기화
		def __init__(self, a_nVal):
			self.m_nVal = a_nVal
			self.m_nColor = CTree_RedBlack.COLOR_RED
			
			self.m_oNode_Parent = None
			self.m_oNode_LChild = None
			self.m_oNode_RChild = None
			
			
	# 초기화
	def __init__(self):
		self.m_oNode_Nil = CTree_RedBlack.CNode(0)
		self.m_oNode_Nil.m_nColor = CTree_RedBlack.COLOR_BLACK
		
		self.m_oNode_Root = self.m_oNode_Nil
		
	# 값을 추가한다
	def addVal(self, a_nVal):
		oNode_New = self.createNode(a_nVal)
		
		# 루트 노드가 없을 경우
		if self.m_oNode_Root == self.m_oNode_Nil:
			self.m_oNode_Root = oNode_New
		
		else:
			oNode = self.m_oNode_Root
			oNode_Parent = None
			
			while oNode != self.m_oNode_Nil:
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
		
		self.rebalance_ByAdd(oNode_New)
	
	# 값을 제거한다
	def removeVal(self, a_nVal):
		oNode_Remove = self.findNode(a_nVal)
		
		# 자식 노드가 모두 존재 할 경우
		if oNode_Remove.m_oNode_LChild != self.m_oNode_Nil and oNode_Remove.m_oNode_RChild != self.m_oNode_Nil:
			oNode_Descendants = oNode_Remove.m_oNode_RChild
			
			while oNode_Descendants.m_oNode_LChild != self.m_oNode_Nil:
				oNode_Descendants = oNode_Descendants.m_oNode_LChild
			
			oNode_Remove.m_nVal = oNode_Descendants.m_nVal
			oNode_Remove = oNode_Descendants
		
		# 루트 노드 일 경우
		if oNode_Remove == self.m_oNode_Root:
			self.m_oNode_Root = oNode_Remove.m_oNode_LChild if oNode_Remove.m_oNode_LChild != self.m_oNode_Nil else oNode_Remove.m_oNode_RChild
			
		else:
			# 왼쪽 자식이 존재 할 경우
			if oNode_Remove.m_oNode_LChild != self.m_oNode_Nil:
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
					
		self.rebalance_ByRemove(oNode_Remove)
	
	# 노드를 탐색한다
	def findNode(self, a_nVal):
		oNode = self.m_oNode_Root
		
		while oNode != self.m_oNode_Nil and a_nVal != oNode.m_nVal:
			# 값이 작을 경우
			if a_nVal <= oNode.m_nVal:
				oNode = oNode.m_oNode_LChild
			
			else:
				oNode = oNode.m_oNode_RChild
		
		return oNode
	
	# 균형을 회복한다
	def rebalance_ByAdd(self, a_oNode):
		oNode = a_oNode
		
		while oNode.m_oNode_Parent != None:
			# 균형 회복이 필요 없을 경우
			if oNode.m_oNode_Parent.m_nColor != CTree_RedBlack.COLOR_RED:
				break
				
			bIsLeft = oNode.m_oNode_Parent == oNode.m_oNode_Parent.m_oNode_Parent.m_oNode_LChild
			oNode_Uncle = oNode.m_oNode_Parent.m_oNode_Parent.m_oNode_RChild if bIsLeft else oNode.m_oNode_Parent.m_oNode_Parent.m_oNode_LChild
			
			# 삼촌 노드가 빨간색 일 경우
			if oNode_Uncle.m_nColor == CTree_RedBlack.COLOR_RED:
				oNode.m_oNode_Parent.m_oNode_Parent.m_nColor = CTree_RedBlack.COLOR_RED
				
				oNode.m_oNode_Parent.m_nColor = CTree_RedBlack.COLOR_BLACK
				oNode_Uncle.m_nColor = CTree_RedBlack.COLOR_BLACK
				
				oNode = oNode.m_oNode_Parent.m_oNode_Parent
				continue
				
			# 부모 노드가 왼쪽 자식 일 경우
			if bIsLeft:
				# 현재 노드가 오른쪽 자식 일 경우
				if oNode == oNode.m_oNode_Parent.m_oNode_RChild:
					oNode = oNode.m_oNode_Parent
					self.rotateNode_Left(oNode)
					
				oNode.m_oNode_Parent.m_nColor = CTree_RedBlack.COLOR_BLACK
				oNode.m_oNode_Parent.m_oNode_Parent.m_nColor = CTree_RedBlack.COLOR_RED
			
				self.rotateNode_Right(oNode.m_oNode_Parent.m_oNode_Parent)
				
			else:
				# 현재 노드가 왼쪽 자식 일 경우
				if oNode == oNode.m_oNode_Parent.m_oNode_LChild:
					oNode = oNode.m_oNode_Parent
					self.rotateNode_Right(oNode)
				
				oNode.m_oNode_Parent.m_nColor = CTree_RedBlack.COLOR_BLACK
				oNode.m_oNode_Parent.m_oNode_Parent.m_nColor = CTree_RedBlack.COLOR_RED
				
				self.rotateNode_Left(oNode.m_oNode_Parent.m_oNode_Parent)
		
		self.m_oNode_Root.m_nColor = CTree_RedBlack.COLOR_BLACK
		
	# 균형을 회복한다
	def rebalance_ByRemove(self, a_oNode):
		oNode = a_oNode
		
		while oNode.m_oNode_Parent != None:
			# 균형 회복이 필요 없을 경우
			if oNode.m_nColor != CTree_RedBlack.COLOR_BLACK:
				break
				
			bIsLeft = oNode == oNode.m_oNode_Parent.m_oNode_LChild
			oNode_Sibiling = oNode.m_oNode_Parent.m_oNode_RChild if bIsLeft else oNode.m_oNode_Parent.m_oNode_LChild
			
			# 형제 노드가 빨간색 일 경우
			if oNode_Sibiling.m_nColor == CTree_RedBlack.COLOR_RED:
				oNode.m_oNode_Parent.m_nColor = CTree_RedBlack.COLOR_RED
				oNode_Sibiling.m_nColor = CTree_RedBlack.COLOR_BLACK
				
				# 현재 노드가 왼쪽 자식 일 경우
				if bIsLeft:
					self.rotateNode_Left(oNode.m_oNode_Parent)
					
				else:
					self.rotateNode_Right(oNode.m_oNode_Parent)
				
				continue
				
			bIsNode_BlackA = oNode_Sibiling.m_oNode_LChild.m_nColor == CTree_RedBlack.COLOR_BLACK
			bIsNode_BlackB = oNode_Sibiling.m_oNode_RChild.m_nColor == CTree_RedBlack.COLOR_BLACK
				
			# 형제 노드의 자식 노드가 모두 검은색 일 경우
			if bIsNode_BlackA and bIsNode_BlackB:
				oNode_Sibiling.m_nColor = CTree_RedBlack.COLOR_RED
				oNode = oNode.m_oNode_Parent
				
				continue
				
			# 현재 노드가 왼쪽 자식 일 경우
			if bIsLeft:
				# 형제 노드의 왼쪽 자식이 빨간색 일 경우
				if oNode_Sibiling.m_oNode_LChild.m_nColor == CTree_RedBlack.COLOR_RED:
					oNode_Sibiling.m_nColor = CTree_RedBlack.COLOR_RED
					oNode_Sibiling.m_oNode_LChild.m_nColor = CTree_RedBlack.COLOR_BLACK
					
					self.rotateNode_Right(oNode_Sibiling)
					oNode_Sibiling = oNode_Sibiling.m_oNode_Parent
					
				oNode_Sibiling.m_nColor = oNode_Sibiling.m_oNode_Parent.m_nColor
				
				oNode_Sibiling.m_oNode_Parent.m_nColor = CTree_RedBlack.COLOR_BLACK
				oNode_Sibiling.m_oNode_RChild.m_nColor = CTree_RedBlack.COLOR_BLACK
				
				self.rotateNode_Left(oNode_Sibiling.m_oNode_Parent)
					
			else:
				# 형제 노드의 오른쪽 자식이 빨간색 일 경우
				if oNode_Sibiling.m_oNode_RChild.m_nColor == CTree_RedBlack.COLOR_RED:
					oNode_Sibiling.m_nColor = CTree_RedBlack.COLOR_RED
					oNode_Sibiling.m_oNode_RChild.m_nColor = CTree_RedBlack.COLOR_BLACK
					
					self.rotateNode_Left(oNode_Sibiling)
					oNode_Sibiling = oNode_Sibiling.m_oNode_Parent
				
				oNode_Sibiling.m_nColor = oNode_Sibiling.m_oNode_Parent.m_nColor
				
				oNode_Sibiling.m_oNode_Parent.m_nColor = CTree_RedBlack.COLOR_BLACK
				oNode_Sibiling.m_oNode_LChild.m_nColor = CTree_RedBlack.COLOR_BLACK
				
				self.rotateNode_Right(oNode_Sibiling.m_oNode_Parent)
					
			oNode = self.m_oNode_Root
		
		oNode.m_nColor = CTree_RedBlack.COLOR_BLACK
	
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
		if oNode_RLChild != self.m_oNode_Nil:
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
		if oNode_LRChild != self.m_oNode_Nil:
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
		if a_oNode == self.m_oNode_Nil:
			return
		
		self.enumerate_ByInOrder(a_oNode.m_oNode_LChild, a_nDepth + 1, a_oCallback)
		a_oCallback(a_nDepth, a_oNode.m_nVal)
		
		self.enumerate_ByInOrder(a_oNode.m_oNode_RChild, a_nDepth + 1, a_oCallback)
		
	# 노드를 생성한다
	def createNode(self, a_nVal):
		oNode = CTree_RedBlack.CNode(a_nVal)
		oNode.m_oNode_LChild = self.m_oNode_Nil
		oNode.m_oNode_RChild = self.m_oNode_Nil
		
		return oNode
	