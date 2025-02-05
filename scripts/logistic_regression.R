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

df <- read.csv('cwe_data.csv', sep = ';')
glimpse(df)
df$child_id <- as.factor(df$child_id)
df$gender <- as.factor(df$gender)
df$age_months <- as.integer(df$age_months)

# correlation matrix

predictors <- c('repetition', # .59 with 'retraction' -> 2 models
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
                # 'gender', # not included as it is not numeric
                # 'age_months' # not included as there are NAs
                )
cor_matrix <- cor(df[, predictors])  # Only numeric columns
# Print the correlation matrix
print(cor_matrix)
ggcorrplot(cor_matrix, lab = TRUE)


# glmer

# child_id + repetition + retraction + unfilled_pause + unfilled_pause_longer + unfilled_pause_longest + nonword + filled_pause + error + nr_lines + nr_words + nr_words_per_line + age_months + gender

m1 <- glmer(cwe_sick ~ repetition + retraction + unfilled_pause + unfilled_pause_longer + error + nr_lines + nr_words_per_line + (1|child_id), family = binomial, data = df)

m0 <- glmer(cwe_sick ~ repetition + retraction + unfilled_pause + unfilled_pause_longer + error + nr_lines + nr_words_per_line + gender + (1|child_id), family = binomial, data = df)
m1 <- glmer(cwe_sick ~ retraction + unfilled_pause + unfilled_pause_longer + error + nr_lines + nr_words_per_line + gender + (1|child_id), family = binomial, data = df)
m2 <- glmer(cwe_sick ~ repetition + unfilled_pause + unfilled_pause_longer + error + nr_lines + nr_words_per_line + gender + (1|child_id), family = binomial, data = df)
BIC(m0, m1, m2)
# taking our the correlated values improves the model, I take 'repetition' as there is less data

m11 <- glmer(cwe_sick ~ retraction + unfilled_pause + unfilled_pause_longer + error + nr_lines + nr_words_per_line + gender + (1|child_id), family = binomial, data = df)
m12 <- glmer(cwe_sick ~ retraction + (1|child_id), family = binomial, data = df)
BIC(m11, m12)

summary(m2)
