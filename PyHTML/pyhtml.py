
class Utils():
	def __init__(self) -> None:
		import os,sys
		self.os,self.sys = os,sys
	def clear_console(self) -> None:
		self.os.system("cls" if self.os.name in ["nt","dos"] else "clear")

class Chars:
	@staticmethod
	def Quote() -> str:
		return "\""

class Locations:
	@staticmethod
	def ROOT() -> None:
		return
	@staticmethod
	def HEADER() -> None:
		return
	@staticmethod
	def BODY() -> None:
		return

class HTML:
	def __init__(self) -> None:
		pass

	@staticmethod
	def title(title:str) -> str:
		return f"<title>{title}</title>"

class Site:
	def __init__(self) -> None:
		self._html:str = ""
		self.elements:list = [ ]
		self.header_elements:list = [ ]
		self.body_elements:list = [ ]
		self.css_classes:dict = { }

	def add_element(self,location,element:str) -> None:
		if location == Locations.ROOT:
			self.elements.append(element)
		if location == Locations.HEADER:
			self.header_elements.append(element)
		if location == Locations.BODY:
			self.body_elements.append(element)

	def build(self) -> None:
		Elements = ""
		for Element in self.header_elements:
			Elements = f"{Elements}{Element}"
		Header = ""
		for Element in self.header_elements:
			Header = f"{Header}{Element}"
		Body = ""
		for Element in self.body_elements:
			Body = f"{Body}{Element}"
		self._html = f"""<!DOCTYPE html>
<html>
	<head>
		{Header}
	</head>
	<body>
		{Body}
	</body>
</html>
		"""

	@property
	def html(self) -> str:
		self.build()
		return self._html
