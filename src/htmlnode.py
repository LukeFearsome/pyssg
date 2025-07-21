class HTMLNode():
    def __init__(self, tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props: return ""
        out = ""
        for key,val in self.props.items():
            out += f" {key}=\"{val}\""
        return out

    def __repr__(self):
        return f"HTMLNode {self.tag} {self.value} {self.children} {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        self.tag = tag
        self.value = value
        self.children = None
        self.props = props
    
    def to_html(self):
        if self.tag:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return self.value
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag.")
        if not self.children:
            raise ValueError("ParentNode has to have children.")
        return f"<{self.tag}{self.props_to_html()}>{''.join([node.to_html() for node in self.children])}</{self.tag}>"

