import sys

from src.copy_static import copy_static
from src.create_html import recursive_page_generation

basepath = sys.argv[1]
print(f"Basepath is: {basepath}")

def main():
    copy_static("./docs/")
    recursive_page_generation("content","template.html","docs",basepath)
    
if __name__ == "__main__":
    main()
