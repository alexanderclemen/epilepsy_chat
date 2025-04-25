# cleans each line before saving

import re

def removeDotString(line:str, regex = re.compile(r' \w{1,13}')) -> str:
    """Removes .cha line final symbol.
    
    Args:
        line (str): An line (e.g. "where are you ? 19760_21588")
        regex (re.Pattern): A re pattern, that will be removed (e.g. 19760_21588')
        
    Returns: 
        line (str): The Line without the .cha symbol (e.g. where are you ?)
    """
     # each line ends with a .cha specific symbol, which is removed
    line = re.sub(pattern = regex, repl = '', string = line)
    return line


def cleanLine(line:str) -> str:
    """Removes unwanted caracters from .cha utterances files.
    
    Args:
        line (str): initial utterance (e.g. *CHI:	where are you ? 19760_21588)
                
    Returns: cleaned utterance (e.g. where are you ? )
    """
    # remove  preambel ('*CHI\t') and postamble ('\n')
    # *CHI indicates that the line was uttered by a child
    line = line[6:].strip()
    
    # each line in the CHAT Transcription format contains a string that is irrelevant to the analysis   
    line = removeDotString(line)
    
    # remove everything between <> when &~ is present
    # in the lines, word repetitions, and part word repetitions are 
    # 
    line = re.sub(r'<.*&~.*>', '', line)
    
    return line