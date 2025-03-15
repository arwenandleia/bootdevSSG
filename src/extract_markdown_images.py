import re

def extract_markdown_images(text):
    # regex_exp = r'!\[(.*?)\]\((.*?)\)'
    regex_exp = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_exp,text)
    return matches


def extract_markdown_links(text):
    #regex_exp = r'^[^!]\[(.*?)\]\((.*?)\)'
    regex_exp = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_exp,text)
    
    return matches