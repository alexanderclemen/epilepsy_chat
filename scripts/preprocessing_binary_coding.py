import pandas as pd
import sys
sys.path.append("..")

from src.constants import TO_DATA, PREDICTORS

df = pd.read_csv(f'{TO_DATA}cwe_data.csv', sep=';')


non_binary_predictors = ['nr_lines', 
              'nr_words', 
              'nr_words_per_line',
              'gender',
              'age_months']

binary_predictors = set(PREDICTORS) - set(non_binary_predictors)
binary_predictors = list(binary_predictors)

# recode the target variable to 0 and 1
for predictor in binary_predictors:
    # change all values to 0 it they are 0 else 1
    df[predictor] = df[predictor].apply(lambda x: 0 if x == 0 else 1)

# recode gender to 0 and 1
df['gender'] = df['gender'].apply(lambda x: 0 if x == 'm' else 1)

# save data
df.to_csv(f'{TO_DATA}cwe_data_binary.csv', sep=';', index=False)