from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'


def block_to_block_type(single_block):
    
    if re.findall(r'^#{1,6} ',single_block):
        return BlockType.HEADING
    
    if (
        len(single_block.strip('\n')) >=6
        and single_block.strip('\n')[0:3]=='```'
        and single_block.strip('\n')[-3:]=='```'
    ):
        return BlockType.CODE
    
    if is_block_a_quote(single_block):
        return BlockType.QUOTE

    if is_block_unordered_list(single_block):
        return BlockType.UNORDERED_LIST
    
    if is_block_ordered_list(single_block):
        return BlockType.ORDERED_LIST

    


    
    

    return BlockType.PARAGRAPH

def is_block_ordered_list(block):
    list_of_lines = block.split('\n')
    if not list_of_lines:
        return False
    i=1
    for line in list_of_lines:
        if len(line)<3:
            return False
        if line[0:3] != f'{i}. ':
            return False
        i += 1
        
    return True


def is_block_unordered_list(block):
    list_of_lines = block.split('\n')
    if not list_of_lines:
        return False
    for line in list_of_lines:
        if len(line) < 2:
            return False
        if line[0:2] != '- ':
            return False
    return True

def is_block_a_quote(block):
    list_of_lines = block.split('\n')
    if not list_of_lines:
        return False
    for line in list_of_lines:
        if not line:
            return False
        if line[0] != '>':
            return False
    return True

