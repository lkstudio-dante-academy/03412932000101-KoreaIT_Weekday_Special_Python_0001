import os
import sys


# 분리 집합
class CSet_Disjoint:
	# 노드
	class CNode:
		# 초기화
		def __init__(self, a_nVal):
			self.m_nVal = a_nVal
			self.m_oNode_Root = None
			
			
	# 초기화
	def __init__(self, a_nVal):
		self.m_oNode = CSet_Disjoint.CNode(a_nVal)
		
	# 분리 집합을 합친다
	def union(self, a_oOther):
		oNode = a_oOther.findNode_Root()
		oNode.m_oNode_Root = self.m_oNode
		
	# 루트 노드를 탐색한다
	def findNode_Root(self):
		oNode = self.m_oNode
		
		while oNode.m_oNode_Root != None:
			oNode = oNode.m_oNode_Root
			
		return oNode
	