def main():
    for page in pages:
        template = open("templates/base.html").read()
        content = open(page['filename']).read()
        combined1 = template.replace("{{content_placeholder}}", content)
        combined2 = combined1.replace("{{title_ph}}", page['title'])
        combined3 = combined2.replace(page['link'], "box")
        open(page['output'], "w+").write(combined3)


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


main()
