from src.htmlnode import LeafNode, ParentNode
from src.markdown_blocks import BlockType, block_to_blocktype, markdown_to_blocks
from src.text_to_textnodes import text_to_textnodes
from src.textnode import textnode_to_htmlnode


def markdown_to_htmlnodes(markdown):
    parent_nodes = []
    for block in markdown_to_blocks(markdown):

        match block_to_blocktype(block):
            case BlockType.P:
                cleaned_text = block.replace('\n',' ').strip()
                parent_nodes.append(ParentNode('p',block_to_children(cleaned_text)))
                continue
            case BlockType.H:
                h_num,cleaned_text = heading_processor(block)
                parent_nodes.append(ParentNode(f"h{h_num}",block_to_children(cleaned_text)))
                continue
            case BlockType.C:
                cleaned_text = block.replace("```",'').lstrip()
                inner_node = LeafNode("code",cleaned_text)
                code_node = ParentNode("pre",[inner_node])
                parent_nodes.append(code_node)
                continue
            case BlockType.Q:
                cleaned_text = block.replace('>','')
                continue
            case BlockType.UL:
                item_nodes = list_processor(block.split('\n'))
                parent_nodes.append(ParentNode("ul",item_nodes))
                continue
            case BlockType.OL:
                item_nodes = list_processor(block.split('\n'))
                parent_nodes.append(ParentNode("ol",item_nodes))
                continue

    return ParentNode('div',parent_nodes)
    

def block_to_children(block):
        children = []
        for textnode in text_to_textnodes(block):
            children.append(textnode_to_htmlnode(textnode))
        return children

def list_processor(items):
    item_nodes = []
    for item in items:
        cleaned_item = ' '.join(item.strip().split(' ')[1:])
        children = block_to_children(cleaned_item)
        item_nodes.append(ParentNode("li",children))

def heading_processor(block):
    i = 0
    while block[i] == '#':
        i += 1
    return i, block[i+1:]

