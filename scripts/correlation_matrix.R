library(tidyverse)
library(lmerTest)
library(lme4)
library(Matrix)
library(ggcorrplot)

# hardcode home
setwd('/home/alex/Documents/02_study/duesseldorf/MA_Linguistik/23_WS_Python/epilepsy_chat/scripts')

setwd('../data')
# setwd('../scripts')
getwd()

df <- read.csv('cwe_all.csv', sep = ';')
glimpse(df)
df$child_id <- as.factor(df$child_id)
df$gender <- as.factor(df$gender)
df$age_months <- as.integer(df$age_months)
# 
# correlation matrix

predictors <- c('repetition', # .59 with 'retraction' -> 2 models
                'retraction', # .59 with 'repititopns' -> 2 models
                'unfilled_pause', 
                'unfilled_pause_longer', # vavoured over 'unfilled_pause_longest' because more data
                'unfilled_pause_longest', # .62 with 'unfilled_pause_longer'
                'nonword',  # removed as there are none
                'filled_pause',  # removed as there are none
                'error', 
                'nr_lines',
                'nr_words', # .77 with 'nr_lines'
                'nr_words_per_line'
                )
cor_matrix <- cor(df[, predictors])  # Only numeric columns
# Print the correlation matrix
ggcorrplot(cor_matrix, lab = TRUE)

predictors_refined <- c('repetition', # .59 with 'retraction' -> 2 models
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
                )
cor_matrix <- cor(df[, predictors_refined])  # Only numeric columns
# Print the correlation matrix
ggcorrplot(cor_matrix, lab = TRUE)

# remove features from df
rm_features <- c('unfilled_pause_longest', 'nonword', 'filled_pause', 'nr_words')
df <- df %>% select(-all_of(rm_features))

# save df
write.csv2(df, 'cwe_all_selected.csv')

#### recent children only ####

df <- read.csv('cwe_recent.csv', sep = ';')
glimpse(df)
df$child_id <- as.factor(df$child_id)
df$gender <- as.factor(df$gender)
df$age_months <- as.integer(df$age_months)
# 
# correlation matrix

predictors <- c('repetition', # 
                'retraction', # 
                'unfilled_pause', 
                'unfilled_pause_longer', # 
                'unfilled_pause_longest', # 
                'nonword',  # 
                'filled_pause',  # 
                'error', 
                'nr_lines',
                'nr_words', # 
                'nr_words_per_line'
                )
cor_matrix <- cor(df[, predictors])  # Only numeric columns
# Print the correlation matrix
ggcorrplot(cor_matrix, lab = TRUE)

predictors_refined <- c('repetition', # .67 with 'retraction' -> 2 models
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
                )
cor_matrix <- cor(df[, predictors_refined])  # Only numeric columns
# Print the correlation matrix
ggcorrplot(cor_matrix, lab = TRUE)

# remove features from df
rm_features <- c('unfilled_pause_longest', 'nonword', 'filled_pause', 'nr_words')
df <- df %>% select(-all_of(rm_features))

# save df
write.csv2(df, 'cwe_recent_selected.csv')
#### Chronic children only ####

df <- read.csv('cwe_chronic.csv', sep = ';')
glimpse(df)
df$child_id <- as.factor(df$child_id)
df$gender <- as.factor(df$gender)
df$age_months <- as.integer(df$age_months)
# 
# correlation matrix

predictors <- c('repetition', # .59 with 'retraction' -> 2 models
                'retraction', # .59 with 'repititopns' -> 2 models
                'unfilled_pause', 
                'unfilled_pause_longer', # vavoured over 'unfilled_pause_longest' because more data
                'unfilled_pause_longest', # .62 with 'unfilled_pause_longer'
                'nonword',  # removed as there are none
                'filled_pause',  # removed as there are none
                'error', 
                'nr_lines',
                'nr_words', # .77 with 'nr_lines'
                'nr_words_per_line'
                )
cor_matrix <- cor(df[, predictors])  # Only numeric columns
# Print the correlation matrix
ggcorrplot(cor_matrix, lab = TRUE)

predictors_refined <- c('repetition', # .57 with 'retraction' -> 2 models
                'retraction', # .57 with 'repititopns' -> 2 models
                'unfilled_pause', 
                'unfilled_pause_longer', # vavoured over 'unfilled_pause_longest' because more data
                # 'unfilled_pause_longest', # .81 with 'unfilled_pause_longer'
                # 'nonword',  # removed as there are none
                # 'filled_pause',  # removed as there are none
                'error', 
                'nr_lines',
                # 'nr_words', # .77 with 'nr_lines'
                'nr_words_per_line'
                )
cor_matrix <- cor(df[, predictors_refined])  # Only numeric columns
# Print the correlation matrix
ggcorrplot(cor_matrix, lab = TRUE)

# remove features from df
rm_features <- c('unfilled_pause_longest', 'nonword', 'filled_pause', 'nr_words')
df <- df %>% select(-one_of(rm_features))

# save df
write.csv(df, 'cwe_chronic_selected.csv', sep = ';')