from copy_src_to_dest import copy_src_to_dest
from generate_page import generate_page
import os
import shutil

TEMPLATE_FILE = './template.html'
CONTENT_FOLDER = './content/'
PUBLIC_FOLDER = './public/'

def main():
    copy_src_to_dest()

    generate_page_recursively(CONTENT_FOLDER,PUBLIC_FOLDER)

    

def generate_page_recursively(origin,dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for filename in os.listdir(origin):
        from_path = os.path.join(origin, filename)
        dest_path = os.path.join(dest, filename)
        
        if os.path.isfile(from_path):
            dest_file = dest_path[:-2]+'html'
            generate_page(from_path,TEMPLATE_FILE,dest_file)
        else:
            generate_page_recursively(from_path, dest_path)       


if __name__ == '__main__':
    main()