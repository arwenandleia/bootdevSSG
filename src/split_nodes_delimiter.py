from textnode import TextType,TextNode


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
            
        

        