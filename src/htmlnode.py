class HTMLNode(object):
    """
    tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    value - A string representing the value of the HTML tag (e.g. the text 
    inside a paragraph)
    children - A list of HTMLNode objects representing the children of this 
    node
    props - A dictionary of key-value pairs representing the attributes of 
    the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    """
    
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self,other):
        if (self.tag == other.tag and self.value == other.value and
            self.children == other.children and self.props == other.props):
            return True
        return False

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        # make sure this runs as expected
        if self.props == None:
            return ''
        
        attributes = []
        for ele in self.props:
            attributes.append(f' {ele}="{self.props[ele]}"')
        return ''.join(attributes)
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)

    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    
    def to_html(self):
        if self.value == None:
            raise ValueError('All leaf nodes must have a value')
        elif self.tag == None:
            return self.value
        else:
            # # The below are not needed because props handles the leading space
            # if self.props == None:
            #     htmlstr = f'<{self.tag}>{self.value}</{self.tag}>'
            #     return htmlstr
            # else:    
            props_str = self.props_to_html()
            htmlstr = f'<{self.tag}{props_str}>{self.value}</{self.tag}>'
            return htmlstr
  
class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)

    def __repr__(self):
        return f'ParentNode({self.tag}, {self.children}, {self.props})'
    
    def to_html(self):
        if self.tag == None:
            raise ValueError('All leaf nodes must have a tag')
        
        output_list = []
        for child in self.children:
            if isinstance(child, ParentNode):
                output_list.append(child.to_html())
            elif isinstance(child, LeafNode) and child.value == None:
                raise ValueError('All child LeafNodes must have a value')
            else:
                output_list.append(child.to_html())
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>" + ''.join(output_list) + f"</{self.tag}>"
        