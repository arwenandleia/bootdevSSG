

class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('Should be overriden by Child classes')
    
    def props_to_html(self):
        prop_string = ''
        if not self.props:
            return prop_string
        for k,v in self.props.items():
            prop_string += f' {k}="{v}"'
        return prop_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value,  props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError('All leaf nodes must have a value')
        if not self.tag:
            return f'{self.value}'
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError('Parent Node Must have a tag')
        if not self.children:
            raise ValueError('ParentNode must have atleast one child')
        
        ret_html = ''
        ret_html += f'<{self.tag}{self.props_to_html()}>'
        
        for child in self.children:
            ret_html += child.to_html()
            

        ret_html += f'</{self.tag}>'
        return ret_html



        
    

    

    
