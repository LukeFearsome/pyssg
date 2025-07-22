import os
from src.markdown_to_htmlnodes import markdown_to_htmlnodes

def recursive_page_generation(src,tmpl,dst,basepath):
    for item in os.listdir(src):
        if item.endswith(".md"):
            generate_page(os.path.join(src,item),tmpl,os.path.join(dst,item.replace(".md",".html")),basepath)
        if os.path.isdir(os.path.join(src,item)):
            os.mkdir(os.path.join(dst,item))
            recursive_page_generation(os.path.join(src,item),tmpl,os.path.join(dst,item),basepath)


def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.strip().startswith("# "):
            return line.strip()[2:]
    raise Exception("No main heading found.")


def generate_page(from_path, template_path,dest_path,basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path,'r') as f:
        content = f.read()
    with open(template_path, 'r') as f:
        template = f.read()
    
    title = extract_title(content)
    content_html = markdown_to_htmlnodes(content).to_html()

    page = template.replace("{{ Title }}",title).replace("{{ Content }}",content_html)
    if basepath != '/':
        print("replacing basepath links")
        page = page.replace("href=\"/",f"href=\"{basepath}").replace("src=\"/",f"src=\"{basepath}")
    
    with open(dest_path,'w') as f:
        f.write(page)

