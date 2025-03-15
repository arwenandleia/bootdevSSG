# converts a full markdown document into a single parent HTMLNode. 
import re
from markdown_to_blocks import markdown_to_blocks
from blocktypes import block_to_block_type, BlockType
from htmlnode import ParentNode
from text_to_textnodes import text_to_textnodes
from textnode_to_htmlnode import text_node_to_html_node
from textnode import TextNode,TextType


def markdown_to_html_node(markdown):
    # Returns an HTML NODE ---> so use HTMLNode.to_html method
    # 1. Split the markdown into blocks
    
    markdown_blocks = markdown_to_blocks(markdown) #list of blocks
    list_of_nodes_from_blocks = []

    for block in markdown_blocks:
        type_of_block = block_to_block_type(block) # Gives back type of block .. eg heading, code, paragraph
        
        match type_of_block:
            case BlockType.PARAGRAPH:
                child_nodes_of_block = text_to_children(block)
                para_parent = parent_node_from_children('p',child_nodes_of_block)
                list_of_nodes_from_blocks.append(para_parent)
            case BlockType.HEADING:
                list_of_nodes_from_blocks.append(get_heading_node(block))
            case BlockType.CODE:
                stripped_code = block.strip('`').lstrip('\n')
                code_text_node = TextNode(stripped_code,TextType.CODE)
                code_html_node = text_node_to_html_node(code_text_node)
                code_parent_node = ParentNode('pre',children=[code_html_node])
                list_of_nodes_from_blocks.append(code_parent_node)
            case BlockType.QUOTE:
                quote_children = get_children_for_quote(block)
                quote_parent = ParentNode('blockquote',children=quote_children)
                list_of_nodes_from_blocks.append(quote_parent)
            case BlockType.UNORDERED_LIST:
                ul_parent = get_parent_for_unordered_list(block)
                list_of_nodes_from_blocks.append(ul_parent)
            case BlockType.ORDERED_LIST:
                ol_parent = get_parent_for_ordered_list(block)
                list_of_nodes_from_blocks.append(ol_parent)
            case _:
                raise Exception('Unknown Block Type')
            
    return ParentNode('div',list_of_nodes_from_blocks)


def get_parent_for_ordered_list(block):
    ol_children = []
    list_of_lines = block.split('\n')
    for line in list_of_lines:
        list_item = line[3:]
        line_child_nodes = text_to_children(list_item)
        line_node = ParentNode('li',children=line_child_nodes)
        ol_children.append(line_node)
        

    return ParentNode('ol',children=ol_children)


def get_parent_for_unordered_list(block):
    ul_children = []
    list_of_lines = block.split('\n')
    for line in list_of_lines:
        list_item = line[2:]
        line_child_nodes = text_to_children(list_item)
        line_node = ParentNode('li',children=line_child_nodes)
        ul_children.append(line_node)
        

    return ParentNode('ul',children=ul_children)


def get_children_for_quote(quote_block):
    actual_quote = ''
    list_of_lines = quote_block.strip().split('\n')
    
    for line in list_of_lines:
        quote_on_line =line.lstrip('>') 
        if quote_on_line:
            actual_quote += quote_on_line

    actual_quote = actual_quote.strip()
    return text_to_children(actual_quote)


def get_heading_node(block_text):
    heading,value = re.findall(r'(^#{1,6} )(.*)',block_text)[0]
    heading_num = len(heading)-1
    heading_tag = f'h{heading_num}'
    children_of_heading_tag = text_to_children(value)
    heading_parent = parent_node_from_children(heading_tag,children_of_heading_tag)
    return heading_parent
    

def text_to_children(block_text): # takes block text and returns a list of children nodes
    child_nodes = []
    text_nodes = text_to_textnodes(block_text.replace('\n',' '))
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        child_nodes.append(html_node)

    return child_nodes

def parent_node_from_children(parent_tag,child_nodes): #takes childnodes and tag for parent and returns a ParentNode
    parent_node = ParentNode(parent_tag,children=child_nodes)
    return parent_node




    
    
    

    
    
