from split_nodes_delimiter import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link
)
from textnode import TextNode,TextType


def text_to_textnodes(text):
    type_delimiters = [
        ('**',TextType.BOLD),
        ('_',TextType.ITALIC),
        ('`',TextType.CODE)
    ]

    curr_nodes = [
        TextNode(text,TextType.TEXT)
    ]

    for delimiter,text_type in type_delimiters:
        curr_nodes = split_nodes_delimiter(
            curr_nodes,
            delimiter,
            text_type
        )
    
    curr_nodes = split_nodes_image(curr_nodes)
    curr_nodes = split_nodes_link(curr_nodes)

    return curr_nodes
