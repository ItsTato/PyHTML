from .Utils import prepare_content as pc
from .Tag import Tag, parent_type

class Abbreviation(Tag):
	def __init__(self,parent:parent_type,title:str,content:str) -> None:
		super().__init__(parent)
		self.__title:str = pc(title)
		self.__content:str = pc(content)
		return
	def build(self) -> str:
		return f"<abbr title=\"{self.__title}\">{self.__content}</abbr>"
	@property
	def title(self) -> str:
		return self.__title
	@title.setter
	def title(self,new_title:str) -> None:
		self.__title = pc(new_title)
		return
	@property
	def content(self) -> str:
		return self.__content
	@content.setter
	def content(self,new_content:str) -> None:
		self.__content = pc(new_content)
		return

class Address(Tag):
	def __init__(self,parent:parent_type,content:str) -> None:
		super().__init__(parent)
		self.__content:str = pc(content)
		return
	def build(self) -> str:
		return f"<address>{self.__content}</address>"
	@property
	def content(self) -> str:
		return self.__content
	@content.setter
	def content(self,new_content:str) -> None:
		self.__content = pc(new_content)
		return

class Bold(Tag):
	def __init__(self,parent:parent_type,content:str) -> None:
		super().__init__(parent)
		self.__content:str = pc(content)
		return
	def build(self) -> str:
		return f"<bold>{self.__content}</bold>"
	@property
	def content(self) -> str:
		return self.__content
	@content.setter
	def content(self,new_content:str) -> None:
		self.__content = pc(new_content)
		return

class BiDirectionalIsolation(Tag):
	def __init__(self,parent:parent_type,content:str) -> None:
		super().__init__(parent)
		self.__content:str = pc(content)
		return
	def build(self) -> str:
		return f"<bdi>{self.__content}</bdi>"
	@property
	def content(self) -> str:
		return self.__content
	@content.setter
	def content(self,new_content:str) -> None:
		self.__content = pc(new_content)
		return
BDI = BiDirectionalIsolation

class BiDirectionalOverride(Tag):
	def __init__(self,parent:parent_type,content:str,left_to_right:bool=False) -> None:
		super().__init__(parent)
		self.__text_direction:str = "ltr" if left_to_right else "rtl"
		self.__content:str = pc(content)
		return
	def build(self) -> str:
		return f"<bdo dir=\"{self.__text_direction}\">{self.__content}</bdo>"
	@property
	def text_direction(self) -> str:
		return self.__text_direction
	@text_direction.setter
	def text_direction(self,new_direction:str) -> None:
		if new_direction not in ["ltr","rtl"]:
			raise AttributeError("new_direction must be either \"ltr\" or \"rtl\"")
		self.__text_direction = new_direction
		return
	@property
	def content(self) -> str:
		return self.__content
	@content.setter
	def content(self,new_content:str) -> None:
		self.__content = pc(new_content)
		return

class BlockQuote(Tag):
	def __init__(self,parent:parent_type,source:str,content:str) -> None:
		super().__init__(parent)
		self.__source:str = pc(source)
		self.__content:str = pc(content)
		return
	def build(self) -> str:
		return f"<blockquote cite=\"{self.__source}\">{self.__content}</blockquote>"
	@property
	def source(self) -> str:
		return self.__source
	@source.setter
	def source(self,new_source:str) -> None:
		self.__source = pc(new_source)
		return
	@property
	def content(self) -> str:
		return self.__content
	@content.setter
	def content(self,new_content:str) -> None:
		self.__content = pc(new_content)
		return

class Cite(Tag):
	def __init__(self,parent:parent_type,content:str) -> None:
		super().__init__(parent)
		self.__content:str = pc(content)
		return
	def build(self) -> str:
		return f"<cite>{self.__content}</cite>"
	@property
	def content(self) -> str:
		return self.__content
	@content.setter
	def content(self,new_content:str) -> None:
		self.__content = pc(new_content)
		return

class Code(Tag):
	def __init__(self,parent:parent_type,content:str) -> None:
		super().__init__(parent)
		self.__content:str = pc(content)
		return
	def build(self) -> str:
		return f"<code>{self.__content}</code>"
	@property
	def content(self) -> str:
		return self.__content
	@content.setter
	def content(self,new_content:str) -> None:
		self.__content = pc(new_content)
		return

class Deleted(Tag):
	def __init__(self,parent:parent_type,content:str) -> None:
		super().__init__(parent)
		self.__content:str = pc(content)
		return
	def build(self) -> str:
		return f"<del>{self.__content}</del>"
	@property
	def content(self) -> str:
		return self.__content
	@content.setter
	def content(self,new_content:str) -> None:
		self.__content = pc(new_content)
		return
Crossed_Out = Deleted

class Definition(Tag):
	def __init__(self,parent:parent_type,title:str,content:str) -> None:
		super().__init__(parent)
		self.__title: str = pc(title)
		self.__content: str = pc(content)
		return
	def build(self) -> str:
		return f"<dfn title=\"{self.__title}\">{self.__content}</dfn>"
	@property
	def title(self) -> str:
		return self.__title
	@title.setter
	def title(self,new_title:str) -> None:
		self.__title = pc(new_title)
		return
	@property
	def content(self) -> str:
		return self.__content
	@content.setter
	def content(self,new_content:str) -> None:
		self.__content = pc(new_content)
		return


