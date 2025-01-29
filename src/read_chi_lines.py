# reads cha files, extracts only children lines, leans them and returns them as a list of tuples

from src.clean_lines import cleanLine
from src.constants import TO_POLER

# read file in /data/POLER/
def readChiLines(child_id:str, cwe_type:str) -> list:
    """reads a single CHAT file and returns a list of all utterances

    Args:
        child_id (str): id of child
        cwe_type (str): name of cwe_type in /data/POLER/ that contains the CHAT file
        
    Returns: (list) list of tuples (child_id, cwe_type, line)
    """
    lines = []
    with open(f'{TO_POLER}{cwe_type}/{child_id}.cha', 'r') as file:
        line_counter = 0 # for line id
        child_id = f'C{child_id}'
        
        # read a list of lines into data
        for line in file:
            # if line starts with *CHI (the childs utterance) keep it
            if line.startswith('*CHI'):
                
                # preprocessing of lines
                line = cleanLine(line)
                
                # create line id
                line_counter += 1
                line_id = f'U{line_counter:03}_{child_id}'
                
                # append line to list of lines
                lines.append((child_id, cwe_type, line_id, line))
    return lines