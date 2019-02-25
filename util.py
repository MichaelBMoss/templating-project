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
        "link_location": name_only + extension,
        "link_box": '{{' + name_only + '_ph}}',
        })
    return pages

def create_links():    
    from jinja2 import Template
    links_template_string = '''
    {% for page in pages %}
        <a href="{{ page.link_location }}">
            <span class="link {{page.link_box}}"> {{ page.title }}</span>
        </a>
    {% endfor %}
    '''
    links_template = Template(links_template_string)
    links = links_template.render(
        pages=create_list(),
    )
    return links

def create_page():
    from jinja2 import Template
    for page in create_list():  
        content = open(page['filename']).read()  
        base = open("templates/base.html").read()
        template = Template(base)
        rendered_page = template.render(
            title_ph=page['title'],
            content_ph=content,
            links_ph=create_links()
            )
        rendered_page_w_box = rendered_page.replace(page['link_box'], 'box')    
        open(page['output'], "w+").write(rendered_page_w_box)

def main():
    create_page() 
    



