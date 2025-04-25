# This script creates correlation matrixes.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
sys.path.append("../")

from src.constants import TO_DATA

def plot_correlations(cor_matrix, title):
    """Plot a correlation matrix.

    Args:
        cor_matrix (pd.DataFrame): Data for the corr matrix
        title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(cor_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title(title, fontsize=16, pad=20)
    plt.tight_layout()
    plt.show()


df = pd.read_csv(f'{TO_DATA}cwe_all.csv', sep=';')

# list all predictors (once)
predictors = [
    'repetition', 
    'retraction', 
    'unfilled_pause', 
    # 'unfilled_pause_longer', # excluded because not present in all groups
    # 'unfilled_pause_longest', # excluded because not present in all groups 
    'nonword',  
    'filled_pause',  
    'error', 
    'nr_lines',
    'nr_words',
    'nr_words_per_line'
]

#### All children ####
cor_matrix = df[predictors].corr() # calculates correlations
plot_correlations(cor_matrix, title="Correlation Matrix for All Children")

# Refine predictors by removing highly correlated variables and others with missing data
predictors_refined = [
    'repetition', # .59 with 'retraction' -> 2 models
    'retraction', # .59 with 'repititopns' -> 2 models
    'unfilled_pause', 
    'nonword',  
    'filled_pause',  
    'error', 
    'nr_lines',
    # 'nr_words', # corr with 'nr_lines' AND nr_words_per_line
    'nr_words_per_line'
]

# remove features
rm_features = ['unfilled_pause_longer', 'unfilled_pause_longest',  
               'nr_words']
df = df.drop(columns=rm_features)
df.to_csv(f'{TO_DATA}cwe_all_selected.csv', sep=';', index=False)


#### new onset children only ####
df_newonset = pd.read_csv(f'{TO_DATA}cwe_newonset.csv', sep=';')
cor_matrix_newonset = df_newonset[predictors].corr()
plot_correlations(cor_matrix_newonset, title="Correlation Matrix for New Onset Children")

# Refine predictors
predictors_refined_newonset = [
    'repetition', # .69 with 'retraction' -> 2 models
    'retraction', # .69 with 'repititopns' -> 2 models
    'unfilled_pause', 
    'nonword',  
    'filled_pause',  
    'error', 
    'nr_lines',
    # 'nr_words', # corr with 'nr_lines' and nr_words_per_line
    'nr_words_per_line'
]

cor_matrix_refined_newonset = df_newonset[predictors_refined_newonset].corr()

# Remove irrelevant features
rm_features = ['unfilled_pause_longer', 'unfilled_pause_longest', 
               'nr_words']
df_newonset = df_newonset.drop(columns=rm_features)
df_newonset.to_csv(f'{TO_DATA}cwe_newonset_selected.csv', sep=';', index=False)



#### Chronic children only ####
df_chronic = pd.read_csv(f'{TO_DATA}cwe_chronic.csv', sep=';')

# correlation matrix for chronic children
cor_matrix_chronic = df_chronic[predictors].corr()
plot_correlations(cor_matrix_chronic, title="Correlation Matrix for Chronic Children")

# Refine predictors
predictors_refined_chronic = [
    'repetition', # .57 with 'retraction' -> 2 models
    'retraction', # .57 with 'repititopns' -> 2 models
    'unfilled_pause', 
    'nonword',  
    'filled_pause',  
    'error', 
    'nr_lines',
    # 'nr_words', # corr with nr_lines AND nr_words_per_line
    'nr_words_per_line'
]

# remove features and save
rm_features = ['unfilled_pause_longer', 'unfilled_pause_longest',  
               'nr_words']
df_chronic = df_chronic.drop(columns=rm_features)
df_chronic.to_csv(f'{TO_DATA}cwe_chronic_selected.csv', sep=';', index=False)