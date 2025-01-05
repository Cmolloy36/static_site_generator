import os
from markdown_to_html_node import *

from_path = 'content/index.md'
template_path = 'template.html'
dest_path = 'public/index.html'

def generate_page(from_path=from_path, template_path=template_path, dest_path=dest_path):
    '''
    Generates page from markdown file at from_path, using template html file at template_path,
    and writes to file at dest_path.
    Paths are provided relative to the root of this folder
    '''

    dest_path_list = dest_path.split('/')
    dest_fnm = dest_path_list.pop()
    dest_path = '/'.join(dest_path_list)

    cwd = os.getcwd()
    from_path = os.path.join(cwd,from_path)
    template_path = os.path.join(cwd,template_path)
    dest_path = os.path.join(cwd,dest_path)

    print(f'Generating page from {from_path} to {dest_path} using {template_path}...')

    with open(from_path,'r') as from_file:
        from_md = from_file.read() # if file is too big... oh well
    with open(template_path,'r') as template_file:
        template_html = template_file.read()

    try:
        title, content = extract_title(from_md)
    except Exception as e:
        print('Error: ',e)
        
    from_html = markdown_to_html_node(content).to_html()

    print(title)
    template_html_replaced = template_html.replace(' {{ Title }} ',title).replace('{{ Content }}', from_html)
    print(template_html_replaced)

    dest_file_path = os.path.join(dest_path,dest_fnm)

    if os.path.exists(dest_path):
        with open(dest_file_path,'w') as f:
            f.write(template_html_replaced)
    else:
        os.makedirs(dest_path)
        with open(dest_file_path,'w') as f:
            f.write(template_html_replaced)


