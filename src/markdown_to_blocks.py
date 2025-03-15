


def markdown_to_blocks(markdown):
    raw_list_of_blocks = markdown.split('\n\n')
    final_list_of_blocks = []
    for block in raw_list_of_blocks:
        stripped_block = block.strip()
        if stripped_block != '':
            final_list_of_blocks.append(stripped_block)

    return final_list_of_blocks

            
           
            
            


