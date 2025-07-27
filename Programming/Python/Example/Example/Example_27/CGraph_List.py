import os
import sys


# 인접 리스트 그래프
class CGraph_List:
	SEARCH_DEPTH = 0
	SEARCH_BREADTH = 1
	
	# 정점
	class CVertex:
		# 초기화
		def __init__(self, a_oKey):
			self.m_oKey = a_oKey
			self.m_oListEdges = []
			

	# 간선
	class CEdge:
		# 초기화
		def __init__(self, a_oFrom, a_oTo, a_nCost):
			self.m_nCost = a_nCost
			
			self.m_oVertex_From = a_oFrom
			self.m_oVertex_To = a_oTo
			
			
	# 초기화
	def __init__(self):
		self.m_oListVertices = []
		
	# 정점을 추가한다
	def addVertex(self, a_oKey):
		oVertex = self.createVertex(a_oKey)
		self.m_oListVertices.append(oVertex)

	# 간선을 추가한다
	def addEdge(self, a_oFrom, a_oTo, a_nCost):
		oVertex_From = self.findVertex(a_oFrom)
		oVertex_To = self.findVertex(a_oTo)
		
		oEdge_From = self.createEdge(oVertex_From, oVertex_To, a_nCost)
		oEdge_To = self.createEdge(oVertex_To, oVertex_From, a_nCost)
		
		oVertex_From.m_oListEdges.append(oEdge_From)
		oVertex_To.m_oListEdges.append(oEdge_To)
		
	# 정점을 제거한다
	def removeVertex(self, a_oKey):
		oVertex = self.findVertex(a_oKey)
		
		for oEdge in oVertex.m_oListEdges:
			self.removeEdge(a_oKey, oEdge.m_oVertex_To.m_oKey)
			
		self.m_oListVertices.remove(oVertex)
		
	# 간선을 제거한다
	def removeEdge(self, a_oFrom, a_oTo):
		oEdge_From = self.findEdge(a_oFrom, a_oTo)
		oEdge_To = self.findEdge(a_oTo, a_oFrom)
		
		oEdge_From.m_oVertex_From.m_oListEdges.remove(oEdge_From)
		oEdge_To.m_oVertex_To.m_oListEdges.remove(oEdge_To)
		
	# 정점을 탐색한다
	def findVertex(self, a_oKey):
		for oVertex in self.m_oListVertices:
			# 정점이 존재 할 경우
			if a_oKey == oVertex.m_oKey:
				return oVertex
			
		return None

	# 간선을 탐색한다
	def findEdge(self, a_oFrom, a_oTo):
		oVertex_From = self.findVertex(a_oFrom)
		
		# 간선 탐색이 불가능 할 경우
		if oVertex_From == None:
			return None
		
		for oEdge in oVertex_From.m_oListEdges:
			# 간선이 존재 할 경우
			if a_oTo == oEdge.m_oVertex_To.m_oKey:
				return oEdge
			
		return None
	
	# 정점을 순회한다
	def enumerate(self, a_nSearch, a_oKey, a_oCallback):
		oListFunctions = [
			self.enumerate_ByDepthFirst,
			self.enumerate_ByBreadthFirst
		]
		
		oVertex_Start = self.findVertex(a_oKey)
		oListVertices_Visited = [None] * len(self.m_oListVertices)
		
		oListFunctions[a_nSearch](oVertex_Start, a_oCallback, oListVertices_Visited)
		
	# 정점을 깊이 우선으로 순회한다
	def enumerate_ByDepthFirst(self, a_oVertex, a_oCallback, a_oOutListVertices_Visited):
		a_oCallback(a_oVertex.m_oKey)
		a_oOutListVertices_Visited.append(a_oVertex)
		
		for oEdge in a_oVertex.m_oListEdges:
			# 방문이 불가능 할 경우
			if oEdge.m_oVertex_To in a_oOutListVertices_Visited:
				continue
				
			self.enumerate_ByDepthFirst(oEdge.m_oVertex_To, a_oCallback, a_oOutListVertices_Visited)
	
	# 정점을 너비 우선으로 순회한다
	def enumerate_ByBreadthFirst(self, a_oVertex, a_oCallback, a_oOutListVertices_Visited):
		oQueueVertices = [a_oVertex]
		
		while len(oQueueVertices) > 0:
			oVertex = oQueueVertices.pop(0)
			
			# 방문이 불가능 할 경우
			if oVertex in a_oOutListVertices_Visited:
				continue
				
			a_oCallback(oVertex.m_oKey)
			a_oOutListVertices_Visited.append(oVertex)
			
			for oEdge in oVertex.m_oListEdges:
				oQueueVertices.append(oEdge.m_oVertex_To)
	
	# 정점을 생성한다
	def createVertex(self, a_oKey):
		return CGraph_List.CVertex(a_oKey)
	
	# 간선을 생성한다
	def createEdge(self, a_oFrom, a_oTo, a_nCost):
		return CGraph_List.CEdge(a_oFrom, a_oTo, a_nCost)
	