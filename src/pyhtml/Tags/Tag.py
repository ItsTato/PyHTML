from typing import Union

class Tag:
	def __init__(self,parent) -> None:
		parent.add_child(self)
		self.__children:list = []
		return
	def build(self) -> str:
		return ""
	@property
	def children(self) -> list:
		return self.__children
	def add_child(self,child) -> None:
		self.__children.append(child)
		return

parent_type:Union = Union[Tag,None]
