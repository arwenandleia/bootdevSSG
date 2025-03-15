from textnode import TextType,TextNode
from extract_markdown_images import (
    extract_markdown_images,
    extract_markdown_links
)


# old_nodes -> list, 

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        old_node_text = old_node.text 
        split_up_text = old_node_text.split(delimiter,maxsplit=2)
        if len(split_up_text) % 2 ==0:
            print(split_up_text)
            raise Exception('Delimiter is not balanced')

        while len(split_up_text)==3:
            if split_up_text[0] != '':
                new_nodes.append(TextNode(split_up_text[0],TextType.TEXT))
            new_nodes.append(TextNode(split_up_text[1],text_type))
            split_up_text = split_up_text[2].split(delimiter,maxsplit=2)
            if len(split_up_text) % 2 ==0:
                print(split_up_text)
                raise Exception('Delimiter is not balanced')
        if split_up_text[0] != '':
            new_nodes.append(TextNode(split_up_text[0],TextType.TEXT))

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        
        old_node_text = old_node.text
        links_list = extract_markdown_images(old_node_text)
        
        while links_list:
            alt_text,image_url = links_list.pop(0)
            split_text = old_node_text.split(f'![{alt_text}]({image_url})',maxsplit=1)
                                        
            if split_text[0] != '':
                new_nodes.append(TextNode(split_text[0],TextType.TEXT))

            new_nodes.append(TextNode(alt_text,TextType.IMAGE,image_url))
            if len(split_text)==2:
                old_node_text = split_text[1]
            else:
                old_node_text=''

        if old_node_text != '':
            new_nodes.append(TextNode(old_node_text,TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        
        old_node_text = old_node.text
        links_list = extract_markdown_links(old_node_text)
        
        while links_list:
            link_text,link_url = links_list.pop(0)
            split_text = old_node_text.split(f'[{link_text}]({link_url})',maxsplit=1)
                                        
            if split_text[0] != '':
                new_nodes.append(TextNode(split_text[0],TextType.TEXT))

            new_nodes.append(TextNode(link_text,TextType.LINK,link_url))
            if len(split_text)==2:
                old_node_text = split_text[1]
            else:
                old_node_text=''

        if old_node_text != '':
            new_nodes.append(TextNode(old_node_text,TextType.TEXT))

    return new_nodes


            
        

        