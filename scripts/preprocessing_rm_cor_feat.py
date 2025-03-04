'''preprocessing
remove correlated features '''

import sys
sys.path.append('../')

import pandas as pd

from src.constants import TO_DATA

df = pd.read_csv(f'{TO_DATA}all_errors_words.csv', sep=';')
rm_features = ['unfilled_pause_longest', 'nonword', 'filled_pause', 'nr_words', ]
df = df.drop(columns=rm_features)

print(df.head())