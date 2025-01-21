# counts errors a child makes in entire dialogue

import pandas as pd
import re
from constants import TO_DATA, CHAT_SYMBOLS

def countErrors(child_id:str) -> tuple:
    
    path = f'{TO_DATA}cwe_lines/{child_id}_Chronic.csv' # TODO: remove this
    with open(path, 'r') as file:
        df = pd.read_csv(file, sep='\t')
        error_dict = {}

        error_types = list(CHAT_SYMBOLS.keys())

        for error in error_types:
            re_error = re.compile(CHAT_SYMBOLS[error])

            count = 0
            for line in df['line']:
                nr_errors = len(re_error.findall(line))
                count += nr_errors
                
            error_dict[error] = count
    return (child_id, error_dict)

def countWordsLines(child_id:str) -> tuple:
    path = f'{TO_DATA}cwe_lines/{child_id}_Chronic.csv' # TODO: remove this
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

        count_dict = {'nr_words': nr_words, 
                      'nr_lines': len(df),
                      'nr_words_per_line': round(nr_words/len(df), 3)}

    return (child_id, count_dict)


print(countErrors('C302'))
print(countWordsLines('C302'))