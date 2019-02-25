def create_list():
    import glob
    all_html_files = glob.glob("content/*.html")
    pages = []
    import os
    for entry in all_html_files:
        file_path = entry
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)
        pages.append({
        "filename": "content/" + name_only + extension,
        "title": name_only,
        "output": "docs/" + name_only + extension,
        "link": name_only + '_ph',
    })
    return pages

def create_page():
    from jinja2 import Template
    for page in create_list():  
        content = open(page['filename']).read()  
        base = open("templates/base.html").read()
        template = Template(base)
        rendered_page = template.render(
            title_ph=page['title'],
            content_ph=content,
        )
        open(page['output'], "w+").write(rendered_page)

def main():
    create_list()
    create_page()
    
if __name__ == "__main__":
    main()


