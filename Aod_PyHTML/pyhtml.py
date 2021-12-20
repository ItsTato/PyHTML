
# def HTML(html:str,doctype:str="html"):
#   return f"""
#<!DOCTYPE {doctype}>
#<html>
#{html}
#</html>
#   """

class Internal():
    def __init__(self):
        self.Utils = Internal.Utils(__name__)
        self.Utils.main_file_check()

    class Utils():
        def __init__(self,name) -> None:
            import os,sys
            self.os,self.sys = os,sys
            self.name = name
        def clear_console(self) -> None:
            self.os.system("cls" if self.os.name in ["nt"] else "clear")
        def main_file_check(self) -> None:
            if self.name == "__main__": print("You cannot run this file individually."); self.sys.exit(1)

    class Chars():
        def Quote() -> str:
            return "\""

Internal = Internal()
Internal.Utils.main_file_check()

class Locations():

    def root() -> str:
        return "root"

    def header() -> str:
        return "header"

    def body() -> str:
        return "body"

class HTML():

    def __init__(self) -> None:
        Internal.Utils.main_file_check()
        pass

    def title(title:str) -> str:
        return f"<title>{title}</title>"

class Site():
    def __init__(self) -> None:
        Internal.Utils.main_file_check()
        self.elements = [ ]
        self.header_elements = [ ]
        self.body_elements = [ ]
        self.css_classes = { }

    def add_element(self,location:str,element:str) -> None:
        if location == Locations.root:
            self.elements.append(element)
        if location == Locations.header:
            self.header_elements.append(element)
        if location == Locations.body:
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
        self.html = f"""<!DOCTYPE html>
<html>
    <head>
        {Header}
    </head>
    <body>
        {Body}
    </body>
</html>
        """

    def html(self) -> str:
        return self.html
