import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path,template_path,dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path,'r') as markdown_file:
        markdown = markdown_file.read()

    #print(markdown)

    with open(template_path,'r') as html_template_file:
        html_template = html_template_file.read()

    #print(html_template)

    html_node_of_md = markdown_to_html_node(markdown)
    html_string_of_md = html_node_of_md.to_html()
    title_of_file = extract_title(markdown)
    new_file_html = html_template.replace('{{ Title }}',title_of_file).replace('{{ Content }}',html_string_of_md)
    write_html_to_file(dest_path,new_file_html)

def write_html_to_file(dest_path,html_file):
    # check if directory exists
    dir_name = os.path.dirname(dest_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name,exist_ok=True)
    
    with open(dest_path,'w') as write_html_file:
        write_html_file.write(html_file)
        


    

