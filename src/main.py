from textnode import TextNode,TextType

def main():
    node = TextNode("sample text", TextType.BOLD,"www.test.net")
    print(node)

if __name__ == "__main__":
    main()
