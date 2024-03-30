def prepare_content(content:str) -> str:
	return content.replace("\n","<br>").replace("|line|","<hr>")