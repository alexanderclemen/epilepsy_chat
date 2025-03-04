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

# scale the predictors
df$nr_lines <- scale(df$nr_lines)
df$nr_words_per_line <- scale(df$nr_words_per_line)
df$retraction <- scale(df$retraction)
df$repetition <- scale(df$repetition)
df$unfilled_pause <- scale(df$unfilled_pause)
df$unfilled_pause_longer <- scale(df$unfilled_pause_longer)
df$unfilled_pause_longest <- scale(df$unfilled_pause_longest)
df$nonword <- scale(df$nonword)
df$filled_pause <- scale(df$filled_pause)
df$error <- scale(df$error)
df$nr_words <- scale(df$nr_words)
df$age_months <- scale(df$age_months)

# glmer

# child_id + repetition + retraction + unfilled_pause + unfilled_pause_longer + unfilled_pause_longest + nonword + filled_pause + error + nr_lines + nr_words + nr_words_per_line + age_months + gender

m0 <- glmer(cwe_sick ~ repetition + retraction + unfilled_pause + unfilled_pause_longer + error + nr_lines + nr_words_per_line + gender + (1|child_id), family = binomial, data = df)
m1 <- glmer(cwe_sick ~ retraction + unfilled_pause + unfilled_pause_longer + error + nr_lines + nr_words_per_line + gender + (1|child_id), family = binomial, data = df)
m2 <- glmer(cwe_sick ~ repetition + unfilled_pause + unfilled_pause_longer + error + nr_lines + nr_words_per_line + gender + (1|child_id), family = binomial, data = df)
BIC(m0, m1, m2)
# taking our the correlated values improves the model, I take 'repetition' as there is less data

m11 <- glmer(cwe_sick ~ repetition + unfilled_pause + unfilled_pause_longer + error + nr_lines + nr_words_per_line + gender + (1|child_id), family = binomial, data = df)
m12 <- glmer(cwe_sick ~ repetition + unfilled_pause + unfilled_pause_longer + error + nr_lines + nr_words_per_line + (1|child_id), family = binomial, data = df)
AIC(m11, m12)
# a model with 0 predictors is best with BIC comparisons and a model with all predoctors is best with AIC comparisons

summary(m12)
