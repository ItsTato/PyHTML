from .Utils import prepare_content as pc
from .Tag import Tag, parent_type

class DOCTYPE(Tag):
	def __init__(self,parent:parent_type,document_type:str) -> None:
		super().__init__(parent)
		self.__document_type:str = document_type
		return
	def build(self) -> str:
		return f"<!DOCTYPE {self.__document_type}>"
	@property
	def document_type(self) -> str:
		return self.__document_type
	@document_type.setter
	def document_type(self,new_type:str) -> None:
		self.__document_type = new_type
		return

class Title(Tag):
	def __init__(self,parent:parent_type,title:str) -> None:
		super().__init__(parent)
		self.__title:str = title
		return
	def build(self) -> str:
		return f"<title>{self.__title}</title>"
	@property
	def title(self) -> str:
		return self.__title
	@title.setter
	def title(self,new_title:str) -> None:
		self.__title = new_title
		return

class Header(Tag):
	def __init__(self,parent:parent_type,header_level:int,content:str) -> None:
		super().__init__(parent)
		if header_level not in [1,2,3,4,5,6]:
			raise AttributeError(f"header_level must be 1, 2, 3, 4, 5 or 6.")
		self.__header_level:int = header_level
		self.__content:str = pc(content)
		return
	def build(self) -> str:
		return f"<h{self.__header_level}>{self.__content}</h{self.__header_level}>"
	@property
	def header_level(self) -> int:
		return self.__header_level
	@header_level.setter
	def header_level(self,new_header_level:int) -> None:
		if new_header_level not in [1,2,3,4,5,6]:
			raise AttributeError(f"header_level must be 1, 2, 3, 4, 5 or 6.")
		self.__header_level = new_header_level
		return
	@property
	def content(self) -> str:
		return self.__content
	@content.setter
	def content(self,new_content:str) -> None:
		self.__content = pc(new_content)
		return

class Paragraph(Tag):
	def __init__(self,parent:parent_type,content:str) -> None:
		super().__init__(parent)
		self.__content:str = pc(content)
		return
	def build(self) -> str:
		return f"<p>{self.__content}</p>"
	@property
	def content(self) -> str:
		return self.__content
	@content.setter
	def content(self,new_content:str) -> None:
		self.__content = pc(new_content)
		return

class Comment(Tag):
	def __init__(self,parent:parent_type,content:str) -> None:
		super().__init__(parent)
		self.__content:str = pc(content)
		return
	def build(self) -> str:
		return f"<!-- {self.__content} -->"
	@property
	def content(self) -> str:
		return self.__content
	@content.setter
	def content(self,new_content:str) -> None:
		self.__content = pc(new_content)
		return
