from enum import Enum
from src.htmlnode import LeafNode

class TextType(Enum):
    PLAIN = "plain text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code text"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self,text,text_type,url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self,comp):
        return self.text == comp.text and self.text_type == comp.text_type and self.url == comp.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def textnode_to_htmlnode(text_node):
    match text_node.text_type:
        case TextType.PLAIN:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode('b',text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode('a',text_node.text,{"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img",'',{"src":text_node.url,"alt":text_node.text})

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    for i,node in enumerate(old_nodes):
        if node.text_type == TextType.PLAIN:
            splits = node.text.split(delimiter)
            if len(splits) < 2:
                continue
            new_nodes = []
            for s,split in enumerate(splits):
                if s % 2 == 0:
                    new_nodes.append(TextNode(split,TextType.PLAIN))
                else:
                    new_nodes.append(TextNode(split,text_type))
            old_nodes = old_nodes[:i] + new_nodes + old_nodes[i+1:]
    return old_nodes

