from src.copy_static import copy_static
from src.create_html import recursive_page_generation

def main():
    copy_static()
    recursive_page_generation("content","template.html","public")
    
if __name__ == "__main__":
    main()
