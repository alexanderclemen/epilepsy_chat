# This file contains functions that count the number of errors, words, lines, etc.
import pandas as pd
import re

from src.constants import CHAT_SYMBOLS

def countErrors(path:str) -> dict: 
    """Counts speech errors (e.g. repetition, pause, filled_pause etc.) in a docuent.

    This function scans through the lines of a tab-separated (.csv) file, where speech errors
    are represented by specific CHAT symbols. It counts the occurrences of these errors for each 
    type based on regular expressions, defined in constants.py.
    
    Args:
        path (str): The file path to a tab-separated file.
                    The file needs the columns 'line' and 'child_id'

    Returns:
        dict: A dictionary with the following data:
            - 'child_id': A list of unique child_ids.
            - error type keys: For each error type (e.g., 'repetition', 'retraction' etc.), 
              the dictionary contains the count of occurrences for that error type.
              
            Example structure:
            - 'child_id': ['C332'], 
            - 'repetition': [17], 
            - 'retraction': [12], 
            - 'unfilled_pause': [1], 
            - ...
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
        path (str):The file path to a tab-separated file.
                   The file needs the columns 'line' and 'child_id'

    Returns:
        dict: A dictionary containing the following data:
            - 'child_id': A list of unique child_ids.
            - 'nr_words': A list with the total number of words (after filtering).
            - 'nr_lines': A list with the total number of lines.
            - 'nr_words_per_line': A list with the average number of words per line.
    """
    with open(path, 'r') as file:
        df = pd.read_csv(file, sep='\t')
        nr_words = 0

        chat_symbols = set(CHAT_SYMBOLS.values())
        # these CHAT annotations are not in my predictor pool and contain alphanumeric strings. 
        # I don't want them to count as words.
        chat_symbols = chat_symbols | {'[* sem]', '[* syn]', 'hm:', 'xxx'}
        
        for line in df['line']:
            words = line.split()
            
            # filter words: CHAT symbols and alphanumeric
            # &~uh and &-f contain alphanumeric stings 'uh' and 'f' would be counted as words
            filtered_words = []
            for word in words:
                if word in chat_symbols or word.isalpha():
                    filtered_words.append(word)

            nr_words += len(filtered_words)

        count_dict = {'child_id': list(set(df['child_id'])),
                      'nr_words': [(nr_words)], 
                      'nr_lines': [(len(df))],
                      'nr_words_per_line': [(round(nr_words/len(df), 3))]}
        
    return (count_dict)