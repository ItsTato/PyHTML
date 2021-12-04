
def HTML(code:str,doctype:str="html"):
    return f"""
<!DOCTYPE {doctype}>
<html>
{code}
</html>
    """

class Head():
    def open():
        return "<head>"
    
    def title(title:str):
        return f"<title>{title}</title>"
    
    def close():
        return "</head>"

class Body():
    def open():
        return "<body>"
    
    def p(content:str,css:str=""):
        return f"<p style=\"{css}\">{str(content)}</p>"

    def h1(content:str="Header 1"):
        return f"<h1>{str(content)}</h1>"
    
    def h2(content:str="Header 2"):
        return f"<h2>{str(content)}</h2>"
    
    def h3(content:str="Header 3"):
        return f"<h3>{str(content)}</h3>"
    
    def h4(content:str="Header 4"):
        return f"<h4>{str(content)}</h4>"
    
    def h5(content:str="Header 5"):
        return f"<h5>{str(content)}</h5>"
    
    def close():
        return "</body>"
