from constants import TO_POLER
from clean_utterances import cleanUtterance

# read file in /data/POLER/
def readChiUtterances(child_id:str, folder:str) -> list:
    """reads a single CHAT file and returns a list of all utterances

    Args:
        child_id (str): id of child
        folder (str): name of folder in /data/POLER/ that contains the CHAT file
    """
    lines = []
    with open(f'{TO_POLER}{folder}/{child_id}.cha', 'r') as file:
        # read a list of lines into data
        for line in file:
            # if line starts with *CHI (the childs utterance) keep it
            if line.startswith('*CHI'):
                
                # preprocessing of lines
                line = cleanUtterance(line)
                
                # append line to list of lines
                lines.append(line)
    return lines