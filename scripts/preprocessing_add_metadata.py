'''preprocessing
adds metadata () from 0demo.xls to errors_words.csv
adds 'cwe_sick' column
recodes 'gender': 'm': 0 and 'f': 1
splits data into chronic and recent onset
'''


# This script adds metadata to the errors_words.csv file.

import pandas as pd
import sys
sys.path.append("..")

from src.constants import TO_POLER, TO_DATA

# read in data
df_errs_wrds = pd.read_csv(f"{TO_DATA}errors_words.csv", sep='\t')
df_meta = pd.read_excel(f"{TO_POLER}0demo.xls", sheet_name='Sheet1')

#### 1) add metadata ####

# subset df_meta to only include child_id, age, EOWAT
df_meta = df_meta[['SUBNBR', 'Age (months)', 'Gender', 'GROUP ID']]
df_meta.rename(columns={'SUBNBR': 'child_id', 
                        'Age (months)': 'age_months',
                        'Gender': 'gender', 
                        'GROUP ID': 'cwe_type'}, inplace=True)

# match child_id to df_errs_wrds
df_meta['child_id'] = 'C' + df_meta['child_id'].astype(str)
df_meta['cwe_sick'] = [0 if "Match" in child else 1 for child in df_meta['cwe_type']]

# merge dataframes
df = pd.merge(df_errs_wrds, df_meta, on='child_id', how='left')

#### 2) recode meta data such that analysis wors #####

# recode gender 'm': 0 and 'f': df.loc[df['gender'] == 'm', 'gender'] = 0
df['gender'] = df['gender'].replace({'m': 0, 'f': 1})

print(df.head( ))
#### 3) split data into chronic and recent and save

df_chronic = df[df['cwe_type'].isin(['Chronic Match', 'Chronic'])]
df_recent = df[df['cwe_type'].isin(['New Onset Match', 'New Onset'])]

df_chronic.to_csv(f'{TO_DATA}cwe_chronic.csv', sep=';')
df_recent.to_csv(f'{TO_DATA}cwe_recent.csv', sep=';')
df.to_csv(f"{TO_DATA}cwe_all.csv", sep=';')

