import os
import sys

from Example.Example_27.CGraph_List import CGraph_List
from Example.Example_28.MinimumCostSpanningTree import createMCST_ByPrim, createMCST_ByKruskal

"""
최소 비용 신장 트리 (Minimum Cost Spanning Tree) 란?
- 가중치가 낮은 최소한의 간선으로 그래프 내의 모든 정점을 연결한 트리를 의미한다. (+ 즉,
최소 비용 신장 트리 내의 간선 개수는 정점 개수 - 1 이라는 것을 알 수 있다.)

최소 비용 신장 트리 구축 알고리즘 종류
- 프림 (Prim)
- 크루스칼 (Kruskal)
"""


# Example 28 (최소 비용 신장 트리)
def start(args):
	oGraph = CGraph_List()
	
	oGraph.addVertex("A")
	oGraph.addVertex("B")
	oGraph.addVertex("C")
	oGraph.addVertex("D")
	oGraph.addVertex("E")
	oGraph.addVertex("F")
	
	oGraph.addEdge("A", "B", 1)
	oGraph.addEdge("A", "C", 2)
	
	oGraph.addEdge("B", "D", 1)
	oGraph.addEdge("B", "E", 2)
	
	oGraph.addEdge("C", "F", 1)
	oGraph.addEdge("C", "A", 2)
	
	oGraph.addEdge("D", "B", 1)
	oGraph.addEdge("D", "C", 2)
	
	oGraph.addEdge("E", "D", 1)
	oGraph.addEdge("E", "F", 2)
	
	oGraph.addEdge("F", "A", 1)
	oGraph.addEdge("F", "B", 2)
	
	oTree_MCST = createMCST_ByPrim(oGraph, "A")
	# oTree_MCST = createMCST_ByKruskal(oGraph)
	
	print("=====> 최소 비용 신장 트리 <=====")
	printEdges(oTree_MCST)
	
	
# 간선을 출력한다
def printEdges(a_oTree_MCST):
	for i in range(0, len(a_oTree_MCST.m_oListVertices)):
		oVertex = a_oTree_MCST.m_oListVertices[i]
		
		for oEdge in oVertex.m_oListEdges:
			print(f"{oEdge.m_oVertex_From.m_oKey} -> {oEdge.m_oVertex_To.m_oKey} : {oEdge.m_nCost}")
	