from util import create_pages

def get_command():
    import sys
    print("This is argv:", sys.argv)
    if len(sys.argv) < 2:
        print("Please specify 'build' or 'new'")
        sys.exit(1)  # abort because of error
    elif len(sys.argv) == 2:
        command = sys.argv[1]
        print(command)
        if command == "build":
            print("Build was specified")
            create_pages()
        elif command == "new":
            print("New page was specified")
            title = input('Title of new page? ')
            title_lower = title.lower()
            import re
            sanitized_title = re.sub(r'[^a-zA-Z]', "_", title_lower)
            open('content/' + sanitized_title + '.html', 'w+').write(
'''
<h1>New Content!</h1>
<p>New content...</p>
'''
            )            
        else:
            print("Please specify 'build' or 'new'")

def main():
    get_command()

if __name__ == "__main__":
    main()
    
    
