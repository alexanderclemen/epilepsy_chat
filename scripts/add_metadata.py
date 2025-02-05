# This script adds metadata to the errors_words.csv file.

import pandas as pd
import sys
sys.path.append("..")

from src.constants import TO_POLER, TO_DATA

# read in data
df_errs_wrds = pd.read_csv(f"{TO_DATA}errors_words.csv", sep='\t')
df_meta = pd.read_excel(f"{TO_POLER}0demo.xls", sheet_name='Sheet1')
print(len(df_meta))
# subset df_meta to only include child_id, age, EOWAT
df_meta = df_meta[['SUBNBR', 'Age (months)', 'Gender', 'GROUP ID', 'EOWVTSS']]
df_meta.rename(columns={'SUBNBR': 'child_id', 
                        'Age (months)': 'age_months',
                        'Gender': 'gender', 
                        'GROUP ID': 'cwe_type', 
                        'EOWVTSS': 'eowpvt'}, inplace=True)

# match child_id to df_errs_wrds
df_meta['child_id'] = 'C' + df_meta['child_id'].astype(str)
df_meta['cwe_sick'] = [0 if "Match" in child else 1 for child in df_meta['cwe_type']]

# merge dataframes
df = pd.merge(df_errs_wrds, df_meta, on='child_id', how='left')

df.to_csv(f"{TO_DATA}cwe_data.csv", sep=';', index=False)