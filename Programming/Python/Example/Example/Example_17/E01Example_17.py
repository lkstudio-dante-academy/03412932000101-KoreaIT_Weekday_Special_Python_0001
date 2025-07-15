import os
import sys

from Example.Example_17.CSingleton import CSingleton
from Example.Example_17.CWidget import CWidget

"""
클래스 멤버 (Class Member) 란?
- 객체에 종속 되는 일반적인 멤버와 달리 클래스에 종속 되는 멤버를 의미한다.

클래스 멤버는 클래스 자체에 종속 되기 때문에 클래스 별로 1 개만 존재하며 클래스 변수는 모든 객체가
공유하는 변수라는 특징이 존재한다.

또한 클래스 멤버는 클래스 만으로 접근이 가능하다. (+ 즉, 일반적인 멤버는 객체에 종속 되기 때문에 특정 멤버에
접근하기 위해서는 객체 생성이 필요하지만 클래스 멤버는 객체 생성이 필요 없다는 것을 의미한다.)

Ex)
class CSomeClass:
	m_nVal_Static = 0
	
CSomeClass.m_nVal_Static = 10

위와 같이 클래스 영역에 변수를 선언하면 해당 변수는 클래스 자체에 종속 되는 클래스 변수가 된다. (+ 즉,
해당 변수는 클래스 만으로 접근 가능하다는 것을 알 수 있다.)
"""


# Example 18
def start(args):
	oWidgetA = CWidget()
	oWidgetB = CWidget()
	
	oWidgetA.incrVal(10)
	oWidgetB.incrVal(20)
	
	print("=====> 위젯 - A <=====")
	oWidgetA.showInfo()
	
	print("\n=====> 위젯 - B <=====")
	oWidgetB.showInfo()
	
	oSingletonA = CSingleton.getInst()
	oSingletonB = CSingleton.getInst()
	
	oSingletonA.setVal(10)
	oSingletonB.setVal(20)
	
	print("\n=====> 싱글턴 - A <=====")
	oSingletonA.showInfo()
	
	print("\n=====> 싱글턴 - B <=====")
	oSingletonB.showInfo()
	