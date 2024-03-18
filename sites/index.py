from pyhtml import Site, Locations, HTML

Index:Site = Site()

Index.add_element(Locations.HEADER, element=HTML.title("OwO"))
Index.add_element(Locations.BODY, element="HEWWO!")
