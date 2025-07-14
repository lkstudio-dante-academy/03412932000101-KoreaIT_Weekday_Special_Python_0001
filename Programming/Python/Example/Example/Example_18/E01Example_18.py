import os
import sys

from Example.Example_18.CSingleton import CSingleton
from Example.Example_18.CWidget import CWidget


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
	