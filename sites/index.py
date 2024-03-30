from pyhtml import Site, Locations, HTML
from components.buttons import DefaultButton

class Index(Site):
	def __init__(self) -> None:
		super().__init__()
		self.add_element(Locations.HEADER, element=HTML.title("OwO"))
		self.add_element(Locations.BODY, element="HEWWO!")
