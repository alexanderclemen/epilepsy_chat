# create df of errors
import pandas as pd
import sys
sys.path.append("../")

from src.findFiles import findCsvs
from src.count_stuff import countErrors, countWordsLines
from src.constants import TO_DATA

df_errors = pd.DataFrame()
df_words = pd.DataFrame()

files = findCsvs()

for file in files:
    # create df of errors
    temp_df = pd.DataFrame(countErrors(file))
    df_errors = pd.concat([df_errors, temp_df], ignore_index=True)
    
    # create df of words / lines
    temp_df = pd.DataFrame(countWordsLines(file))
    df_words = pd.concat([df_words, temp_df], ignore_index=True)

# removes duplicat child_id
cols_to_use = df_words.columns.difference(df_errors.columns) 
# merge dataframes
df = pd.concat([df_errors,df_words[cols_to_use]], axis=1)

# dave data
df.to_csv(f'{TO_DATA}errors_words.csv', index=False, sep=';')