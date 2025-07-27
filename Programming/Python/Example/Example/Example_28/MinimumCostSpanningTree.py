import os
import sys

from queue import PriorityQueue

from Example.Example_27.CGraph_List import CGraph_List
from Example.Example_28.CSet_Disjoint import CSet_Disjoint

# 최소 비용 신장 트리를 생성한다
def createMCST_ByPrim(a_oGraph, a_oKey_Start):
	oTree_MCST = CGraph_List()
	
	for i in range(0, len(a_oGraph.m_oListVertices)):
		oVertex = a_oGraph.m_oListVertices[i]
		oTree_MCST.addVertex(oVertex.m_oKey)
	
	oEdge = a_oGraph.findVertex(a_oKey_Start).m_oListEdges[0]
	oListVertices_Visitied = [oEdge.m_oVertex_From]
	
	oPQueueInfos_Edge = PriorityQueue()
	oPQueueInfos_Edge.put((oEdge.m_nCost, oEdge.m_oVertex_From.m_oKey, oEdge.m_oVertex_To.m_oKey))
	
	while not oPQueueInfos_Edge.empty():
		oInfo_Edge = oPQueueInfos_Edge.get()
		oVertex_To = a_oGraph.findVertex(oInfo_Edge[2])
		
		# 정점이 존재 할 경우
		if oVertex_To in oListVertices_Visitied:
			continue
			
		oTree_MCST.addEdge(oInfo_Edge[1], oInfo_Edge[2], oInfo_Edge[0])
		oListVertices_Visitied.append(oVertex_To)
		
		for oEdge in oVertex_To.m_oListEdges:
			oPQueueInfos_Edge.put((oEdge.m_nCost, oEdge.m_oVertex_From.m_oKey, oEdge.m_oVertex_To.m_oKey))
		
	return oTree_MCST


# 최소 비용 신장 트리를 생성한다
def createMCST_ByKruskal(a_oGraph):
	oTree_MCST = CGraph_List()
	oPQueueInfos_Edge = PriorityQueue()
	
	oDictSets_Disjoint = dict()
	
	for i in range(0, len(a_oGraph.m_oListVertices)):
		oVertex = a_oGraph.m_oListVertices[i]
		oTree_MCST.addVertex(oVertex.m_oKey)
		
		oDictSets_Disjoint[oVertex.m_oKey] = CSet_Disjoint(oVertex.m_oKey)
		
		for oEdge in oVertex.m_oListEdges:
			nCost = oEdge.m_nCost
			oVertex_From = oEdge.m_oVertex_From
			oVertex_To = oEdge.m_oVertex_To
			
			oPQueueInfos_Edge.put((nCost, oVertex_From.m_oKey, oVertex_To.m_oKey))
			
	while not oPQueueInfos_Edge.empty():
		oInfo_Edge = oPQueueInfos_Edge.get()
		
		oVertex_From = a_oGraph.findVertex(oInfo_Edge[1])
		oVertex_To = a_oGraph.findVertex(oInfo_Edge[2])
		
		oSet_FromDisjoint = oDictSets_Disjoint[oVertex_From.m_oKey]
		oSet_ToDisjoint = oDictSets_Disjoint[oVertex_To.m_oKey]
		
		# 간선 추가가 불가능 할 경우
		if oSet_FromDisjoint.findNode_Root() == oSet_ToDisjoint.findNode_Root():
			continue
		
		oTree_MCST.addEdge(oVertex_From.m_oKey, oVertex_To.m_oKey, oInfo_Edge[0])
		oSet_FromDisjoint.union(oSet_ToDisjoint)
		
	return oTree_MCST
