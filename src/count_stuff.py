# This file contains functions that count the number of errors, words, lines, etc. in a given file.

import pandas as pd
import re

from src.constants import CHAT_SYMBOLS

def countErrors(path:str) -> dict: 
    """Counts speech errors (e.g. repetition, pause, filled_pause etc.) in a docuent.

    Args:
        path (str): path to a .csv file

    Returns:
        dict: 
    """
    with open(path, 'r') as file:
        df = pd.read_csv(file, sep='\t')
        
        # initialize dictionary with child_id already added
        error_dict = {'child_id': list(set(df['child_id']))}

        error_types = list(CHAT_SYMBOLS.keys())

        for error in error_types:
            re_error = re.compile(CHAT_SYMBOLS[error])

            count = 0
            for line in df['line']:
                nr_errors = len(re_error.findall(line))
                count += nr_errors
                
            error_dict[error] = [count]
            
    return (error_dict)

def countWordsLines(path:str) -> dict:
    """Counts the number of words in a line of text.

    Args:
        path (str): _description_

    Returns:
        dict: _description_
    """
    with open(path, 'r') as file:
        df = pd.read_csv(file, sep='\t')
        nr_words = 0

        remove_words = list(CHAT_SYMBOLS.values())
        remove_words.append(r'\.')
        # TODO: there are more symbols that need to be removed try counter

        for line in df['line']:
            
            # remove all unwanted "words" (i.e. CHAT symbols)
            for word in remove_words:
                line = re.sub(word, '', line)

            nr_words += len(line.split())

        count_dict = {'child_id': list(set(df['child_id'])),
                      'nr_words': [(nr_words)], 
                      'nr_lines': [(len(df))],
                      'nr_words_per_line': [(round(nr_words/len(df), 3))]}
        
    return (count_dict)