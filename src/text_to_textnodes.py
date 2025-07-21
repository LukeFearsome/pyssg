from src.extract_regex import split_nodes_images,split_nodes_links
from src.textnode import TextNode,TextType,split_nodes_delimiter


def text_to_textnodes(text):
    nodes = [TextNode(text,TextType.PLAIN)]

    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes,"_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes,"`",TextType.CODE)
   
    return nodes

