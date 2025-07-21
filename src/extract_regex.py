import re

from src.textnode import TextNode,TextType

def extract_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matches

def extract_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return matches

def split_nodes_images(in_nodes):
    out_nodes = []
    
    for node in in_nodes:
        text = node.text
        images = extract_images(text)
        for image in images:
            splits = text.split(f"![{image[0]}]({image[1]})")
            if len(splits[0]):
                out_nodes.append(TextNode(splits[0],TextType.PLAIN))
            out_nodes.append(TextNode(image[0],TextType.IMAGE,image[1]))
            text = splits[1]
        if len(text):
            out_nodes.append(TextNode(text,TextType.PLAIN))
    return out_nodes

def split_nodes_links(in_nodes):
    out_nodes = []
    
    for node in in_nodes:
        if node.text_type == TextType.IMAGE:
            out_nodes.append(node)
            continue
        text = node.text
        links = extract_links(text)
        for link in links:
            splits = text.split(f"[{link[0]}]({link[1]})")
            if len(splits[0]):
                out_nodes.append(TextNode(splits[0],node.text_type,node.url or None))
            out_nodes.append(TextNode(link[0],TextType.LINK,link[1]))
            text = splits[1]
        if len(text):
            out_nodes.append(TextNode(text,node.text_type, node.url or None))
    return out_nodes

