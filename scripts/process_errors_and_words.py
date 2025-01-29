# create df of errors
import pandas as pd
import sys
sys.path.append("..")

from src.findFiles import findCsvs
from src.count_stuff import countErrors, countWordsLines
from src.constants import CWE_TYPES, TO_DATA

files = []
df_errors = pd.DataFrame()
df_words = pd.DataFrame()

for cwe_type in CWE_TYPES:
    # TODO: maybe avoid findCSsvs because it is a oneliner
    file = findCsvs(cwe_type)
    files.extend(file)
    
    for file in files:
        temp_df = pd.DataFrame(countErrors(file))
        df_errors = pd.concat([df_errors, temp_df], ignore_index=True)
        
        temp_df = pd.DataFrame(countWordsLines(file))
        df_words = pd.concat([df_words, temp_df], ignore_index=True)

cols_to_use = df_words.columns.difference(df_errors.columns) # removes duplicat child_id
df = pd.concat([df_errors,df_words[cols_to_use]], axis=1)

df.to_csv(f'{TO_DATA}errors_words.csv', index=False, sep='\t')