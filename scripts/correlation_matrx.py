import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Set working directory (adjust path as needed)
import os
os.chdir('/home/alex/Documents/02_study/duesseldorf/MA_Linguistik/23_WS_Python/epilepsy_chat/scripts')

# Load data
df = pd.read_csv('../data/cwe_all.csv', sep=';')

# Glimpse the data
print(df.head())

# Create the correlation matrix for selected predictors
predictors = [
    'repetition', 
    'retraction', 
    'unfilled_pause', 
    'unfilled_pause_longer', 
    'unfilled_pause_longest', 
    'nonword',  
    'filled_pause',  
    'error', 
    'nr_lines',
    'nr_words',
    'nr_words_per_line'
]

# Compute the correlation matrix
cor_matrix = df[predictors].corr()

# Plot the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(cor_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.show()

# Refine predictors by removing highly correlated variables and others with missing data
predictors_refined = [
    'repetition', # .59 with 'retraction' -> 2 models
    'retraction', # .59 with 'repititopns' -> 2 models
    'unfilled_pause', 
    'unfilled_pause_longer', # vavoured over 'unfilled_pause_longest' because more data
    # 'unfilled_pause_longest', # .62 with 'unfilled_pause_longer'
    # 'nonword',  # removed as there are none
    # 'filled_pause',  # removed as there are none
    'error', 
    'nr_lines',
    # 'nr_words', # .77 with 'nr_lines'
    'nr_words_per_line'
]

cor_matrix_refined = df[predictors_refined].corr()

# Plot refined correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(cor_matrix_refined, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.show()

# Remove irrelevant features
rm_features = ['unfilled_pause_longest', 'nonword', 'filled_pause', 'nr_words']
df = df.drop(columns=rm_features)

# Save the processed dataframe
df.to_csv('../data/cwe_all_selected.csv', sep=';', index=False)



#### Recent children only ####
df_recent = pd.read_csv('../data/cwe_recent.csv', sep=';')

# Glimpse the data
print(df_recent.head())

# Create the correlation matrix for recent children
cor_matrix_recent = df_recent[predictors].corr()

# Plot the correlation matrix for recent children
plt.figure(figsize=(10, 8))
sns.heatmap(cor_matrix_recent, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.show()

# Refine predictors
predictors_refined_recent = [
    'repetition', # .67 with 'retraction' -> 2 models
    'retraction', # .67 with 'repititopns' -> 2 models
    'unfilled_pause', 
    'unfilled_pause_longer', # vavoured over 'unfilled_pause_longest' because more data
    # 'unfilled_pause_longest', # removed as there are none
    # 'nonword',  # removed as there are none
    # 'filled_pause',  # removed as there are none
    'error', 
    'nr_lines',
    # 'nr_words', # .82 with 'nr_lines'
    'nr_words_per_line'
]

cor_matrix_refined_recent = df_recent[predictors_refined_recent].corr()

# Plot refined correlation matrix for recent children
plt.figure(figsize=(10, 8))
sns.heatmap(cor_matrix_refined_recent, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.show()

# Remove irrelevant features
rm_features_recent = ['unfilled_pause_longest', 'nonword', 'filled_pause', 'nr_words']
df_recent = df_recent.drop(columns=rm_features_recent)

# Save the processed dataframe
df_recent.to_csv('../data/cwe_recent_selected.csv', sep=';', index=False)



#### Chronic children only ####
df_chronic = pd.read_csv('../data/cwe_chronic.csv', sep=';')

# Glimpse the data
print(df_chronic.head())

# Create the correlation matrix for chronic children
cor_matrix_chronic = df_chronic[predictors].corr()

# Plot the correlation matrix for chronic children
plt.figure(figsize=(10, 8))
sns.heatmap(cor_matrix_chronic, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.show()

# Refine predictors
predictors_refined_chronic = [
    'repetition',
    'retraction',
    'unfilled_pause', 
    'unfilled_pause_longer',
    'error', 
    'nr_lines',
    'nr_words_per_line'
]

cor_matrix_refined_chronic = df_chronic[predictors_refined_chronic].corr()

# Plot refined correlation matrix for chronic children
plt.figure(figsize=(10, 8))
sns.heatmap(cor_matrix_refined_chronic, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.show()

# Remove irrelevant features
rm_features_chronic = ['unfilled_pause_longest', 'nonword', 'filled_pause', 'nr_words']
df_chronic = df_chronic.drop(columns=rm_features_chronic)

# Save the processed dataframe
df_chronic.to_csv('../data/cwe_chronic_selected.csv', sep=';', index=False)