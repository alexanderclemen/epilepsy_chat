# cleans each line before saving

import re

def removeDotString(line:str, regex = re.compile(r' \w{1,13}')) -> str:
     #  works but \\x15 does not
    line = re.sub(pattern = regex, repl = '', string = line)
    return line


def cleanLine(line:str) -> str:
    """clean a utterance
    
    Args:
        line (str): initial utterance
        
    Returns: cleaned utterance
    """
    # remove  preambel ('*CHI\t') and postamble ('\n')
    line = line[6:].strip()
    
    # remove .cha specific symbol
    line = removeDotString(line)
    return line