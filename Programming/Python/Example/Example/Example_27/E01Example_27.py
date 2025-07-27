import os
import sys

from Example.Example_27.CGraph_List import CGraph_List
from Example.Example_27.CGraph_Matrix import CGraph_Matrix

"""
그래프 (Graph) 란?
- 정점과 간선의 집합으로 데이터 간의 관계를 표현하는 자료구조를 의미한다. (+ 즉, 그래프를 활용하면
데이터 간의 복잡한 관계를 표현하는 것이 가능하다.)

그래프는 간선의 방향 유무에 따라 방향성 그래프와 무방향성 그래프가 존재하며 간선의 표현 방식에 따라
인접 행렬 방식 (Adjacency Matrix Graph) 과 인접 리스트 방식 (Adjacency List Graph) 으로 구현이 가능하다.

그래프 탐색 (Graph Search) 란?
- 그래프에 존재하는 모든 정점을 방문하는 것을 의미한다. (+ 즉, 탐색을 활용하면 그래프에 존재하는 모든 정점에
접근하는 것이 가능하다.)

그래프 탐색 종류
- 깊이 우선 탐색 (Depth First Search)
- 너비 우선 탐색 (Breadth First Search)

깊이 우선 탐색 (Depth First Search) 이란?
- 출발 정점에서 인접한 정점 중 하나를 선택해서 탐색을 이어나가는 방법을 의미한다. (+ 즉, 깊이 우선 탐색은
현재 정점에서 인접한 정점 하나를 타고 들어간다는 것을 알 수 있다.)

너비 우선 탐색 (Breadth First Search) 이란?
- 출발 정점에서 인접한 정점으로 탐색 범위를 확장 시켜나가는 탐색 방법을 의미한다. (+ 즉, 너비 우선 탐색은
현재 정점에서 인접한 모든 정점을 탐색 후 다른 정점의 인접한 정점을 탐색한다는 것을 알 수 있다.)

인접 행렬 방식 (Adjacency Matrix Graph) 이란?
- 간선을 행렬로 표현하는 방법을 의미한다. (+ 즉, 인접 행렬 방식은 간선 정보가 하나의 행렬로
모두 표현 된다는 것을 알 수 있다.)

인접 리스트 방식 (Adjacency List Graph) 이란?
- 간선을 연결 리스트로 표현하는 방법을 의미한다. (+ 즉, 인접 리스트 방식은 간선 정보가 각 정점 마다
개별적으로 존재한다는 것을 알 수 있다.)

인접 행렬 방식 (Adjacency Matrix Graph) vs 인접 리스트 방식 (Adjacency List Graph)
- 인접 행렬 방식은 행렬을 통해 간선을 표현하기 때문에 간선의 개수가 적을 경우 메모리가 낭비되는 단점이 존재한다.

반면, 인접 리스트 방식은 연결 리스트를 통해 간선을 표현하기 때문에 간선의 개수가 많을 경우 탐색 성능이
떨어지는 단점이 존재한다.

따라서 간선의 개수가 적을 경우 인접 리스트 방식이 좀 더 유리하며 간선의 개수가 많을 경우 인접 행렬 방식이
좀 더 좋은 선택이라는 것을 알 수 있다.
"""


# Example 27 (그래프)
def start(args):
	# oGraph = CGraph_List()
	oGraph = CGraph_Matrix()
	
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
	
	print("=====> 그래프 - 깊이 우선 탐색 <=====")
	oGraph.enumerate(CGraph_List.SEARCH_DEPTH, "A", lambda a_oKey: print(f"{a_oKey}, ", end = ""))
	
	print("\n\n=====> 그래프 - 너비 우선 탐색 <=====")
	oGraph.enumerate(CGraph_List.SEARCH_BREADTH, "A", lambda a_oKey: print(f"{a_oKey}, ", end = ""))
	
	print()
	