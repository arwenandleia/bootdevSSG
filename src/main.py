from copy_src_to_dest import copy_src_to_dest
from generate_page import generate_page
import os
import shutil
import sys

TEMPLATE_FILE = './template.html'
CONTENT_FOLDER = './content/'
PUBLIC_FOLDER = './public/'
DEFAULT_BASEPATH = '/'

DEST_FOLDER = './public/'
SOURCE_STATIC_FOLDER = './static/'

def main():
    basepath = DEFAULT_BASEPATH
    if len(sys.argv) > 1:
        basepath = sys.argv[1]    

    copy_src_to_dest(DEST_FOLDER,SOURCE_STATIC_FOLDER)

    generate_page_recursively(CONTENT_FOLDER,PUBLIC_FOLDER,basepath)

    

def generate_page_recursively(origin,dest,basepath):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for filename in os.listdir(origin):
        from_path = os.path.join(origin, filename)
        dest_path = os.path.join(dest, filename)
        
        if os.path.isfile(from_path):
            dest_file = dest_path[:-2]+'html'
            generate_page(from_path,TEMPLATE_FILE,dest_file)
        else:
            generate_page_recursively(from_path, dest_path,basepath)       


if __name__ == '__main__':
    main()