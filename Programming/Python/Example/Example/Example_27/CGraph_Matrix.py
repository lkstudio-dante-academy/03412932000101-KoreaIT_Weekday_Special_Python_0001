import os
import sys


# 인접 행렬 그래프
class CGraph_Matrix:
	SEARCH_DEPTH = 0
	SEARCH_BREADTH = 1
	
	# 정점
	class CVertex:
		# 초기화
		def __init__(self, a_oKey):
			self.m_oKey = a_oKey
			
			
	# 초기화
	def __init__(self):
		self.m_oListVertices = []
		self.m_oMatrixEdges = []
		
	# 정점을 추가한다
	def addVertex(self, a_oKey):
		oVertex = self.createVertex(a_oKey)
		self.m_oListVertices.append(oVertex)
		
		self.m_oMatrixEdges.append(list())
		
		for i in range(0, len(self.m_oMatrixEdges)):
			for j in range(len(self.m_oMatrixEdges[i]), len(self.m_oMatrixEdges)):
				self.m_oMatrixEdges[i].append(0)

	# 간선을 추가한다
	def addEdge(self, a_oFrom, a_oTo, a_nCost):
		nIdx_FromVertex = self.findVertex_At(a_oFrom)
		nIdx_ToVertex = self.findVertex_At(a_oTo)
		
		self.m_oMatrixEdges[nIdx_FromVertex][nIdx_ToVertex] = a_nCost
		self.m_oMatrixEdges[nIdx_ToVertex][nIdx_FromVertex] = a_nCost
	
	# 정점을 제거한다
	def removeVertex(self, a_oKey):
		oVertex = self.findVertex(a_oKey)
		nIdx_Vertex = self.findVertex_At(a_oKey)
		
		for i in range(0, len(self.m_oMatrixEdges)):
			# 간선 제거가 불가능 할 경우
			if self.m_oMatrixEdges[nIdx_Vertex][i] <= 0:
				continue
				
			del self.m_oMatrixEdges[nIdx_Vertex][i]
		
		self.m_oListVertices.remove(oVertex)
		del self.m_oMatrixEdges[nIdx_Vertex]
	
	# 간선을 제거한다
	def removeEdge(self, a_oFrom, a_oTo):
		nIdx_FromVertex = self.findVertex_At(a_oFrom)
		nIdx_ToVertex = self.findVertex_At(a_oTo)
		
		self.m_oMatrixEdges[nIdx_FromVertex][nIdx_ToVertex] = 0
		self.m_oMatrixEdges[nIdx_ToVertex][nIdx_FromVertex] = 0
	
	# 정점을 탐색한다
	def findVertex(self, a_oKey):
		for oVertex in self.m_oListVertices:
			# 정점이 존재 할 경우
			if a_oKey == oVertex.m_oKey:
				return oVertex
		
		return None
	
	# 정점을 탐색한다
	def findVertex_At(self, a_oKey):
		oVertex = self.findVertex(a_oKey)
		return self.m_oListVertices.index(oVertex)
	
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
		
		nIdx_Vertex = self.findVertex_At(a_oVertex.m_oKey)
		
		for i in range(0, len(self.m_oMatrixEdges[nIdx_Vertex])):
			oVertex_To = self.m_oListVertices[i]
			
			bIsEnable_VisitA = self.m_oMatrixEdges[nIdx_Vertex][i] > 0
			bIsEnable_VisitB = oVertex_To not in a_oOutListVertices_Visited
			
			# 방문이 불가능 할 경우
			if not bIsEnable_VisitA or not bIsEnable_VisitB:
				continue
			
			self.enumerate_ByDepthFirst(oVertex_To, a_oCallback, a_oOutListVertices_Visited)
	
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
			
			nIdx_Vertex = self.findVertex_At(oVertex.m_oKey)
			
			for i in range(0, len(self.m_oMatrixEdges[nIdx_Vertex])):
				# 방문이 불가능 할 경우
				if self.m_oMatrixEdges[nIdx_Vertex][i] <= 0:
					continue
				
				oQueueVertices.append(self.m_oListVertices[i])
	
	# 정점을 생성한다
	def createVertex(self, a_oKey):
		return CGraph_Matrix.CVertex(a_oKey)
	