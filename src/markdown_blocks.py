import re
from enum import Enum

class BlockType(Enum):
    P = "paragraph"
    H = "heading"
    C = "code"
    Q = "quote"
    UL = "unordered_list"
    OL = "ordered_list"

def markdown_to_blocks(markdown):
    out = []
    splits = markdown.split('\n\n')
    for split in splits:
        if not len(split):
            continue
        out.append(split.strip())
    return out
       
def block_to_blocktype(block):
    if re.search(r"#+ ", block):
        return BlockType.H
    if block.startswith("```"):
        return BlockType.C
    if all([line.strip().startswith('>') for line in block.split('\n')]):
        return BlockType.Q
    if all([line.strip().startswith('-') for line in block.split('\n')]):
        return BlockType.UL
    if all([re.search(r"\d+\.",line) for line in block.split('\n')]): 
        return BlockType.OL
    
    return BlockType.P        

