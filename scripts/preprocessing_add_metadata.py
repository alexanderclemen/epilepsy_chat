# This script adds metadata to the errors_words.csv file, recodes gender, and splits data into all, chronic, and new onset.
import pandas as pd
import sys
sys.path.append("../")

from src.constants import TO_POLER, TO_DATA

# read in data
df_errs_wrds = pd.read_csv(f"{TO_DATA}errors_words.csv", sep=';')
df_meta = pd.read_excel(f"{TO_POLER}0demo.xls", sheet_name='Sheet1')

#### 1) add metadata ####

# subset df_meta to only include child_id, age, EOWAT
df_meta = df_meta[['SUBNBR', 'Age (months)', 'Gender', 'GROUP ID']]
df_meta.rename(columns={'SUBNBR': 'child_id', 
                        'Age (months)': 'age_months',
                        'Gender': 'gender', 
                        'GROUP ID': 'cwe_type'
                        }, inplace=True)


# match child_id to df_errs_wrds
df_meta['child_id'] = 'C' + df_meta['child_id'].astype(str)
df_meta['cwe_sick'] = [0 if "Match" in child else 1 for child in df_meta['cwe_type']]

# merge dataframes
df = pd.merge(df_errs_wrds, df_meta, on='child_id', how='left')

#### 2) recode meta data such that analysis wors #####
df.loc[df['gender'] == 'm', 'gender'] = 0
df.loc[df['gender'] == 'f', 'gender'] = 1

#### 3) split data into chronic and new onset and save
df_chronic = df[df['cwe_type'].str.contains('Chronic', na=False)]
df_newonset = df[df['cwe_type'].str.contains('New Onset', na=False)]

df_chronic.to_csv(f'{TO_DATA}cwe_chronic.csv', sep=';')
df_newonset.to_csv(f'{TO_DATA}cwe_newonset.csv', sep=';')
df.to_csv(f"{TO_DATA}cwe_all.csv", sep=';')